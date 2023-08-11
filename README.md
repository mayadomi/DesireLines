# Desire Lines (Back End)
 
by Maya Dominice

She Codes Plus crowdfunding project - DRF Backend.

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
| POST | /users/ | Create new user | Email, password | 201 | N/A | 
| GET | /projects/ | Return all projects | N/A | 200 | N/A |
| POST | /projects/ | Create a new project | project object | 201 | User must be logged in. |
| GET | /projects/1 | Returns the project with ID of '1' (Project detail page) and all associated information and pledges | N/A | 200 | N/A |
| PUT | /projects/1 | Updates the project with ID of '1' | Project object | 200 | User must be logged in. Must be project owner.|
| POST| /pledges/ | Create a new pledge | Pledge object| 201 | User must be logged in. Must not be the owner of the project. |
| GET | /pledges/1 | Returns the pledge with ID of '1' | N/A | 200 | N/A |
| DELETE | /pledges/1 | Deletes the pledge with ID of '1' | N/A | 200 | User must be logged in. Must be pledge owner. |
| GET | /users/1 | Return user with ID of '1' | N/A | 200 | User of ID '1' must be logged in. |

A table showing what api can do; url = endpoints; authorisation/authentication --> specific user/privileges




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
