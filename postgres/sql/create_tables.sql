-- Creation of user table

CREATE TABLE IF NOT EXISTS Account (
  user_id SERIAL PRIMARY KEY,
  username varchar(250) NOT NULL,
  first_name varchar(250),
  last_name varchar(250),
  email varchar(250),
  phone INT,
  pass_hash BYTEA NOT NULL,
  money_invested INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Session (
  user_id INT NOT NULL,
  token BYTEA NOT NULL
);

-- Creation of holding table
CREATE TABLE IF NOT EXISTS Holding (
  company_id INT NOT NULL,
  company_name varchar(250) NOT NULL,
  stocks INT NOT NULL,
  buying_val INT NOT NULL,
  PRIMARY KEY (company_id)
);

-- Creation of market table
CREATE TABLE IF NOT EXISTS Market (
  company_id INT NOT NULL,
  market_name varchar(250) NOT NULL,
  total_stocks INT NOT NULL,
  trading_price INT NOT NULL,
  PRIMARY KEY (company_id)
);

-- Creation of store table
CREATE TABLE IF NOT EXISTS TransactionHistory (
  company_id INT NOT NULL,
  executed_by varchar(250) NOT NULL,
  buy_sell BOOLEAN NOT NULL,
  number INT NOT NULL,
  PRIMARY KEY (company_id)
);

-- Creation of user table
CREATE TABLE IF NOT EXISTS FundInformation (
  order_id INT NOT NULL,
  fund_name varchar(250) NOT NULL,
  free_money INT NOT NULL,
  keywords varchar(250) NOT NULL,
  fund_value INT NOT NULL,
  PRIMARY KEY (order_id)
);
