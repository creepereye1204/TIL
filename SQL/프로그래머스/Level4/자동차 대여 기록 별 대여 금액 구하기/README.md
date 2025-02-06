# 톱니바퀴

## 📝 피드백

```mysql
(SELECT * FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE='트럭') AS B

```

- 조건은 서브 쿼리 안에서 이루어져야 됨 외부 조인 시 트럭이라는 조건을 걸어버리면 조인된 상태에서는 할인 정책이 없는 경우에는 조건에서 바 져버림!!

- 조인할 때 웬만하면 서브 쿼리 안에서 조건을 걸자
- 조인할 때 예외 상황을 잘 생각하자
