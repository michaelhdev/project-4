# Uniattractor issue and feature tracker
----------------------

[![Build Status](https://travis-ci.org/michaelhdev/project-4.svg?branch=master)](https://travis-ci.org/michaelhdev/project-4)

# [Live Website](https://uniattractor.herokuapp.com/)
-------------
Login Details
- User privileges = user1
- Admin privileges = admin
-----------

Project aim:
----------
The Uniattractor website is an online community for those who use the Uniattractor web app. The website will provide a place for users to log bugs that they find using the Uniattractor web app. These bugs can be voted on by other users. This will help the admin to priorities bug fixes, which he/she will fix for free. Users can also comment on bugs to provide fixes and note similar issues.

The website will also provide a way for users to submit feature ideas. If other users like the feature they have the facility to donate money to have that feature developed. The admin will then be able to priorities which features he/she will develop. The admin will dedicate 50% of his/her time to the feature with the highest donation. 30% of his/her time to the feature with the second highest donation and 20% of his/her time to the feature with the third highest donation. Users will also be able to comment on features that are being developed.

The website will provide a way that users can clearly view bugs and features. It will be clearly visible what the current status of a bug or feature is and what features have the highest donations and that the admin is working on.

The website will have sublime UI aimed at attracting new users. 

## UX

The UX focus was on making an intuitive, clear and easy to use site. A mobile first approach has been taken when designing the site, ensuring that content and navigation are clear no matter what device the user is using.

The following user stories were created during the design process. 

User Stories
----------
### Guest

- A guest visits the website after using the Uniattractor web app. The goal is to have the guest sign up and to become an active community member. To this effect the website should provide a “call to action” landing page. This should display information regarding the site, useful graphs and user reviews. All designed to entice the user to sign up.

- A guest wants to register as a user -> The guest clicks on the sign up button on the home page. The guest is taken to the registration page where they can enter a username, email, and passwords. If the details are correct and no user already exists in the system with the same credentials the user account is created. The user is taken to the user dashboard. If incorrect details are entered they are displayed with an error message.


### User

- A user wants to login -> The user clicks the login button on the landing page. The user is taken to a login page where they can login. If the correct login details are entered they are taken to the user dashboard. If the incorrect details are entered they are displayed with an error message on the login page.

- A user forget his/her login detail -> The user clicks on the forgot password on the login page. The user enters his/her email address and click ‘reset’. An email with a link to reset details is sent to the users email address.

- A user wants to view current bugs -> The user selects the view bugs link on the dashboard page or menu bar. The website displays all the current bugs on the system order initially by votes. The bugs clearly display their current status, name, description and number of votes they have.

- A user wants to view bugs based on a certain criteria -> On the bug list page the user can sort by: votes, status, created by.

- A user wants to add a bug to the system -> The user clicks on the add bug button on the bug list page. The add bug page is displayed. The user enters the bug name and description and clicks add. The bug is added to the system and the user is returned to the bug list page. If incorrect details are entered an error is returned.

- A user wants to vote on a bug -> The user selects the bug they want to vote for and clicks the vote button. Their vote is added and the vote is reflected on the bug details. The user can only vote on a bug once.

- A user wants to cancel their vote -> The user selects the bug they previously voted for. In place of the vote button there is a cancel vote button. The user clicks on the cancel vote button. Their vote is cancelled and the new number of votes is reflected on the bug details

- A user wants to comment on a bug -> The user selects the bug they want to comment on. They select the view bug button. The bug details page is display. The user enters their comment in the comment box and presses the comment button. There comment is added to the page along with their name and the date. If the user presses the comment button without entering a comment and error is displayed.

- A user wants to view current features -> The user selects the view features link on the dashboard page or menu bar. The website displays all the current features on the system order initially by donations. The features clearly display their current status, name, description and total donations they have. It is clear the 3 features the admin is currently working on.

- A user wants to view features based on a certain criteria -> On the feature list page the user can sort by: donations, status, created by.

- A user wants to add a feature to the system -> The user clicks on the add feature button on the feature list page. The add feature page is displayed. The user enters the feature name and description and clicks add. The feature is added to the system and the user is returned to the feature list page. If incorrect details are entered an error is returned.

- A user wants to donate to have a feature developed -> The user selects the feature they want to donate to. They enter the amount of money they want to donate and click the donate button. A message is displayed saying their donation has been added to the cart. The user can donate to other features or checkout. 

- A user wants to checkout and pay for his/her donations -> The user clicks on the cart link in the menu bar. The user is taken to the cart page where everything in their cart is displayed along with the total cost. The user clicks the checkout button. The user is take to the payment page where the items are displayed again along with an address and payment form. The user enters his/her payment details and click pay. If the payment is successful they are returned to the feature list page with a success message. Their added donation is displayed on the feature. If incorrect details were entered and error is displayed

- A user wants to delete items from his/her basket -> The user clicks on the cart link in the menu bar. The user is taken to the cart page where everything in their cart is displayed along with the total cost. The user clicks on the delete icon beside the item they want to delete. That item is removed and the new total is displayed.

- A user wants to comment on a feature -> The user selects the feature they want to comment on. They select the view feature button. The feature details page is display. The user enters their comment in the comment box and presses the comment button. There comment is added to the page along with their name and the date. If the user presses the comment button without entering a comment and error is displayed.

- A user wants to log out -> The user clicks the logout link in the menu bar. They are return to the landing page with a log out message displayed

### Admin

- The admin wants to login and manage feature/bug status and moderate the site -> The admin writes the address to the admin login in the browser. The admin logs into the Django admin interface and from their he/she is able to moderate all the data within the system.


Wire Frame Diagrams
----------

<p align="center"><img src="static/img"/></p>
<p align="center"><img src="static/img/"/></p>
<p align="center"><img src="static/img/"/></p>
<p align="center"><img src="static/img/"/></p>

## Features

Below are a list of apps added to the project to provide the website functionality.

-   Users – This app contains all the views, models and forms to manage user login and authentication. [Users App]( https://github.com/michaelhdev/project-4/tree/master/users)
 
-   Home – This app contains the views to display the landing page of the website [Home App]( https://github.com/michaelhdev/project-4/tree/master/home)

-   Bugs – This app contains all the views, models and forms to manage bugs within the system [Bugs App]( https://github.com/michaelhdev/project-4/tree/master/bugs)

-   Features – This app contains all the views, models and forms to manage features within the system. [Feature App]( https://github.com/michaelhdev/project-4/tree/master/features)

-   Cart – This app contains all the views, models and forms to manage add items to the cart within the website. [Cart App]( https://github.com/michaelhdev/project-4/tree/master/cart)

-   Checkout – This app contains all the views, models and forms to manage payment and stripe details. [Checkout App]( https://github.com/michaelhdev/project-4/tree/master/checkout)


Interface
===============
## View

<p align="center"><img src="static/img "/></p>

Future Features
===============

If the scope of the project was to be extended the following features should be added:

1.  Live Search – live search to allow a user check if a bug or feature already exist within the website.

Database Schemas
================

This project consists of a number of tables. The schema for each is shown below:

<p align="center"><img src="static/img"/></p>

Technologies Used
=================

The technologies used for this project are listed below in no particualr order.

1. HTML5

2. CSS

3. [Materialize front-end framework v0.100.2](http://archives.materializecss.com/0.100.2/)

4.  [Python](https://www.python.org/downloads/) v3.6.8

5.  [Django]( https://www.djangoproject.com/) v1.11

6.  Pip3

7.  [Sqlite](https://www.sqlite.org/index.html) Used for development

8.  [Postgresql](https://www.postgresql.org/) Used for deployment

9. [Heroku](https://www.heroku.com/)

10. [Travis]( https://travis-ci.org/)

11. [Google fonts](https://fonts.google.com/)

12. Chrome developer tools

13. [Git/Github](https://github.com/michaelhdev/project-4)

14. AWS Cloud9

## Testing
The application was tested constantly as it was being developed. Debugging was enabled during developement and any issues or bugs were fixed.

Each app was tested using tests written in the Django test framework. This ensured all functions were acting as expected

Travis was used to ensure the project was building correctly
[Travis] (https://travis-ci.org/michaelhdev/project-4)

Test cases to ensure the application was functioning as expected were derived from the user stories. Below is the list of these test cases along with the expected results.
Errors encountered when running the test cases have been rectified

## Use Cases and expected results

### Guest tests
### A guest wants to register as a user
- The guest selects the sign up button on the landing page
- The guest is taken to the register page where he/she enters email, username, password and re-enter password. 
- If correct and unique details are entered the user is registered on the system and they are taken to the dashboard page. A success message is displayed 
- If the incorrect details are entered they remain on register page and an error message is displayed.

### User tests
### A user wants to login
- The user selects the login link on the menu bar
- The user is taken to a login page where they can enter login details. 
- If the correct login details are entered they are taken to the site dashboard page. 
- If the incorrect login details are entered they remain on the login page and an error message is displayed.

### A user forget his/her login detail
- The user selects the login link on the menu bar
- The user is taken to a login page.
- The user clicks on the ‘Forgot password’ link.
- The user is taken to the reset password page where they enter their email address and click the reset password button. 
- An email with a link is sent to their email.
- When they click the link within the email they are taken to the password reset page where they enter their new password.

### A user wants to view all current bugs.
- The user clicks on the view bugs link on the menu bar or on the dashboard page.
- A list of bugs are display sorted by date created.
- If a bug is pending it is coloured red, if it is in progress it is coloured orange and if it is complete it is coloured green
- The bug contains – bug name, create by and votes. When the drop down is selected the date added, description and number of comments are displayed.

### A user wants to view bugs based on a certain criteria.
- The user clicks on the view bugs link on the menu bar or on the dashboard page, bugs are initially sorted by date.
- The user selects ‘created by’ and selects the sort button. The bugs are returned sorted by who created them.
- The user selects ‘status’ and selects the sort button. The bugs are returned sorted by status.
- The user selects ‘date’ and selects the sort button. The bugs are returned sorted by date.

### A user wants to add a bug to the system.
- The user clicks on the add bug button on the bugs page.
- The New bug page is displayed
- The user enters a title and description and clicks save
- The user is returned to the bug details page where they can see the information they have entered. There is an option to edit the bug if they are not happy with what they have entered.
- If no title or description is entered an error message is displayed

### A user wants to edit a bug that they have entered.
-  On the bugs list page the user clicks the bug the have created and would like to edit.
- The user clicks on the view details button and the bug details page opens.
- If the user has created the bug the edit bug button will display on the bug details page.
- The user clicks on the edit bug button
- The user edits the title or description and clicks save
- The user is returned to the bug details page where they can see the information they have entered. There is an option to edit the bug again if they are not happy with what they have entered.
- If no title or description is entered an error message is displayed


### A user wants to vote on a bug
- On the bugs list page the user clicks the bug they would like to vote for.
- The user clicks on the vote up button.
- There vote is added to the system and displayed in the bug details section
- The user does not have the option to vote for the same bug twice


### A user wants to cancel their vote
- On the bugs list page the user clicks the bug they would like to cancel their vote.
- The user clicks on the cancel vote button.
- There vote is cancelled and the new vote total is displayed in the bug details section

### A user wants to comment on a bug
-  On the bugs list page the user clicks the bug they would like to comment on.
- The user clicks on the view details button and the bug details page opens.
- The user enters a comment in the comment field and clicks the comment button.


## Issues
- Give less space for votes – bugs/features with large names are extending their container. 
- Bugs don’t appear to be displaying votes in descending order initially, they appear to be assending 
- The percentages on the graph are not appearing correctly

