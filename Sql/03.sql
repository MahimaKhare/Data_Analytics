Use school;

--- Table selection 
Select * from students;

--- Column selection
Select Age from students;

--- Multiple coloumn selection
Select Name, Age from students;

--- Distinct
Select distinct City from students;

--- Count
Select count(distinct City) from students;

--- Where
Select Age from students
where Age > 15;

--- Order by 
Select * from students
order by Age asc;

--- And
Select * from students
where Age > 15 and Marks > 80;

--- OR
Select * from students
where Age > 15 or Marks > 80;

--- Not
Select * from students
where not Age = 18;

--- 
Select City from students
where City is not null;
