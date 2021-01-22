# **Restaurant Management system**
## CBSE Project
---

# ***ACKNOWLEDGEMENT***

- *I take this opportunity to express my sincere gratitude towards smt. Parvathy E, Principal and Smt. Remya Das, Vice Principal, Bhavan’s Vidya Mandir, Eroor who gave me an opportunity to present my project.*

- *I also convey my sincere thanks to Smt. Subha Varma, my teacher for providing guidance and support for completing this project.

- *I express my gratitude to my parents, teachers and friends for their constant support  and encouragement.

- *Above all I thank the God Almighty without whose blessings this project would not have been successful.

 ---

## Index

| Sl No | Content |
|------|------|
| 1 | PROJECT ABSTRACT |
| 2 | TABLE STRUCTURE |
| 3 | SOURCE CODE |
| 4 | PROGRAM OUTPUT |
| 5 | BIBLIOGRAPHY |

---

<img align="right" width="170" height="170" src="https://i.imgur.com/oeCaInY.png"> 

> Members:  
 -  Vinayak K Raman  
 -  [Advaith Narayanan](https://twitter.com/advaithnarayan) 
 -  Meenakshi BS 
 -  M S Sudheb
 -  Suryakiran
#### This project is to create and test a Restaurant Management Program that archives the following criteria:
 1. Store `information` about the food served at the restaurant. 
 2. Provide the user with a `simple` and `easy` interface, which does not affect the `performance`, or `quality` of the service at the restaurant.
 3. A `foolproof` error prevention mechanism that does not allow the program to crash mid-operation.
 4. The use of a Database Management System to keep `logs` and track the data `essential` to the restaurant.
 5. A `secure` and `easily` accessible log of customers and their billing information.  
 
#### This is a program that makes use of a very famous, easy and powerful, high-level programming language called [**Python**](https://en.wikipedia.org/wiki/Python_(programming_language)) and, an equally powerful and versatile database management software called [**Mysql**](https://en.wikipedia.org/wiki/MySQL).  
---
> **Prerequists :**
 - [ ] Python 3.8 +
 - [ ] MySQL 5.5
 - [ ] MySQL Connector/Python 8.0
 
--- 

## Python

<details><summary><b>Modules used:</summary></b> 
 
 - mysql.connector
 - csv
 - random
 - smtplib
 - ssl
 - os
 - time
 
</details>

## MySQL 

<details><summary><b>Tables</summary></b>  

| Field | Type | Null | Key | Default | Extra |
|----------|-------------|------|-----|---------|-------|
| fno | int(3)      | NO   | PRIMARY KEY | NULL    |       |
| fname | varchar(50) | YES  |     | NULL    |       |
| type | varchar(20) | YES  |     | NULL    |       |
| price  | int(5)      | YES  |     | NULL    |       |

 </details>


---
