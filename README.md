# E-commerce-DB-Final-Project
This is the repository for my Database Fundamentals final project. Within this readme file I have included all subsequent deliverables for the project in order to meet the assignment criteria.

I created a simple e-commerce platform that stores product data, customer data, and staff data. This platform allows customers to buy products and allows staff to update products. This platform was created in Python, and uses MySQL for database management.
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

## Database Implementation Instructions



## Database Interaction



