-- 1. Customers with Highest Shipments

SELECT
    c.id,
    c.name,
    COUNT(s.id) AS total_shipments
FROM customers c
JOIN packages p ON c.id = p.customer_id
JOIN shipments s ON p.id = s.package_id
GROUP BY c.id, c.name
ORDER BY total_shipments DESC;

-- 2. Total Delivered Packages

SELECT
    COUNT(*) AS total_delivered_packages
FROM shipments
WHERE status = 'Delivered';

-- 3. Pending Shipments

SELECT
    s.id,
    s.shipment_name,
    s.status,
    p.package_name,
    c.name AS customer_name
FROM shipments s
JOIN packages p ON s.package_id = p.id
JOIN customers c ON p.customer_id = c.id
WHERE s.status = 'Pending';

-- 4. Monthly Shipment Report

SELECT
    strftime('%Y-%m', created_at) AS shipment_month,
    COUNT(*) AS total_shipments,
    SUM(CASE WHEN status='Delivered' THEN 1 ELSE 0 END) AS delivered_shipments,
    SUM(CASE WHEN status='Returned' THEN 1 ELSE 0 END) AS returned_shipments,
    SUM(CASE WHEN status='Pending' THEN 1 ELSE 0 END) AS pending_shipments
FROM shipments
GROUP BY strftime('%Y-%m', created_at)
ORDER BY shipment_month;

-- 5. Average Delivery Time

SELECT
    ROUND(
        AVG(
            JULIANDAY(delivered_at) -
            JULIANDAY(created_at)
        ),
        2
    ) AS avg_delivery_days
FROM shipments
WHERE status='Delivered';

-- 6. Rank Customers by Shipment Count

SELECT
    c.id,
    c.name,
    COUNT(s.id) AS shipment_count,
    RANK() OVER(
        ORDER BY COUNT(s.id) DESC
    ) AS customer_rank
FROM customers c
JOIN packages p ON c.id = p.customer_id
JOIN shipments s ON p.id = s.package_id
GROUP BY c.id, c.name;