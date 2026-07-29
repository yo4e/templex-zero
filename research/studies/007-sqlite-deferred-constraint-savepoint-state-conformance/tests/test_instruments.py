import dataclasses
import pathlib
import unittest

from actions import parse_action
from comparator import compare_records
from harness import SQLiteHarness
from model import IndependentModel


def model_run(tokens):
    return IndependentModel().run_sequence("T", tuple(parse_action(token) for token in tokens))


class ActionTests(unittest.TestCase):
    def test_round_trip(self):
        tokens = ["begin", "savepoint(a)", "rollback_to(z)", "insert_parent(10)", "insert_child(deferred,201,99)", "delete_child(deferred_restrict,301)"]
        self.assertEqual(tokens, [parse_action(token).token() for token in tokens])

    def test_rejects_unbounded_name_and_relation(self):
        with self.assertRaises(ValueError):
            parse_action("savepoint(e)")
        with self.assertRaises(ValueError):
            parse_action("insert_child(other,1,2)")


class ModelTests(unittest.TestCase):
    def test_rollback_to_retains_mark(self):
        records = model_run(["begin", "savepoint(a)", "insert_parent(10)", "rollback_to(a)", "insert_parent(11)", "release(a)", "commit"])
        self.assertEqual((1, 2, 3), records[3].parent)
        self.assertTrue(records[3].in_transaction)
        self.assertEqual((1, 2, 3, 11), records[-1].parent)
        self.assertFalse(records[-1].in_transaction)

    def test_failed_commit_preserves_transaction(self):
        records = model_run(["begin", "insert_child(deferred,201,99)", "commit", "rollback"])
        self.assertEqual("foreign_key", records[2].expected_error_key)
        self.assertTrue(records[2].in_transaction)
        self.assertEqual(((201, 99),), records[2].child_deferred)
        self.assertFalse(records[-1].in_transaction)

    def test_duplicate_name_targets_latest(self):
        records = model_run(["begin", "savepoint(a)", "insert_parent(10)", "savepoint(a)", "insert_parent(11)", "rollback_to(a)", "release(a)", "release(a)", "commit"])
        self.assertEqual((1, 2, 3, 10), records[5].parent)
        self.assertEqual((1, 2, 3, 10), records[-1].parent)

    def test_outer_release_failure_preserves_nested_marks(self):
        records = model_run(["savepoint(a)", "savepoint(b)", "insert_child(deferred,201,99)", "release(a)", "rollback_to(b)", "release(b)", "rollback_to(a)", "release(a)"])
        self.assertEqual("foreign_key", records[3].expected_error_key)
        self.assertTrue(records[3].in_transaction)
        self.assertEqual((), records[4].child_deferred)
        self.assertFalse(records[-1].in_transaction)

    def test_restrict_uses_frozen_mapping(self):
        records = model_run(["begin", "insert_parent(99)", "insert_child(deferred_restrict,301,99)", "delete_parent(99)", "rollback"])
        self.assertEqual((787, "SQLITE_CONSTRAINT_FOREIGNKEY"), (records[3].sqlite_errorcode, records[3].sqlite_errorname))


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.harness = SQLiteHarness("schema.sql")

    def run_tokens(self, tokens):
        return self.harness.run_sequence("T", tuple(parse_action(token) for token in tokens))

    def test_missing_savepoint_mapping(self):
        record = self.run_tokens(["begin", "release(z)", "commit"])[1]
        self.assertEqual(("sqlite3.OperationalError", 1, "SQLITE_ERROR"), (record.python_exception, record.sqlite_errorcode, record.sqlite_errorname))

    def test_deferred_violation_visible(self):
        record = self.run_tokens(["begin", "insert_child(deferred,201,99)", "rollback"])[1]
        self.assertEqual((("child_deferred", 201, "parent", 0),), record.foreign_key_check)

    def test_restrict_reports_trigger_extended_code(self):
        record = self.run_tokens(["begin", "insert_parent(99)", "insert_child(deferred_restrict,301,99)", "delete_parent(99)", "rollback"])[3]
        self.assertEqual(("sqlite3.IntegrityError", 1811, "SQLITE_CONSTRAINT_TRIGGER"), (record.python_exception, record.sqlite_errorcode, record.sqlite_errorname))
        self.assertIn(99, record.parent)


class ComparatorAndSeparationTests(unittest.TestCase):
    def test_records_are_frozen(self):
        record = model_run(["begin"])[0]
        with self.assertRaises(dataclasses.FrozenInstanceError):
            record.in_transaction = False

    def test_basic_model_harness_match(self):
        actions = tuple(parse_action(token) for token in ["begin", "savepoint(a)", "insert_parent(10)", "rollback_to(a)", "release(a)", "commit"])
        self.assertTrue(compare_records(IndependentModel().run_sequence("T", actions), SQLiteHarness("schema.sql").run_sequence("T", actions)).matched)

    def test_source_separation(self):
        model_source = pathlib.Path("model.py").read_text()
        harness_source = pathlib.Path("harness.py").read_text()
        comparator_source = pathlib.Path("comparator.py").read_text()
        self.assertNotIn("import sqlite3", model_source)
        self.assertNotIn("from harness", model_source)
        self.assertNotIn("from model", harness_source)
        self.assertNotIn("from model", comparator_source)
        self.assertNotIn("from harness", comparator_source)


if __name__ == "__main__":
    unittest.main()
