Create database School;
use School;

--Teachers Table
create table Teachers(
    TeacherID INT PRIMARY KEY,
    Name VARCHAR(50),
    Subject VARCHAR(40),
    Gender VARCHAR(10),
    Experience INT,       
    Salary INT,
    City VARCHAR(30)
)

insert into Teachers Values
(1, 'Anita Sharma', 'Mathematics', 'Female', 8, 45000, 'Delhi'),
(2, 'Rohit Verma', 'Physics', 'Male', 10, 52000, 'Mumbai'),
(3, 'Neha Gupta', 'Chemistry', 'Female', 6, 42000, 'Jaipur'),
(4, 'Amit Singh', 'Biology', 'Male', 12, 60000, 'Lucknow'),
(5, 'Pooja Mehta', 'English', 'Female', 7, 48000, 'Ahmedabad'),
(6, 'Suresh Kumar', 'History', 'Male', 15, 65000, 'Patna'),
(7, 'Kavita Joshi', 'Geography', 'Female', 5, 40000, 'Bhopal'),
(8, 'Vikas Malhotra', 'Computer Science', 'Male', 9, 55000, 'Chandigarh'),
(9, 'Sunita Rani', 'Hindi', 'Female', 11, 50000, 'Rohtak'),
(10, 'Rahul Jain', 'Economics', 'Male', 4, 38000, 'Indore'),
(11, 'Meena Kapoor', 'Political Science', 'Female', 13, 62000, 'Delhi'),
(12, 'Arun Mishra', 'Philosophy', 'Male', 14, 64000, 'Varanasi'),
(13, 'Ritika Arora', 'Psychology', 'Female', 6, 46000, 'Noida'),
(14, 'Deepak Yadav', 'Physical Education', 'Male', 8, 43000, 'Gurgaon'),
(15, 'Nidhi Saxena', 'Sociology', 'Female', 9, 47000, 'Agra'),
(16, 'Manoj Tiwari', 'Statistics', 'Male', 16, 70000, 'Prayagraj'),
(17, 'Isha Khanna', 'Computer Science', 'Female', 5, 49000, 'Pune'),
(18, 'Rajesh Patel', 'Accountancy', 'Male', 18, 75000, 'Surat'),
(19, 'Sneha Kulkarni', 'Business Studies', 'Female', 7, 51000, 'Nagpur'),
(20, 'Alok Banerjee', 'Mathematics', 'Male', 20, 80000, 'Kolkata');

select * from Teachers;


-- Creating Student table
create table Students(
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Gender VARCHAR(10),
    Age INT,
    Class VARCHAR(10),
    City VARCHAR(30),
    Marks INT
    );

insert into Students Values 
(1, 'Aarav Sharma', 'Male', 16, '10th', 'Delhi', 78),
(2, 'Ananya Verma', 'Female', 15, '9th', 'Mumbai', 85),
(3, 'Rohan Gupta', 'Male', 17, '11th', 'Jaipur', 72),
(4, 'Ishita Mehta', 'Female', 16, '10th', 'Ahmedabad', 88),
(5, 'Kunal Singh', 'Male', 18, '12th', 'Lucknow', 91),
(6, 'Priya Patel', 'Female', 17, '11th', 'Surat', 84),
(7, 'Aditya Mishra', 'Male', 16, '10th', 'Varanasi', 69),
(8, 'Neha Joshi', 'Female', 15, '9th', 'Bhopal', 76),
(9, 'Siddharth Malhotra', 'Male', 18, '12th', 'Chandigarh', 90),
(10, 'Pooja Rani', 'Female', 17, '11th', 'Rohtak', 82),

(11, 'Mohit Jain', 'Male', 16, '10th', 'Indore', 75),
(12, 'Ritika Kapoor', 'Female', 15, '9th', 'Delhi', 89),
(13, 'Aman Tiwari', 'Male', 17, '11th', 'Prayagraj', 67),
(14, 'Sneha Kulkarni', 'Female', 16, '10th', 'Nagpur', 92),
(15, 'Yash Arora', 'Male', 18, '12th', 'Noida', 86),
(16, 'Kriti Saxena', 'Female', 17, '11th', 'Agra', 79),
(17, 'Ravi Kumar', 'Male', 16, '10th', 'Patna', 71),
(18, 'Simran Kaur', 'Female', 15, '9th', 'Amritsar', 88),
(19, 'Harsh Vardhan', 'Male', 18, '12th', 'Kanpur', 83),
(20, 'Nisha Pandey', 'Female', 17, '11th', 'Gorakhpur', 77),

(21, 'Dev Patel', 'Male', 16, '10th', 'Vadodara', 81),
(22, 'Aditi Choudhary', 'Female', 15, '9th', 'Meerut', 74),
(23, 'Shubham Yadav', 'Male', 17, '11th', 'Ballia', 68),
(24, 'Tanvi Deshpande', 'Female', 16, '10th', 'Pune', 90),
(25, 'Nitin Agarwal', 'Male', 18, '12th', 'Bareilly', 65),
(26, 'Riya Sen', 'Female', 17, '11th', 'Kolkata', 87),
(27, 'Abhishek Roy', 'Male', 16, '10th', 'Howrah', 73),
(28, 'Palak Bansal', 'Female', 15, '9th', 'Panipat', 80),
(29, 'Vivek Soni', 'Male', 18, '12th', 'Udaipur', 84),
(30, 'Isha Nair', 'Female', 17, '11th', 'Kochi', 91),

(31, 'Rahul Das', 'Male', 16, '10th', 'Siliguri', 70),
(32, 'Kavya Iyer', 'Female', 15, '9th', 'Chennai', 86),
(33, 'Ankit Chauhan', 'Male', 17, '11th', 'Aligarh', 78),
(34, 'Shruti Rao', 'Female', 16, '10th', 'Bengaluru', 89),
(35, 'Saurabh Pandit', 'Male', 18, '12th', 'Haridwar', 66),
(36, 'Pallavi Ghosh', 'Female', 17, '11th', 'Durgapur', 83),
(37, 'Naveen Reddy', 'Male', 16, '10th', 'Hyderabad', 88),
(38, 'Anjali Kumari', 'Female', 15, '9th', 'Muzaffarpur', 72),
(39, 'Karan Malhotra', 'Male', 18, '12th', 'Faridabad', 90),
(40, 'Ritu Sinha', 'Female', 17, '11th', 'Ranchi', 75),

(41, 'Pranav Kulkarni', 'Male', 16, '10th', 'Kolhapur', 82),
(42, 'Sakshi Tomar', 'Female', 15, '9th', 'Gwalior', 79),
(43, 'Ayush Srivastava', 'Male', 17, '11th', 'Faizabad', 68),
(44, 'Nandini Mishra', 'Female', 16, '10th', 'Rewa', 85),
(45, 'Rakesh Singh', 'Male', 18, '12th', 'Deoria', 73),
(46, 'Bhavya Jain', 'Female', 17, '11th', 'Ujjain', 88),
(47, 'Lakshya Bhatia', 'Male', 16, '10th', 'Sonipat', 81),
(48, 'Madhuri Patil', 'Female', 15, '9th', 'Jalgaon', 76),
(49, 'Arjun Menon', 'Male', 18, '12th', 'Thrissur', 92),
(50, 'Pankhuri Dubey', 'Female', 17, '11th', 'Satna', 84);

select * from Students