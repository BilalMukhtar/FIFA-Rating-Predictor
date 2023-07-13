SELECT *
FROM PLAYER p
JOIN PLAYER_STATS ps ON p.player_id = ps.player_id
JOIN PLAYER_RATINGS pr ON p.player_id = pr.player_id
WHERE ps.season = 22 and pr.season = 23;


SELECT *, *, curr.*, prevr.*
FROM PLAYER p
JOIN PLAYER_STATS ps ON p.player_id = ps.player_id
JOIN PLAYER_RATINGS prevr ON p.player_id = prevr.player_id
JOIN PLAYER_RATINGS curr ON p.player_id = curr.player_id
WHERE ps.season = prevr.season AND ps.season = curr.season-1;