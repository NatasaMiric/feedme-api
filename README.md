# FeedMe API

## Deployed project and repository

The live app can be accessed at: [FeedMe API](https://feedme-api.herokuapp.com/)

Repository for the front-end application: 

## Table of Content

[Project Goals](#Project-Goals)

[Agile implementation and planing](#Agile-implementation-and-planing)

[User Stories](#User-Stories)

[Database Design](#Database-design)

[Technologies Used](#Technologies-Used)

[Testing](#Testing)

[Deployment](#Deployment)

[Acknowledgement](#Acknowledgement)

---------------------------------------------
## Project Goals

The goal for this API is to provide a backend service to allow the FeedMe front-end application to perform Create, Read, Update and Delete operations via the user interface.

## Agile implementation and planing

The project was developed using an Agile approach by defining the epics and user stories that were implemented in 5 sprints, where each lasted one week. 

I used GitHub project for planing and creating epics and user stories that were broken into tasks and each user story had assigned label according to the app that it belong to and connected to corresponding epic. MoSCoW prioritization was assigned to the each user story in order to ensure that all core features are completed first. 

I decided to have one Kanban board where will I implement issues for both api and frontend application which I considered more practical and can be accessed [here](https://github.com/users/NatasaMiric/projects/4) in order to see more details for each ticket. 

## User Stories

* Project set up 

    As a developer I want to setup my project and prepare for deployment so that I can start developing my app.

* Create the user profile API

    As a user I can create a profile so that I can store and share information about myself with other users. 

* Create the recipe API

    As a user I can store all recipes in a database so that I can retrieve, update and delete them.  

* Create the comment API  

    As a logged-in user I can store comments in the database so that I can retrieve, update and delete them.

* Create the like API

    As a user I can like a recipe so that I can show my support to the author of the recipe.

* Create bookmark API

    As a logged in user I can save/bookmark recipes so that I can store in one place all recipes that I like the most.

* Search recipes API

    As a user I can search data by author and recipe title so that I can find the recipe that interests me.

* Filter recipes API

    As a user I can filter data by category and difficulty so that I can easier find the recipe that I need.

* Filter comments API

    As a user I can retrieve all the comments associated with a given recipe so that I can easily access to all comments related to that recipe.


## Database Design

![](docs/images/erd.png)

## Technologies Used

### Languages
* HTML
* Python version 3.8.1

### Frameworks, Libraries & Programs
* Django 3.2.18 - main framework used for application creation
* Django REST Framework 3.14.0 -  used for creating API
* Django Allauth - used for authentication, registration & account management
* Django filters
* gunicorn 20.1.0 - a Python WSGI HTTP Server
* dj-database-url 0.5.0 - allows us to utilise the DATABASE_URL variable
* psycopg2-2.9.6- a postgres database adapter which allow us to connect with a postgres database.
* PostgreSQL - used as a database management system.
* Git - used for version control
* GitHub - project repository
* Heroku - used for hosting the application
* ElephantSQL - PostgreSQL database hosting service.
* Cloudinary 1.32.0 - for free image hosting
* Code Institute GitPod Full Template - Using the GitPod Full Template from the Code Institute for my project.

## Testing

### Manual testing 

* Testing The Profile App

Screenshot of manual testing are provided in comment section of the respective user story:
https://github.com/users/NatasaMiric/projects/4/views/1?pane=issue&itemId=26047295

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| Profile List | Get all profiles list as logged out and logged in user| Go to profiles page,and check if profiles are listed in logged out state, then log in | All profiles listed in both cases | Pass |
| Profile Detail View | Get profile detail view by specific id as logged in and logged out user | Go to profiles page and entered an existing id in url field in logged out state, repeated the same after logging in | The Profile Details are present | Pass |
| Get profile detail view by nonexisting id as logged in and logged out user  | not found 404 error | Go to profiles page and enter an nonexisting id in url field in logged out state, repeated the same after logging in |  The 404 error has been displayed | Pass |
| Profile Detail Update | As logged in user, user should be able to edit a profile that he owns | Go to profiles page and logg in, then entered my id in url field that redirected me to profile detail page | The update form is present on the page | Pass |
|  | Not possible to edit someone else's profile | Navigated to profiles page and logged in, entered  id from other user in url field that redirected me to profile detail page | The update form is not present on the page | Pass|
| Authorization(isOwner permission) | As logged out user is-owner field is false on all profiles listed on the page | Go to profiles page and check is_owner fields | All of them are false | Pass |
|  | As logged out user my profile detail shows is_owner false | Go to profiles page and enter a corresponding id in url to user  | As expected, is_owner field is false |Pass |
| | As logged in user is_owner field is true on the profile detail list of currently logged in user and false on the rest of the profiles | Go to profiles page and check profile list | Is_owner field is true on logged in user field and false on the rest | Pass |
|  | As logged in user, on the profile detail page of the logged-in user, is_owner is true | Go to logged in users page by adding a corresponding id to profiles url and that will redirect to profile detail page of the logged in user | is_owner field is true | Pass |
|  | As logged in user, on the profile detail page of other users, is_owner is false | Go to profiles page and add an id from other user to profiles url and that will redirect to profile detail page of the other user | is_owner field is false | Pass |


* Testing The Recipes App

Screenshot of manual testing are provided in comment section of the respective user story:
https://github.com/users/NatasaMiric/projects/4/views/1?pane=issue&itemId=26050307

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| Recipe list | If the user is logged out he should be able to see the list of all profiles | Go to recipes url | All recipes are listed | Pass |
| | If the user is logged in he should be able to see the list of all profiles| Navigated to recipes url  | All recipes are listed | Pass |
| Recipe Detail view | If the user is logged out he should be able to see the recipe details of his and other user's recipes| Navigated to recipes page and added an existing id to url of my own recipe and then repeated the same by typing id from another user  | Recipe details are present  | Pass |
|  | If the user is logged in he should be able to see the recipe details of his and other user's recipes| Navigated to recipes page and add an existing id to url by my own recipe and then repeated the same by typing id from another user | Recipe details are present  | Pass |
|  | If the user tries to fetch a recipe by nonexisting id, he should get an 404 error message  | Navigated to recipes page and added an nonexisting id to url  | The 404 error message 'not found' is shown | Pass |
| Create a recipe | If the user is logged in,he should be able to create a new recipe  | Navigated to recipes page and fill-out the form on bottom of the page then click 'post' | New recipe is created | Pass |
| Update a recipe | As logged in user and owner of the recipe,user should be able to update a recipe | Navigated to recipes page and add a specific id in url that belongs to logged in user. Got the access to recipe detail page where the form for updating is present. Updated the fields and then clicked 'put' | Taken to correct page and update form present. Recipe successfully updated. | Pass |
| Delete a recipe | As logged in user and owner of the recipe,user should be able to delete a recipe | Navigated to recipes page and add a specific id in url that belongs to logged in user. Got the access to recipe detail page where delete button is present and clicked on it| Recipe has been deleted | Pass |


* Testing Comments app

Screenshot of manual testing are provided in comment section of the respective user story:
https://github.com/users/NatasaMiric/projects/4/views/1?pane=issue&itemId=26052261

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| Comment List  | If the user is logged out or logged in,he should be able to see the list of all comments | Navigated to comments page in logged in and logged out state  | All comments are listed in both cases| Pass |
| Create comment | If the user is logged in he should be able to create a comment | Navigated to comments page and found comment form on the bottom, underneath the comments list, filled out the form and clicked 'post' | The comment has been created | Pass |
| Update comment| As logged in user and owner of the comment, user should be able to update his comment | Navigated to comments page and added a correct comment id to url to retrieve a particular comment that should be updated | Form for updating is present on the page and it is updated after changing the data and clicking on 'put' | Pass |
| Delete comment| As logged in user and owner of the comment, user should be able to delete his comment | Navigated to comments page and added a correct comment id to url to retrieve a particular comment that should be deleted | Delete button is present on the page and comment is deleted after clicking on the button | Pass |


* Testing Likes app

Screenshot of manual testing are provided in comment section of the respective user story:
https://github.com/users/NatasaMiric/projects/4/views/1?pane=issue&itemId=26052843

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| List all likes | If the user is logged out or logged in,he should be able to see the list of all likes | Navigated to likes page in logged in and logged out state  | All likes are listed in both cases | Pass |
| Like a recipe | If the user is logged in, user should be able to like a recipe | Navigated to likes page and found form on the bottom for liking a recipe, choosed recipe and clicked 'post' | The recipe has been liked | Pass|
| Unlike a recipe | If the user is logged in, user should be able to delete a like | Navigated to likes page and then added to url an id of the like that you would like to delete. This has taken me to like detail page where delete button is. Clicked on button.  | The like has been deleted | Pass |
| Handle duplicate likes | If the user tries to like the recipe that he already liked,he should get tha message about possible duplicate | Choosed the recipe that I already liked and clicked post | The message has been displayed | Pass |





## Deployment

## Acknowledgement

