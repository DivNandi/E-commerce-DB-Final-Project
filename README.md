# E-commerce-DB-Final-Project
This is the repository for my Database Fundamentals final project. Within this readme file I have included all subsequent deliverables for the project in order to meet the assignment criteria.

I created a simple e-commerce platform that stores product data, customer data, and staff data. This platform allows staff to update products, and allows staff to update customer information. This platform is designed for a giant warehouse firm, so there is no direct customer input. This platform was created in Python, and uses MySQL as a backend for database management.
## Requirements Gathering 
Below are the use cases created for this specific project, and the subsequent data requirement created by the Use Case.
| Use Cases | Data Requirements |
| ----------- | ----------- |
| User must be able to purchase item | Must include relationship between Customer and Product entities |
| User must be able to supply relevant information so product can be shipped to them | Must include relevant attributes |
| Product must be able to be updated by Designated User(Staff) | Relationship must exist between product entity and staff entity |
| User must be able to supply multiple credit cards | Credit Cards must have a weak relationship to Customer |
| User expects data to be accurately stored | Data integrity must be maintained throughout the system |

## Entity Relationship Diagram
<img width="1802" height="775" alt="image" src="https://github.com/user-attachments/assets/9aa27039-9f2d-4447-93a4-1335aa452641" />
Assumption made: Customers can only have one email, as this will be the email they sign in with. Purchase should also include an attribute called "QuantitiesPurchased" 

## Schema Design
Customer(*CustomerID*, First Name, Last Name, Email, StreetAddress, City, State, ZipCode)

CreditCard(*CardNum*, CustomerID, SecurityCode, Expdate)

Purchase(*OrderNumber, ProductID*, CustomerID, DatePurchased, QuantitiesPurchased)

Product(*ProductID*, Name, Quantity, Price)

Updates(*UID*, ProductID, StaffID, Date)

Staff(*StaffID*, Name, Position)

## Database Implementation
Within my Repository is the links to my database creation statements and my database data insertion statements.

Database Creation: https://github.com/DivNandi/E-commerce-DB-Final-Project/blob/main/online-store/schema.sql 
Database Insertion: https://github.com/DivNandi/E-commerce-DB-Final-Project/blob/main/online-store/sample_data.sql

## Database Interaction
Within my Repository is also links to the example SQL queries required for the project: https://github.com/DivNandi/E-commerce-DB-Final-Project/blob/main/online-store/queries.sql

Lastly, here is a link to my database demonstration video: https://drive.google.com/file/d/1-sW31QhZq55ZFLTNnVVa0isEFSmhesHe/view?usp=sharing 


