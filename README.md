<h1 align="center">
<a href="https://astromerik-big-city-golf.herokuapp.com/" target="_blank"><img src="static/media/logo.png" alt="Big city golf logo"></a>
</h1>

<div align="center">

[View this website through Heroku](https://astromerik-big-city-golf.herokuapp.com/) 
</div>

Big City Golf was built to achive a easier way to book tee times on golf courses in big cities. In Sweden, the booking system for tee times provided by the Swedish Golf Association have had a har time running propperly during the first month of 2020, thus an alternative would be welcome.
The application contains different pages depending of if the user is logged in or not. 
If the user is not logged in the site displays, a home page, a course page, a login/sign up page and an about page.
If the user is logged in a profile page and a page for booking/purchasing tee times is available.


The goal of the application is:
* To make it easier for golfers in big cities to find a golf course near their location
* To create a broader experience when booking tee times, not only pick a time, but also to read more about the golf course itself.

The users goals are:
* To easily find a tee time close to a big city. 

## UX

#### Ideal users are:
* English speaking
* Golfer
* Living in/visiting Stockholm, Gothenburg or Malmö

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

To see the initial wireframes for the application click <a href="static/media/wireframes/big-city-golf-firstdraft.pdf" target="_blank">here</a>

## Featureas

### Navigation bar and footer 

<img src="static/media/demo/demonavbar.png" alt="Demonstration navbar" style="max-height:300px;">

On the top of the website we find a fixed navbar which conotains the optons "Home", "Courses, "About" and "Login/Signup". 
If the user is logged in the option "Profile" will appear which takes the logged in user to their profile page. 
If the user have a tee time in their 'shopping bag' the option "Pay greenfee" will appear on the top right.
If the user us logged in, the "Login/Signup" button is changed to "Logout". 

The footer is a mirror of the top navbar but in a simpler format. The footer do not include the login buttons, profile option or the pay greenfee button.
In the footer we also find a all rights revserved statement. 

### Home page

<img src="static/media/demo/demohomepage.png" alt="Demonstration hompage" style="max-height:300px;">

The home page is a clean page with little information and plenty of space between the different objects on the page. 
A welcoming video of a group of golfers is autoplaying and a short statement is presented next to it. Another button for signing up is added below the statement which is exhange for a "find tee time" button if user is logged in (which redirects the user to the courses page).
further down on the page we find some quotes why golf is good for stress releif and a short presentation about the application.
On the button of the page another golf picture with the button for searching the courses is presented. 

### Courses page/Course detail page

<img src="static/media/demo/democourses.png" alt="Demonstration courses" style="max-height:300px;">

On the courses page the user find all the courses in the database. 
The user can choose to sort the courses based on rating, price or location. The user can also search for a golf corse by passing in text in the input field. 
For each course a picture, price and rating is presented. The user can choose to read more about the specific course or book a tee time right away. 
If the user click "read more" the user is sent to a course detail page which include more detailed information about the specific course. 
If the user click book tee tinme, a modal pops up for the specifc course and the user then need to pass in what date and time he/she want to play.
When the booking form is completed the user get redirected to the checkout page to complete their payment. 

### Pay greenfee page

<img src="static/media/demo/demopay.png" alt="Demonstration checkout" style="max-height:300px;">

The pay greenfee page (or the checkout page) is displaying the tee times the user want to book/pay for and the payment form (the information needed for passing the purchase to Stripe)
If the payment form is completed correctly the user is redirected to their profile page.


### Profile page 

<img src="static/media/demo/demoprofile.png" alt="Demonstration profilepage" style="max-height:300px;">

On the users profile page, the user can see all the teetimes they have purchased and their profile information. 
The profile infomration is editable by using the presented form. 
For every booked tee time there is a delete tee time button. If clicked, a warning message appear which the user need to accept in order for the deletion of the tee time to be successful. 


### About page

The about page is a simple page whit a Big city golf logo and some statements what the 'company' stands for and wish to provide. 

### Database 

<img src="static/media/demo/demodatabase.png" alt="Demonstration database" style="max-height:300px;">

The database used in development mode is sqllite3 and in Heroku PostgreSQL. 
The database has a hierarchical structure where UserProfile is dependent on User, Courses of Districts and so on.


## Existing features 

* Navigation bar - Collabsable when screen size is below 993 pixels, different options depending if user is logged in or not
* Login functionality - Fully functional login and user registration process
* CR(U)D - Users are able to upload, read and delete content in the database.
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
* Django was used as the framwork to make the development of the application more simplistic. 
* [Heroku](https://www.heroku.com/) was used to deploye the live version of the application.
* [Bootstrap](https://www.bootstrap.com/) was used as a library for design and layout.
* The website as built and developed using [GitPod](https://www.gitpod.io/) as IDE.
* The logotype was created using [LogoMakr](https://logomakr.com).
* [W3C's HTLM Validator](https://validator.w3.org/) were used to validate the websites HTML code. 
* [W3C's CSS Validator](https://validator.w3.org/) were used to validate the websites CSS code. 
* [JSHint](https://jshint.com/) were used to validate the websites JavaScript code. 

## Testing

Manual testing has been performed throughout the page with 2 errors occuring and 1 design flaw. 
When the user is deleting a teetime from the bag, the pay greenfee button remain in the header. When clicked (without items in bag) a stripe error occurs since the paygreenfee page cannot be accesed without a amount/price of the items in the bag. 
The reason for this error is because the bag is not completely cleared. 
The second error is due to a conflict in the Bootstrap CDNs which are needed for Stripe card input and the toasts (info messages for users when performing an action). The CDN for the toast requires a new version of the Bootstrap CDN whilst the stripe requires an older version. 
Due to the limited time before making the application go live, the stripe card input was prioritized, thus the application lacks toasts. 
The design flaw is regarding the sorting functionality on the course page. Users can filter on districts or sort on rating/price but the user cannot filter within a district. This will be investigated further.  

Further automated testing has been completed and circa 50 % of the code have currently beeing tested as of today. See specific app for test files.

## Deployment

As mentioned, [GitPod](https://www.gitpod.io/) was used as IDE when developing this application. Throug out the development, the project was commited to the git and continuously pushed to GitHub and Heroku. 
The project is hosted through Heroku since Heroku can run python code. GitHub pages only supports HTML, CSS and JavaScript, thus is not suitable for this project.

#### Deploy to Heroku
The following steps were taken to deploy the application on Heroku:
1. Log in to my Heroku 
2. Click on "new" in the top right corner and choose "create new app"
3. Choose the name of the application and set "Region" to Europe. Click "Create app"
4. Login on Heroku through the CLI in your IDE. 
5. Add the project as a master branch 
6. Push to Heroku (git push)

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