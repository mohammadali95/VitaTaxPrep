DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS hours;
DROP TABLE IF EXISTS volunteers;

CREATE TABLE events (
    name text NOT NULL CONSTRAINT events_pk PRIMARY KEY,
    date date NOT NULL,
    start_time text NOT NULL,
    end_time text NOT NULL,
    description text NOT NULL
);
CREATE TABLE hours (
    volunteers_email text NOT NULL,
    eventName text NOT NULL,
    start_time text NOT NULL,
    end_time text NOT NULL,
    CONSTRAINT hours_volunteers FOREIGN KEY (volunteers_email)
    REFERENCES volunteers (email)
);
CREATE TABLE volunteers (
    name text NOT NULL,
    email text NOT NULL CONSTRAINT volunteers_pk PRIMARY KEY,
    phone text NOT NULL,
    address text NOT NULL
);