
-- Create Root User -- password: root --
INSERT INTO Account (username, pass_hash, money_invested) 
VALUES ('root', '$2b$12$wDyQIOBj6.RcxYHemxolr.unfu0TEdsx1MACglSlKBgaGh4.XvpDy', 0);

-- Create Example User -- password: example --
INSERT INTO Account (username, pass_hash, money_invested) 
VALUES ('example', '$2b$12$g.wF9IuRY5tnnLFyfy6MweAe1tb5CCa1ameIOnlcQwlfa4hLTSLwO', 0);

-- Creates the companies' stocks we'll be trading --
INSERT INTO Company(company_id, company_name, current_trading_price, num_shares)
VALUES ('MSFT', 'Microsoft Corporation', 0, 0), 
       ('GOOGL', 'Alphabet Inc. ', 0, 0),
       ('AMZN', 'Amazon.com, Inc.', 0, 0),
       ('GS', 'The Goldman Sachs Group, Inc.', 0, 0),
       ('UBER', 'Uber Technologies Inc', 0, 0);