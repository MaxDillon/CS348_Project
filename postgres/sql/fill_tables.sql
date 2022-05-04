
-- Create Root User -- password: root --
INSERT INTO Account (username, pass_hash, money_invested) 
VALUES ('root', '$2b$12$wDyQIOBj6.RcxYHemxolr.unfu0TEdsx1MACglSlKBgaGh4.XvpDy', 0);

-- Create Example User -- password: example --
INSERT INTO Account (username, pass_hash, money_invested) 
VALUES ('example', '$2b$12$g.wF9IuRY5tnnLFyfy6MweAe1tb5CCa1ameIOnlcQwlfa4hLTSLwO', 0);

-- Creates the companies' stocks we'll be trading --
INSERT INTO Company(company_id, company_name, current_trading_price, num_shares)
VALUES ('MSFT', 'Microsoft Corporation', 0, 30), 
       ('GOOGL', 'Alphabet Inc. ', 0, 2),
       ('AMZN', 'Amazon.com, Inc.', 0, 16),
       ('GS', 'The Goldman Sachs Group, Inc.', 0, 1),
       ('UBER', 'Uber Technologies Inc', 0, 0);

-- Fake company history --
INSERT INTO CompanyHistory (company_id, time_fetched, trading_price)
VALUES ('MSFT', extract(epoch from now()), 0),
       ('GOOGL', extract(epoch from now()), 0),
       ('AMZN', extract(epoch from now()), 0),
       ('GS', extract(epoch from now()), 0),
       ('UBER', extract(epoch from now()), 0);

INSERT INTO Transactions(company_id, user_id, time_executed, num_shares, buy_or_sell)
VALUES ('MSFT', 1, '1651551135', 3,'0'), 
       ('GOOGL', 1, '1651551200', 4,'1'),
       ('AMZN', 2, '1651551135', 5,'0');

-- Creates fund details --
INSERT INTO FundInfo (fund_name, fund_description, parent_company, fund_value, fund_invested)
VALUES ('Vanguard 500', 
       'As the industry’s first index fund for individual investors, the 500 Index Fund is a low-cost way to gain diversified exposure to the U.S. equity market. ',
       'Vanguard',
       0, 0);

-- Creates fund history --
INSERT INTO FundPerformance (ts, fund_value, fund_invested)
VALUES 
(0, 0, 0),
(10, 13, 0),
(20, 39, 0),
(30, 19, 0),
(40, 22, 0),
(50, 26, 0),
(60, 20, 0),
(70, 23, 0),
(80, 25, 0),
(90, 46, 0),
(1651291200, 55, 0),  /*Saturday, April 30, 2022 12:00:00 AM GMT-04:00 DST*/
(1651377599, 56, 0),  /*Saturday, April 30, 2022 11:59:59 PM GMT-04:00 DST*/
(1651377600, 70, 0),  /*Sunday, May 1, 2022 12:00:00 AM GMT-04:00 DST*/
(1651550399, 34, 0),  /*Monday, May 2, 2022 11:59:59 PM GMT-04:00 DST*/
(1651464000, 24, 0),  /*Monday, May 2, 2022 12:00:00 AM GMT-04:00 DST*/
(1651636799, 24, 0),  /*Tuesday, May 3, 2022 11:59:59 PM GMT-04:00 DST*/
(1651550400, 32, 0),  /*Tuesday, May 3, 2022 12:00:00 AM GMT-04:00 DST*/
(1651636800, 22, 0),  /*Wednesday, May 4, 2022 12:00:00 AM GMT-04:00 DST*/
(extract(epoch from now()), 0, 0);


INSERT INTO PaymentHistory (user_id, time_created, amount_invested)
VALUES 
(1, 1, 4),
(1, 6, 5),
(1, 14, 30),
(1, 34, 36),
(1, 61, 500),
(1, 85, 576);


