WITH user_stats AS(
         SELECT
             user_id,
             COUNT(*) AS orders_count,
             SUM(total) AS total_spent
         FROM orders
         WHERE status = 'paid'
         GROUP BY user_id
)
SELECT
    username,
    orders_count,
    total_spent
FROM users AS u
JOIN user_stats AS us
    ON u.id = us.user_id