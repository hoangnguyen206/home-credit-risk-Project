-- số khoản vay ngoài từng khách hàng

SELECT
    a.sk_id_curr,
    COUNT(b.sk_id_curr) AS n_bureau_loans
FROM application_train a
LEFT JOIN bureau b ON a.sk_id_curr = b.sk_id_curr
GROUP BY a.sk_id_curr
ORDER BY a.sk_id_curr;