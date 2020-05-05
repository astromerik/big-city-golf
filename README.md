Project statement:
The application will help users in larger cities to find a golf location in their area and book the tee time of their wishes. 

User stories:
As a new user I want to create an account to be able to book a tee time 
As a user I want to get a brief information of each golf course (location, price, (maybe course guide), facilities etc.)
As a user I want to be able to view all courses in my area
As a user I want to be able to sort golf courses on rating, green fee price (and maybe availability of tee times)
As a user I want to see the available tee times when trying to book (a schedule pop up?)
As a user I want to pay my greenfee right after booking the tee time. 
As a returning user I want to see what tee times I have booked and cancel or reschedule them.

Project roadmap:
Start with setting up Django/Allauth
Create landing page and base.html
Create home/landing page
Create login functionality
Create and/or import a datafile of golf courses
Create course page - golf courses, filtering system (maybe rating functionality?)
Create booking functionality - maximum 4 people on the same time spot (10 minutes between every tee time?) including a payment placeholder
Create profile page - view current bookings, earlier bookings, able to change or delete 
Add Stripe functionality 
Add email confirmations 



Meta tag in base header (X-UA-Compatible) is to ensure compatability with older ie browsers.