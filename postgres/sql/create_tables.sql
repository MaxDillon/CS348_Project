-- Creation of user table

CREATE TABLE IF NOT EXISTS Account (
  user_id SERIAL PRIMARY KEY,
  username varchar(250) NOT NULL,
  first_name varchar(250),
  last_name varchar(250),
  email varchar(250),
  phone varchar(250),
  pass_hash BYTEA NOT NULL,
  money_invested INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS LoginSession (
  token BYTEA PRIMARY KEY,
  user_id INT REFERENCES Account (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
  time_created TIMESTAMP 
);

CREATE TABLE IF NOT EXISTS PaymentHistory (
  user_id INT REFERENCES Account (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
  time_created TIMESTAMP NOT NULL,
  amount_invested INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Company (
  company_id varchar(250) PRIMARY KEY,
  company_name varchar(250) NOT NULL,
  current_trading_price MONEY NOT NULL,
  num_shares INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Transactions (
  company_id varchar(250) REFERENCES Company(company_id) ON UPDATE CASCADE ON DELETE CASCADE,
  user_id INT REFERENCES Account (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
  time_executed TIMESTAMP NOT NULL,
  num_shares INT NOT NULL,
  buy_or_sell BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS Employee (
  employee_id SERIAL PRIMARY KEY,
  username varchar(250) NOT NULL,
  first_name varchar(250),
  last_name varchar(250),
  email varchar(250),
  phone varchar(250),
  pass_hash BYTEA NOT NULL
);

CREATE TABLE IF NOT EXISTS CompanyHistory (
  company_id varchar(250) REFERENCES Company(company_id) ON UPDATE CASCADE ON DELETE CASCADE,
  time_fetched INT NOT NULL,
  trading_price MONEY NOT NULL
);

CREATE TABLE IF NOT EXISTS Manages (
  manager_id INT REFERENCES Employee(employee_id) ON UPDATE CASCADE ON DELETE CASCADE,
  employee_id INT REFERENCES Employee(employee_id) ON UPDATE CASCADE ON DELETE CASCADE
);
