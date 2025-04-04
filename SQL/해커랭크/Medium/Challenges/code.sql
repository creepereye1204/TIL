SELECT A.HACKER_ID, A.NAME, COUNT(*) AS CHALLENGES_CREATED
FROM HACKERS AS A
JOIN CHALLENGES AS B ON A.HACKER_ID = B.HACKER_ID
GROUP BY A.HACKER_ID, A.NAME
HAVING COUNT(*) IN (
    SELECT TOTAL
    FROM (
        SELECT COUNT(*) AS TOTAL
        FROM CHALLENGES
        GROUP BY HACKER_ID
    ) AS subquery
    GROUP BY TOTAL
    HAVING COUNT(*) = 1
)
OR COUNT(*) = (
    SELECT MAX(TOTAL)
    FROM (
        SELECT COUNT(*) AS TOTAL
        FROM CHALLENGES
        GROUP BY HACKER_ID
    ) AS subquery
)
ORDER BY CHALLENGES_CREATED DESC, A.hacker_id;
