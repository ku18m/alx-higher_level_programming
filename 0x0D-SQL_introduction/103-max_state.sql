-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- data imported with this command `cat temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0` (Second command may be different depends on ur setup)
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC LIMIT 3;
