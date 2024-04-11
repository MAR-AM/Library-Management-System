# Library-Management-System
<img src="User-Authentication.png">

-->  Library Management System - User Authentication

This Python script implements a user authentication system for a Library Management System using Tkinter for the GUI. It allows users to log in, register as a new user, and reset their password if forgotten. The script connects to a MySQL database to perform user authentication and password management tasks. Users can log in with their username and password, and if the credentials are correct, they gain access to the library system. If the user forgets their password, they can reset it by providing their contact number and setting a new password. The application provides appropriate error messages for invalid input and ensures data integrity by validating user inputs before performing database operations.

<img src="New-Register.png">

--> Library Management System - User Registration

This Python script enables user registration functionality for a Library Management System using Tkinter for the GUI. Users can register by providing their personal information such as first name, last name, contact number, email, and password. The script validates user input to ensure all required fields are filled, passwords match, and users agree to the terms and conditions. It also checks if the user already exists in the database before registering. Upon successful registration, the user is welcomed to the MAR-AM BOOK STORE with a success message. Users can also navigate to the login page using the "Login Now" button. The script connects to a MySQL database to store user registration information securely.


<img src="forget-password.png">

--> Library Management System - Password Reset Interface 

The `forget_psw` function is a part of a graphical user interface (GUI) designed for password reset functionality in a registration system. It prompts the user to enter their email address. If the email address is provided, it queries a database to check if the email exists. If it does, the interface allows the user to reset their password by providing a new password and confirming it. The user interface includes input fields for the contact number, new password, and confirmation of the new password. Additionally, it features a button to trigger the password update process. This function provides a simple yet effective means for users to reset their passwords securely.
