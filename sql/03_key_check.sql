-- kiểm tra khoá chính

-- mong muốn trả về rỗng
SELECT sk_id_curr, COUNT(*)
FROM application_train
GROUP BY sk_id_curr
HAVING COUNT(*) > 1;

-- bureau có sk_id_curr không có trong application_train
SELECT b.sk_id_curr
FROM bureau b
LEFT JOIN application_train a ON b.sk_id_curr = a.sk_id_curr
WHERE a.sk_id_curr IS NULL;



-- psql -U home_credit_app -d home_credit -h localhost -W