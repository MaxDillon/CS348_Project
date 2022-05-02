
-- Create Root User -- password: root --
INSERT INTO Account (username, pass_hash, money_invested) 
VALUES ('root', '$2b$12$wDyQIOBj6.RcxYHemxolr.unfu0TEdsx1MACglSlKBgaGh4.XvpDy', 0);

-- Create Example User -- password: example --
INSERT INTO Account (username, pass_hash, money_invested) 
VALUES ('example', '$2b$12$g.wF9IuRY5tnnLFyfy6MweAe1tb5CCa1ameIOnlcQwlfa4hLTSLwO', 0);

-- Creates the companies' stocks we'll be trading --
INSERT INTO Company(company_id, company_name, current_trading_price, num_shares)
VALUES ('MSFT', 'Microsoft', 0, 0), 
       ('GOOGL', 'Google', 0, 0),
       ('AMZN', 'Amazon', 0, 0),
       ('GS', 'Goldman Sachs', 0, 0),
       ('UBER', 'Uber', 0, 0);

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
(extract(epoch from now()), 0, 0);


INSERT INTO PaymentHistory (user_id, time_created, amount_invested)
VALUES 
(1, 1, 4),
(1, 6, 5),
(1, 14, 30),
(1, 34, 36),
(1, 61, 500),
(1, 85, 576);


