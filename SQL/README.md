서브 쿼리 예시

```mysql
SELECT A.ID, B.AGE, A.COINS_NEEDED, A.POWER
FROM WANDS AS A , WANDS_PROPERTY AS B
WHERE A.CODE=B.CODE AND B.IS_EVIL=0
AND A.COINS_NEEDED=(
        SELECT MIN(A1.COINS_NEEDED)
        FROM WANDS AS A1 , WANDS_PROPERTY AS B1
        WHERE A1.CODE=B1.CODE AND B.IS_EVIL=0
        AND A.POWER=A1.POWER AND B.AGE=B1.AGE
)
ORDER BY A.POWER DESC ,  B.AGE DESC
```
