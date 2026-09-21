SELECT
         id,
         user_id,
         total,
         SUM(total) OVER () (PARTITION BY user_id) AS user_total
FROM orders;