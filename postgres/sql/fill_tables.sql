
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
VALUES (CURRENT_DATE, 0, 0);


INSERT INTO PaymentHistory (user_id, time_created, amount_invested)
VALUES 
(1, 1574588929, 10),
(1, 1774588929, 2),
(1, 1574582346, 3),
(1, 1574581191, 7),
(1, 1574588929, 5),
(1, 1374588929, 12);



INSERT INTO CompanyHistory (company_id, time_fetched, trading_price)
VALUES 
('GOOGL', 1511362342, 1),
('GOOGL', 1588366500, 2),
('GOOGL', 1588366502, 3),
('GOOGL', 1588366505, 4),
('GOOGL', 1621324232, 5),
('GOOGL', 1651438500, 6),
('GOOGL', 1651438502, 7),
('GOOGL', 1651438505, 8),
('GOOGL', 1689234123, 9);
