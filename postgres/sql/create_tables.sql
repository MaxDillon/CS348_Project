-- Creation of user table

CREATE TABLE IF NOT EXISTS Account (
  user_id SERIAL PRIMARY KEY,
  username varchar(250) NOT NULL,
  first_name varchar(250),
  last_name varchar(250),
  email varchar(250),
  phone varchar(250),
  pass_hash BYTEA NOT NULL,
  money_invested NUMERIC(16,2) NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS LoginSession (
  token BYTEA PRIMARY KEY,
  user_id INT REFERENCES Account (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
  time_created DECIMAL 
);

CREATE TABLE IF NOT EXISTS PaymentHistory (
  user_id INT REFERENCES Account (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
  time_created DECIMAL NOT NULL,
  amount_invested INT NOT NULL
);
/*B+ tree Index on time_created on PaymentHistory */
CREATE INDEX idx_timeCreated 
ON PaymentHistory USING btree(time_created);


CREATE TABLE IF NOT EXISTS Company (
  company_id varchar(250) PRIMARY KEY,
  company_name varchar(250) NOT NULL,
  current_trading_price NUMERIC(16,2) NOT NULL,
  num_shares INT NOT NULL
);

/*Hash Index on company_id on Company */
CREATE INDEX idx_compIdCompany 
ON Company USING HASH (company_id);

CREATE TABLE IF NOT EXISTS Transactions (
  company_id varchar(250) REFERENCES Company(company_id) ON UPDATE CASCADE ON DELETE CASCADE,
  user_id INT REFERENCES Account (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
  time_executed DECIMAL NOT NULL,
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
  time_fetched DECIMAL NOT NULL,
  trading_price NUMERIC(16,2) NOT NULL
);

/*B+ Index on company_id on CompanyHistory */
CREATE INDEX idx_compIdHistory 
ON CompanyHistory USING btree (company_id);

CREATE TABLE IF NOT EXISTS Manages (
  manager_id INT REFERENCES Employee(employee_id) ON UPDATE CASCADE ON DELETE CASCADE,
  employee_id INT REFERENCES Employee(employee_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS FundInfo (
  fund_name varchar(50) NOT NULL PRIMARY KEY,
  fund_description varchar(200) NOT NULL,
  parent_company varchar(50) NOT NULL,
  fund_value NUMERIC(16,2) NOT NULL,
  fund_invested NUMERIC(16,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS FundPerformance (
  ts DECIMAL NOT NULL,
  fund_value NUMERIC(16,2) NOT NULL,
  fund_invested NUMERIC(16,2) NOT NULL
);

/*B+ Index on ts on FundPerformance */
CREATE INDEX idx_ts 
ON FundPerformance USING btree(ts);