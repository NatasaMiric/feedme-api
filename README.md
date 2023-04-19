# FeedMe API

## Deployed project and repository

The live app can be accessed at:

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

The project was developed using an agile approach by defining the epics and user stories that were implemented in 5 sprints, where each lasted one week. 

I used GitHub project for planing and creating epics and user stories that were broken into tasks and each user story had assigned label according to the app that it belong to and connected to corresponding epic. MoSCoW prioritization was assigned to the each user story in order to ensure that all core features are completed first. 

I decided to have one Kanban board where will I implement issues for both api and frontend application which I considered more practical and can be accessed [here](https://github.com/users/NatasaMiric/projects/4) in order to see more details for each ticket. 

## User Stories

* Project set up

    As a developer I want to setup my project and deploy so that I can start developing my app.

* Create the user profile API

    As a user I can create a profile so that I can store and share information about myself with other users. 

* Create the recipe API

    As a user I can store all recipes in a database so that I can manage them.  

* Create the comment API  

    As a logged-in user I can add comments to a recipe so that I can share my thoughts about the recipe.

* Create the like API

    As a user I can like a recipe so that I can show my support to the author of the recipe.

## Database Design

![](docs/images/erd.png)

## Technologies Used

* HTML
* Python version 3.8.1
* Django 3.2.18 - main framework used for application creation
* Django REST Framework 3.14.0 -  used for creating API
* Django Allauth - used for authentication, registration & account management
* Pillow 8.2.0
* Git - used for version control
* GitHub - project repository
* Heroku - used for hosting the application
* ElephantSQL - PostgreSQL database hosting service.
* Cloudinary 1.32.0 - for free image hosting
* Code Institute GitPod Full Template - Using the GitPod Full Template from the Code Institute for my project.

## Testing

## Deployment

## Acknowledgement

