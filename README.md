# Website Blocker/Unblocker
#### A simple web application built with Flask and JavaScript to block or unblock websites by manipulating the hosts file.

## Overview
This project provides a user-friendly interface for blocking or unblocking websites on your system. It consists of a Flask backend for handling HTTP requests and a front-end interface built with HTML, CSS, and JavaScript.

The main features of the application include:
* Blocking websites by adding entries to the hosts file.
* Unblocking websites by removing entries from the hosts file.
* User interface for entering websites to block or unblock.
* Real-time feedback on the success or failure of blocking/unblocking operations.

## Setup
### 1.) Clone the repository:
                git clone https://github.com/Praseed35/website-blocker.git
### 2.) Run the application:Execute the following command to start the Flask server:
                python app.py
The application will be accessible at http://localhost:5000 by default.

## Usage
 ####  1.) Access the web application through your browser.
 ####  2.) Enter the websites you want to block or unblock in the respective input fields.
 ####  3.) Click the "Block Websites" or "Unblock Websites" button to perform the action.
 ####  4.) Receive real-time feedback on the success or failure of the operation.

## Configuration
##### The application manipulates the hosts file located at different paths depending on the operating system:
* ####  Windows: 'C:\Windows\System32\drivers\etc\hosts'
* ####  Linux: '/etc/hosts'
* ####  macOS: '/private/etc/hosts'
Ensure that the application has necessary permissions to read from and write to the hosts file.
