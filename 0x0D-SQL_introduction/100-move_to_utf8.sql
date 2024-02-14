-- converts hbtn_0c_0 database to UTF8
-- Use hbtn_0c_0 database
USE hbtn_0c_0;

-- Convert the character set of the table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the character set of the field
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
