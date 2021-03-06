SELECT
	DEPARTMENT.NAME, COUNT(STUDENT.ID) AS STUDENT_NUMBER
FROM
	DEPARTMENT
		LEFT OUTER JOIN
	STUDENT
		ON DEPARTMENT.ID = STUDENDT.DEPT_ID
GROUP BY DEPARTMENT.NAME
ORDER BY STUDENT_NUMBER DESC, DEPARTMENT.NAME;

SELECT * FROM employee WHERE salary = (SELECT max(salary) FROM employee);

SELECT Name, count(*) from employee GROUP BY Name HAVING count(*) >1;

DELETE FROM employee WHERE id not in ( SELECT max(id) FROM employee GROUP by name );
