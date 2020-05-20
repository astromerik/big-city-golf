


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

Pictures and video from Pixaby (Stress.png - Bellinon)
logotypes made in logomkr
Cropping the video - Clideo


<h1 align="center">
<a href="https://astromerik-big-city-golf.herokuapp.com/" target="_blank"><img src="static/images/logo.png" alt="Big city golf logo"></a>
</h1>

<div align="center">

[View this website through Heroku](https://astromerik-big-city-golf.herokuapp.com/) 
</div>


The goal of the application is:
* To make it easier for golfers in big cities to find a golf course near their location
* To create a broader experience when booking tee times, not only pick a time, but also to read more about the golf course itself.

The users goals are:
* To easily find a tee time close to a big city. 

## UX

#### Ideal users are:
* English speaking
* Golfer
* Living in/visiting Stockholm, Gothenburg or Malmo

#### Users are searching for:
* An application where they can browse golf courses in their area or big cities in Sweden
* An application where they easily can book a tee time on the golf course of their coice

#### This application make it easy for users to share and gain inspiraton because:
* It is intuitive and easy to use 
* It contains only neccesary features, thus reaching the statement above
* The application provides filter functionality which makes it easier for the user to find what they want

#### User stories 
* As a new user I want to create an account to be able to book a tee time 
* As a user I want to get a brief information of each golf course (location, price, course description)
* As a user I want to be able to view all courses in my area
* As a user I want to be able to sort golf courses on rating, green fee price
* As a user I want to see the available tee times when trying to book
* As a user I want to pay my greenfee right after booking the tee time. 
* As a returning user I want to see what tee times I have booked and cancel or reschedule them.

#### Balsamiq mockups

To see the initial wireframes for the application click <a href="" target="_blank">here</a>

## Featureas

### Navigation bar and footer 

On the top of the website we find a fixed navbar which conotains the optons "Home", "Courses, "About" and "Login/Signup". 
If the user is logged in the option "Profile" will appear which takes the logged in user to their profile page. 
If the user have a tee time in their 'shopping bag' the option "Pay greenfee" will appear on the top right.
If the user us logged in, the "Login/Signup" button is changed to "Logout". 

The footer is a mirror of the top navbar but in a simpler format. The footer do not include the login buttons, profile option or the pay greenfee button.
In the footer we also find a all rights revserved statement. 

### Home page

The home page is a clean page with little information and plenty of space between the different objects on the page. 
A welcoming video of a group of golfers is autoplaying and a short statement is presented next to it. Another button for signing up is added below the statement which is exhange for a "find tee time" button if user is logged in (which redirects the user to the courses page).
further down on the page we find some quotes why golf is good for stress releif and a short presentation about the application.
On the button of the page another golf picture with the button for searching the courses is presented. 

### Courses page/Course detail page

On the courses page the user find all the courses in the database. 
The user can choose to sort the courses based on rating, price or location. The user can also search for a golf corse by passing in text in the input field. 
For each course a picture, price and rating is presented. The user can choose to read more about the specific course or book a tee time right away. 
If the user click "read more" the user is sent to a course detail page which include more detailed information about the specific course. 
If the user click book tee tinme, a modal pops up for the specifc course and the user then need to pass in what date and time he/she want to play.
When the booking form is completed the user get redirected to the checkout page to complete their payment. 

### Pay greenfee page

The pay greenfee page (or the checkout page) is displaying the tee times the user want to book/pay for and the payment form (the information needed for passing the purchase to Stripe)
If the payment form is completed correctly the user is redirected to their profile page.


### Profile page 

On the users profile page, the user can see all the teetimes they have purchased and their profile information. 
The profile infomration is editable by using the presented form. 
For every booked tee time there is a delete tee time button. If clicked, a warning message appear which the user need to accept in order for the deletion of the tee time to be successful. 


### About page


### Database 

The database used in development mode is sqllite3 and in Heroku PostgreSQL. The database consist of the golf courses which are conected to a district.
All user profiles are conected to django alauth User model. All TeeTimes are dependent on the user profile. 
All purchases are dependent on TeeTimes. 

MAKE AN IMAGE TO INCLUDE HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



## Existing features 

* Navigation bar - Collabsable when screen size is below 993 pixels, different options depending if user is logged in or not
* Login functionality - Fully functional login and user registration process
* CRUD - Users are able to upload, read, and delete content in the database.
* Sorting - Users are able to sort through golf courses. 
* Stripe payment functionality

## Features left to implement 

* Comments - to make the application more interactive a commenting functionality would be neccesary
* A date time picker to make the choice of tee time simpler.
* Webhooks to secure the Stripe payment functionality

## Technologies used

* The website was built using HTML5 and CSS3. 
* JavaScript was used to build an interactive webpage and to connect to an API.
* Python was used to build the structure and functionality of the back end.

* [Heroku](https://www.heroku.com/) was used to deploye the live version of the application.


* The website as built and developed using [GitPod](https://www.gitpod.io/) as IDE.
* The logotype was created using [LogoMakr](https://logomakr.com).

* [W3C's HTLM Validator](https://validator.w3.org/) were used to validate the websites HTML code. 
* [W3C's CSS Validator](https://validator.w3.org/) were used to validate the websites CSS code. 
* [JSHint](https://jshint.com/) were used to validate the websites JavaScript code. 

## Testing



## Deployment

As mentioned, [GitPod](https://www.gitpod.io/) was used as IDE when developing this application. Throug out the development, the project was commited to the git and continuously pushed to GitHub and Heroku. 
The project is hosted through Heroku since Heroku can run python code. GitHub pages only supports HTML, CSS and JavaScript, thus is not suitable for this project.

#### Deploy to Heroku
The following steps were taken to deploy the application on Heroku:
1. Log in to my Heroku 
2. Click on "new" in the top right corner and choose "create new app"
3. Choose the name of the application and set "Region" to Europe. Click "Create app"
4. Go to settings and add the config vars PORT (5000) and IP (0.0.0.0)
5. Login on Heroku through the CLI in your IDE. 
6. Add the project as a master branch 
7. Push to Heroku (git push)

For Heroku to be able to run the app a Procfile and a requirements.txt must be created which is done in the IDE. 
After connected and deployed on Heroku, when pushing the workspace to Github 'git push origin master' was used. 


#### Run project locally 

If you want to clone the Github repository and run the application locally:

1. Follow the link to the main page of the repository by clicking [here](https://github.com/astromerik/milestone3)
2. Click on the option "Clone or download"
3. Copy the link of the repository by grabbing the displayed URL 
4. Open the terminal of your choice
5. Change the work directory to where you want the cloned directory to be inserted
6. type "git clone" in the terminal window followed by the previously copied URL
7. Press enter and your clone will be created.

More information can be found in Githubs documentation [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

## Credits 

### Media
* Images used in the webpage was collected from [Pixabay](https://pixabay.com).
* The logotype was created using [LogoMakr](https://logomakr.com).

### Code
* Stripe and javascript related to stripe was build with inspiration from Code Institute tutor Chris Zielinksi

### Acknowledgements
* A big thank you to my tutors at Code Institute for helping me along the way. 
* Also a big thank you to my mentor Brian Macharia for all great feedback and for taking the time to help me. 