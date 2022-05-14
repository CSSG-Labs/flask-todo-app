-- For V2: when we add user accounts + user auth
--
-- DROP TABLE IF EXISTS user;
-- DROP TABLE IF EXISTS task;

-- CREATE TABLE user(
--     user_id INTEGER PRIMARY KEY,
--     username TEXT UNIQUE NOT NULL,
--     password TEXT NOT NULL
-- );

-- CREATE TABLE task(
--     task_id INTEGER PRIMARY KEY,
--     desc TEXT NOT NULL,
--     user_id INTEGER NOT NULL,
--     FOREIGN KEY (user_id) REFERENCES user (user_id)
--         ON DELETE CASCADE
-- );

DROP TABLE IF EXISTS task;

CREATE TABLE todo(
    todo_id INTEGER PRIMARY KEY,
    desc TEXT NOT NULL
)