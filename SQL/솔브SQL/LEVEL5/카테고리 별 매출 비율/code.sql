WITH MAIN AS(
  SELECT category,sub_category,SUM(SALES) AS sales_sub_category
  FROM records
  GROUP BY category,sub_category

),
SUB AS(
  SELECT category,SUM(SALES) AS sales_category
  FROM records
  GROUP BY category
),
TOTAL AS(
  SELECT SUM(SALES) AS sales_total
  FROM records
)

SELECT A.CATEGORY,
A.SUB_CATEGORY,
ROUND(A.sales_sub_category,2) AS sales_sub_category,
ROUND(B.sales_category,2) AS sales_category,
ROUND(C.SALES_TOTAL,2) AS sales_total,
ROUND((A.sales_sub_category/B.sales_category)*100,2) AS pct_in_category,
ROUND((A.sales_sub_category/C.SALES_TOTAL)*100,2) AS pct_in_total
FROM 
MAIN AS A JOIN SUB AS B
ON A.CATEGORY = B.CATEGORY
CROSS JOIN TOTAL AS C

