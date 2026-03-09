SELECT department,
COUNT(*) AS total_patients,
AVG(wait_time_minutes) AS avg_wait_time
FROM hospital_data
GROUP BY department
ORDER BY avg_wait_time DESC;

SELECT department,
SUM(CASE WHEN readmission_flag = 1 THEN 1 ELSE 0 END) AS readmissions,
COUNT(*) AS total_patients,
ROUND(100.0 * SUM(CASE WHEN readmission_flag = 1 THEN 1 ELSE 0 END) / COUNT(*),2) AS readmission_rate
FROM hospital_data
GROUP BY department
ORDER BY readmission_rate DESC;
