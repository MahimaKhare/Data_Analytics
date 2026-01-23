Use school;
Select * from teachers;

--- Update
Update teachers
Set Name = 'Rahul Sharma',
    Gender = 'Male'
Where TeacherID = 5;

--- Delete
Delete from teachers 
Where TeacherID = 5;    

--- Top
Select * from teachers
Limit 5;

--- Top 5 in coloumn
Select City from teachers
limit 5;  

--- Aggregate Function
--- Min
Select Min(Experience)
from teachers; 

--- Max
Select Max(Experience)
from teachers; 

--- Count
Select count(TeacherID)
from teachers; 

--- Sum 
Select Sum(Experience)
from teachers; 

--- Avg
Select Avg(Experience)
from teachers; 

