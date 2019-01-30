/*This creates the Database*/

/*create businesses table*/

CREATE TABLE businesses (
 business_id INTEGER PRIMARY KEY,
 business_name TEXT NOT NULL,
 business_category TEXT NOT NULL,
 address_line_1 TEXT,
 address_line_2 TEXT,
 address_line_3 TEXT,
 postcode TEXT UNIQUE,
 phone text NOT NULL UNIQUE
);

/*create people table*/
CREATE TABLE people (
 person_id INTEGER PRIMARY KEY,
 first_name TEXT NOT NULL,
 last_name TEXT NOT NULL,
 address_line_1 TEXT,
 address_line_2 TEXT,
 address_line_3 TEXT,
 postcode TEXT UNIQUE,
 phone text NOT NULL UNIQUE
);

/*create postcode table*/
CREATE TABLE people (
 postcode_id INTEGER PRIMARY KEY,
 longitude DECIMAL,
 latitude DECIMAL,
 postcode TEXT UNIQUE
);
