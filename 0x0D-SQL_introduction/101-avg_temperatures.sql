-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- data imported with this command `cat temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0` (Second command may be different depends on ur setup)
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
