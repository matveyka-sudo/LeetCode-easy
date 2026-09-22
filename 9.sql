WITH most_dear AS (
    SELECT
        id,
        user_id,
        total,
        DENSE_RANK() OVER (
            PARTITION BY user_id
            ORDER BY total DESC
        ) AS rn
    FROM orders
)

SELECT
    u.username,
    md.id AS order_id,
    md.total
FROM most_dear AS md
JOIN users AS u
    ON u.id = md.user_id
WHERE md.rn = 1;