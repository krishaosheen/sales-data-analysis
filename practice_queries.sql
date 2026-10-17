-- Practice SQL queries for the synthetic sales_data table.
-- Syntax for date/month extraction varies by database.

-- 1. Revenue and estimated profit by product
SELECT product,
       SUM(units_sold * unit_price) AS revenue,
       SUM(units_sold * (unit_price - unit_cost)) AS estimated_profit
FROM sales_data
GROUP BY product
ORDER BY revenue DESC;

-- 2. Compare regions
SELECT region,
       SUM(units_sold) AS units_sold,
       SUM(units_sold * unit_price) AS revenue,
       SUM(units_sold * (unit_price - unit_cost)) AS estimated_profit
FROM sales_data
GROUP BY region
ORDER BY estimated_profit DESC;

-- 3. Monthly performance (SQLite-compatible month expression)
SELECT strftime('%Y-%m', date) AS month,
       SUM(units_sold * unit_price) AS revenue,
       SUM(units_sold * (unit_price - unit_cost)) AS estimated_profit
FROM sales_data
GROUP BY strftime('%Y-%m', date)
ORDER BY month;

-- 4. Check for rows with invalid negative quantities or prices
SELECT *
FROM sales_data
WHERE units_sold < 0 OR unit_price < 0 OR unit_cost < 0;
