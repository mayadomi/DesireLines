# Desire Lines (Back End)
 
by Maya Dominice

She Codes Plus crowdfunding project - DRF Backend.

## Submission Content for Part A - DRF 

[ ] A link to the deployed project.
The project is deployed at this URL: https://desirelines-backend.fly.dev/projects/

[ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.

  <img src="./readme_images/insomnia_get_projects.PNG" alt="get_projects" width="300">

[ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.

  <img src="./readme_images/insomnia_create_new_user.PNG" alt="create user" width="300">

[ ] A screenshot of Insomnia, demonstrating a token being returned.

  <img src="./readme_images/insomnia_get_token.PNG" alt="generate token" width="300">

[ ] Step by step instructions for how to register a new user and create a newproject (i.e. endpoints and body data).


[ ] Your refined API specification and Database Schema.

### API Specification

| HTTP Method | Url | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization
| --- | ------- | ------ | -- | -----| ----|
| GET | /projects/ | Return all projects | N/A | 200 | N/A |
| GET | /projects/1 | Returns the project with ID of '1' (Project detail page) and all associated information and pledges | N/A | 200 | N/A |
| GET | /pledges/ | Returns all pledges | N/A | 200 | N/A |
| GET | /pledges/1 | Returns the pledge with ID of '1' | N/A | 200 | N/A |
| GET | /users/ | Return all users| N/A | 200 | User logged in must be admin user. *permissions not implemented yet... |
| GET | /users/1 | Return user with ID of '1' | N/A | 200 | User of ID '1' must be logged in. *permissions not implemented yet... |
| POST | /users/ | Create new user | Example request body: <br />{<br />"username":"User2",<br /> "email":"emailaddress", <br />"password":"yourpassword"<br />} | 201 | N/A |
| POST | /projects/ | Create a new project | Example request body: <br /> {<br />"title":"Project1",<br />"description":"An example project",<br />"goal":5,<br />"image":"https://exampleimage.jpg",<br />"is_open":true,<br />"date_created": "2023-08-12T00:00:00Z",<br />"location_desc":"Brisbane",<br />"location_x":27.4705,<br />"location_y":153.0260<br /> } | 201 | User must be logged in/authorized (via token). |
| POST| /pledges/ | Create a new pledge | Example request body: <br /> {<br />"amount":8,<br />"comment":"This is another pledge",<br />"anonymous":false,<br />"project":2<br />} | 201 | User must be logged in/authorized (via token). |
| PUT | /projects/1 | Updates the project with ID of '1' | Example request body:  <br /> {<br />"id":1<br />"title":"Project1",<br />"description":"An example project",<br />"goal":5,<br />"image":"https://exampleimage.jpg",<br />"is_open":true,<br />"date_created": "2023-08-12T00:00:00Z",<br />"location_desc":"Brisbane",<br />"location_x":27.4705,<br />"location_y":153.0260<br /> }| 201 | User must be logged in/authorized (via token). Must be project owner.|
| PUT | /pledges/1 | Updates the pledge with ID of '1' | Example request body:<br /> {<br />"id":1,<br />"amount":8,<br />"comment":"This is another pledge",<br />"anonymous":false,<br />"project":2<br />} | 201 | User must be logged in. Must be pledge creator/supporter.|


### Database Schema
  <img src="./readme_images/database_erd.png" alt="database erd" width="300">




## About
Deriving from the urban planning paradigm of the unplanned links forged by people following the path they desire, not the path planned for them, this 
crowdfunding platform is aimed at providing agency and empowerment to local communities to tackle urban design issues in their neighbourhoods.

Design of and safe mobility through spaces that people inhabit are vital to human health and wellbeing,
and often those who live in the area know what's needed best where: one only needs to look for the desire lines already there.

Examples of projects could include community verge gardens, little public libraries, parklets, natural playground equipment, benches/tables or other seating amenities,
lighting, artwork pieces, connective pathways, vehicle traffic slowing devices and many more. 

## Features
{{ The features your MVP will include. (Remebber this is a working document, you can change these as you go!) }}
* [ ] Create an account
* [ ] Login/Logout
* [ ] Create a project
* [ ] Geo-locate (auto-populate address field) and get XY coordinates
* [ ] Project owner privileges:
  * [ ] Update status of a project (open/closed)
* [ ] User privileges (logged in)
  * [ ] Create a project
  * [ ] Donate/pledge to an existing project
  * [ ] Donate/pledge to one's own project
* [ ] Pledges non-editable (ie can't withdraw or edit pledge once submitted)
* [ ] View user profile (if user logged in)
    * [ ] List user's projects
    * [ ] List user's pledges
* [ ] View project details (no login required)
* [ ] View map of projects using XY coordinates (no login required)
* [ ] View list projects with highest pledges/closest to completion (no login required)


### Stretch Goals
{{ Outline three features that will be your stretch goals if you finish your MVP }}
* [ ] Password reset for user
* [ ] Edit certain account details for logged in user
* [ ] Bookmark/watch projects for logged in user
* [ ] Search for projects (no login required)
* [ ] Email out to pledgers when complete/send updates (for logged in project owner)
* [ ] Vote on projects (anonymously - to see which projects community really wants)
  * [ ] Method to control how/amount of votes (ie to avoid being susceptible to a bot/dos attack....) 
  * [ ] List of projects with highest votes
* [ ] Create project through map - get x,y from map to auto-populate location fields
* [ ] OAuth2 authentication
* [ ] Geo-magic to connect locations as a line
* [ ] Pedshed visual from project locations (similar to what Google is now starting to roll-out as 'x-minute walk' blobs from a point)

## API Specification

| HTTP Method | Url | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization
| --- | ------- | ------ | -- | -----| ----|
| GET | /projects/ | Return all projects | N/A | 200 | N/A |
| GET | /projects/1 | Returns the project with ID of '1' (Project detail page) and all associated information and pledges | N/A | 200 | N/A |
| GET | /pledges/ | Returns all pledges | N/A | 200 | N/A |
| GET | /pledges/1 | Returns the pledge with ID of '1' | N/A | 200 | N/A |
| GET | /users/ | Return all users| N/A | 200 | User logged in must be admin user. *permissions not implemented yet... |
| GET | /users/1 | Return user with ID of '1' | N/A | 200 | User of ID '1' must be logged in. *permissions not implemented yet... |
| POST | /users/ | Create new user | Example request body: <br />{<br />"username":"User2",<br /> "email":"emailaddress", <br />"password":"yourpassword"<br />} | 201 | N/A |
| POST | /projects/ | Create a new project | Example request body: <br /> {<br />"title":"Project1",<br />"description":"An example project",<br />"goal":5,<br />"image":"https://exampleimage.jpg",<br />"is_open":true,<br />"date_created": "2023-08-12T00:00:00Z",<br />"location_desc":"Brisbane",<br />"location_x":27.4705,<br />"location_y":153.0260<br /> } | 201 | User must be logged in/authorized (via token). |
| POST| /pledges/ | Create a new pledge | Example request body: <br /> {<br />"amount":8,<br />"comment":"This is another pledge",<br />"anonymous":false,<br />"project":2<br />} | 201 | User must be logged in/authorized (via token). |
| PUT | /projects/1 | Updates the project with ID of '1' | Example request body:  <br /> {<br />"id":1<br />"title":"Project1",<br />"description":"An example project",<br />"goal":5,<br />"image":"https://exampleimage.jpg",<br />"is_open":true,<br />"date_created": "2023-08-12T00:00:00Z",<br />"location_desc":"Brisbane",<br />"location_x":27.4705,<br />"location_y":153.0260<br /> }| 201 | User must be logged in/authorized (via token). Must be project owner.|
| PUT | /pledges/1 | Updates the pledge with ID of '1' | Example request body:<br /> {<br />"id":1,<br />"amount":8,<br />"comment":"This is another pledge",<br />"anonymous":false,<br />"project":2<br />} | 201 | User must be logged in. Must be pledge creator/supporter.|


## Database Schema
{{ Insert your database schema }}

![image info goes here](./docs/image.png)

## Wireframes
{{ Insert your wireframes }}

<img src="./readme_images/homepage.png" alt="test" width="300">

<img src="./readme_images/ExplorePage.png" alt="test" width="300">

<img src="./readme_images/ProjectCreationPage.png" alt="test" width="300">
    
<img src="./readme_images/ProjectEditingPage.png" alt="test" width="300">
    
<img src="./readme_images/ProjectDetailPage.png" alt="test" width="300">

<img src="./readme_images/PledgeCreation.png" alt="test" width="300">

<img src="./readme_images/PledgeDeletion.png" alt="test" width="300">
    
<img src="./readme_images/SignUpLoginPages.png" alt="test" width="300">
   
<img src="./readme_images/UserAccountView.png" alt="test" width="300">


## Colour Scheme
{{ Insert your colour scheme }}

![image info goes here](./docs/image.png)

## Fonts
{{ outline your heading & body font(s) }}
----> stop here ---> Saturday

## Submission Documentation
{{ Fill this section out for submission }}

Deployed Project: [Deployed website](http://linkhere.com/)

### How To Run
{{ What steps to take to run this code }}

### Updated Database Schema
{{ Updated schema }}

![image info goes here](./docs/image.png)

### Updated Wireframes
{{  Updated wireframes }}

![image info goes here](./docs/image.png)

### How To Register a New User
{{ Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data). }}

### Screenshots
* [] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a token being returned.
![image info goes here](./docs/image.png)
