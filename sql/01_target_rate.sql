-- tỉ lệ vỡ nợ

SELECT
    target,
    COUNT(*) AS n_customers,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct     -- SUM(COUNT(*)) OVER () là tổng số khách hàng trong toàn bộ bảng, dùng để tính tỷ lệ phần trăm
FROM application_train
GROUP BY target
ORDER BY target;