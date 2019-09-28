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

