-- this script adds a summary of every score by the amount of times
-- it is listed in the table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;