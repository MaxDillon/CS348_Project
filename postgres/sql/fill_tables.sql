
-- Create Root User -- password: root --
INSERT INTO Customer (user_id, username, pass_hash, money_invested) 
VALUES (1, 'root', '$2b$12$wDyQIOBj6.RcxYHemxolr.unfu0TEdsx1MACglSlKBgaGh4.XvpDy', 0);

-- Create Example User -- password: example --
INSERT INTO Customer (user_id, username, pass_hash, money_invested) 
VALUES (2, 'example', '$2b$12$g.wF9IuRY5tnnLFyfy6MweAe1tb5CCa1ameIOnlcQwlfa4hLTSLwO', 0);