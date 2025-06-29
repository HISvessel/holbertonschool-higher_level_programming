-- this script retrieves all of the members who have a high
-- enough score and arranges it in the correct order
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;