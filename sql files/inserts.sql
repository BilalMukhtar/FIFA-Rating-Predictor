SELECT *
FROM PLAYER p
JOIN PLAYER_STATS ps ON p.player_id = ps.player_id
JOIN PLAYER_RATINGS pr ON p.player_id = pr.player_id
WHERE ps.season = 22 and pr.season = 23;

SELECT * FROM PLAYER