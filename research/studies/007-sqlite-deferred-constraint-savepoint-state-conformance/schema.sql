PRAGMA foreign_keys = ON;

CREATE TABLE parent (
    id INTEGER PRIMARY KEY
);

CREATE TABLE child_immediate (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES parent(id)
        ON DELETE NO ACTION
        NOT DEFERRABLE INITIALLY IMMEDIATE
);

CREATE TABLE child_deferred (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES parent(id)
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE child_restrict (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES parent(id)
        ON DELETE RESTRICT
        DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO parent(id) VALUES (1), (2), (3);
