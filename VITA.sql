DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS hours;
DROP TABLE IF EXISTS volunteers;

CREATE TABLE events (
    name text NOT NULL CONSTRAINT events_pk PRIMARY KEY,
    date date NOT NULL,
    start_time text NOT NULL,
    end_time text NOT NULL,
    description text NOT NULL
	image text NOT NULL
);
CREATE TABLE hours (
	email TEXT NOT NULL,
	eventName TEXT NOT NULL,
	hours TEXT NOT NULL
);
CREATE TABLE volunteers (
    name text NOT NULL,
    address text NOT NULL,
    city text NOT NULL,
    state text NOT NULL,
    zip text NOT NULL,
    email text NOT NULL,
    phone text NOT NULL,
    dob text NOT NULL,
    languages text NOT NULL
);
