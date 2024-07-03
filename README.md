# **CEB Art**

![CEB Art image]()

## **Table of Contents**

- [**CEB Art**](#CEB Art)
  - [**Table of Contents**](#table-of-contents)
  - [**Introduction**](#introduction)
  - [**UX Development**](#ux-development)
    - [1. **Strategy Plane**](#1-strategy-plane)
    - [**User Stories**](#user-stories)
      - [**First Time User Goals**](#first-time-user-goals)
      - [**Returning User Goals**](#returning-user-goals)
      - [**Frequent User Goals**](#frequent-user-goal)
    - [**Research**](#research)
    - [**Project Goals**](#project-goals)
    - [**User Goals**](#user-goals)
    - [**Other Considerations**](#other-considerations)
    - [**Strategy Table**](#strategy-table)
    - [2. **Scope Plane**](#2-scope-plane)
    - [3. **Structure Plane**](#3-structure-plane)
    - [4. **Skeleton Plane**](#4-skeleton-plane)
    - [5. **Surface Plane**](#5-surface-plane)
      - [**Color Scheme**](#color-scheme)
      - [**Typography**](#typography)
      - [**Imagery**](#imagery)
  - [**Features**](#features)
    - [**Current Features**](#current-features)
      - [1. **Header**](#1-header)
      - [2. **Home Page**](#2-home-page)
      - [3. **Games Page**](#2-games-page)
      - [4. **Reviews Page**](#3-reviews-page)
      - [5. **Footer**](#4-footer)
    - [**Features to be added in the future**](#features-to-be-added-in-the-future)
  - [**Technologies Used**](#technologies-used)
    - [**Main Languages used**](#main-languages-used)
    - [**Additional Languages Used**](#additional-languages-used)
    - [**Frameworks, Libraries and Programs Used**](#frameworks-libraries-and-programs-used)
  - [**Issues and Bugs**](#issues-and-bugs)
  - [**Deployment**](#deployment)
    - [**Preparing my_database for deployment**](#preparing-my_database-for-deployment)
    - [**Project deployment to Heroku**](#project-deployment-to-heroku)
  - [**Testing**](#testing)
    - [**User Stories Testing**](#user-stories-testing)
      - [**First Time User Goal**](#first-time-user-goal)
      - [**Returning User Goal**](#returning-user-goal)
      - [**Frequent Visitor Goal**](#frequent-visitor-goal)
  - [**Manual Testing**](#manual-testing)
    - [**Responsiveness**](#responsiveness)
    - [**Links Testing**](#links-testing)
    - [**Forms Testing**](#forms-testing)
  - [**Autoprefixer CSS**](#autoprefixer-css)
  - [**W3C Validator Testing**](#w3c-validator-testing)
  - [**Lighthouse Testing**](#lighthouse-testing)
  - [**Further Testing**](#further-testing)
  - [**Credits**](#credits)
    - [**Code**](#code)
    - [**Images**](#images)
    - [**Additional contents**](#additional-contents)
  - [**Acknowledgements**](#acknowledgements)

## **Introduction**

CEB Art is an Art based e-commerce website with the primary purpose of marketing art portraits/pictures from a variety of genres and art media. The site will also provide a place for users to leave reviews about the website, it's products, and anything else pertinent to the site.

The main requirement of this Code Institute project was to build a Django full stack website, with the primary objective of making the website simple and easy to us. All of the site's products, orders, users and reviews will be stored in a sqlite relational database.

## **UX Development**

### 1. **Strategy Plane**

### **User Stories**

#### **First Time User Goals**

1. As a first-time user, I want to be able to navigate the website with ease via a main navigation menu and structured layout.
1. As a first-time user, I want to be able to purchase products safely and securely on the site.
2. As a first-time user, I want to know what products are listed on the site quickly and easily, being able to filter products where required.
3. As a first-time user, I want to be able to review the site's products safely and securely. 
5. As a first-time user, I want to be able to leave a review on the site if required, and see other user reviews on the site, safely and securely.
6. As a first-time user, I want to be able to locate the site's social media links to see their followings and find any future updates/products to the site.

#### **Returning User Goals**
  
1. As a returning user, I want to be able to navigate the website with ease via a main navigation menu and structured layout.
2. As a returning  user, I want to know what products are listed on the site quickly and easily, being able to filter products where required.
3. As a returning  user, I want to be able to purchase products safely and securely on the site.
4. As a returning  user, I want to be able to review the site's products safely and securely.
5. As a returning user, I want to be able to leave additional reviews on the site if required, and see other user reviews on the site, safely and securely.
6. As a returning  user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.
6. As a returning  user, I want to be able to access a history of my product purchases.

#### **Frequent User Goals**
  
1. As a frequent user, I want to be able to navigate the website with ease via a main navigation menu and structured layout.
2. As a frequent user I want safe, easy access to the site's products and reviews, as well as any additional information.
3. As a frequent user, I want to be able to leave additional reviews on the site if required, and see other user reviews on the site, safely and securely.
4. As a frequent  user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.
4. As a frequent  user, I want to be able to access a history of my product purchases.

### **Research**

- Online research

I Researched other art websites available online such as [displate](https://displate.com/) and [Artsy](https://www.artsy.net/). This helped me to understand the what is feasible, the aesthetics of other site's in this sector and how they provide a service and user accessibilty.

### **Project Goals**

The project goal is to build a full-stack Django project with relational database to create a website that allows users to store and manipulate data records about a particular domain. It should be accessible, easy to navigate, and the service provided, clear and unambiguous.

### **User Goals**

The target audience for this website is primarily Artists and Art critics, however, the site should be easily accessible for all, providing clear intent and site content.

Specifically:

- People who might be looking for information on popular Artwork in the current market.
- Anyone interested in Art.
- Anybody looking to make an Art purchase and may need guidance.
- The site can also provide a platform for Art critics to indirectly communicate with Artists.

User goals when accessing this website include gaining information about the site's products and allow users to have the ability to critic the products/artwork on offer in the current market. 

[Back to top](#CEB-Art)

### **Other Considerations**

The CB Suite is a Business-To-Customer (B2C) product, designed to sell Art products to the customer/end user. The site has considerations as below:

- Minimal, to the point content which utilises a search engine for increased accessibility to products.
- Simple design/layout/aesthetics

### **Strategy Table**

Based on the research, goals, and the considerations above, I considered what should be implemented on the website. I mapped the ideas based on their importance based on user needs and viability (given limited time and resources), to determine which ideas were going to be included and which were not:

| Features/Ideas             | Importance | Viability |
| -------------------------- |:----------:| ---------:|
|  A. Home page              |      5     |     5     |
|  B. About us page          |      5     |     5     |
|  C. Art products page      |      5     |     5     |
|  D. Art product detail page|      5     |     5     |
|  E. Product sort/filtering |      5     |     4     |
|  F. Product reviews        |      4     |     2     |
|  G. Site reviews           |      3     |     3     |
|  H. Social Media links     |      3     |     4     |
|  I. Secure payment system  |      5     |     4     |
|  J. User profile           |      4     |     3     |
|  K. User order history     |      3     |     3     |


### 2. **Scope Plane**

Based on the mapping in Strategy Plane, I decided to include these contents below in the website:

- Home page; A simple introductory layout where the user can access the site's products via a navbar a search engine or links.
- About us page; Includes any site reviews, based on previous user satisfaction, and includes a brief precis of CEB Art.
- Art products page; Displays all the products available to purchase from CEB Art.
- Product details page; Contains all the details of each Art product to the user, such as price and product description.
- Search bar; Gives a user another level of accessibilty to all the products available on the site.
- Art products filtering/sorting; Provides further accessibility, allowing the products to be sorted by price for example.
- Social media links; Will provide an external source of information about the site, or provides another avenue of communication if required by the user.
- Secure payment; A stripe payment system will be implemented to allow for fast, reliable and secure payments between the site and it's customers.
- User profile; A user profile provides an extra layer of security to the site and it's customer. 
- Order History; User history will give a customer the ability to track previous orders where necessary.
- Site reviews; Built into the About Us page, and gives the customer the abilty to leave a review if they like.

### 3. **Structure Plane**

The website's front-end framework will consist of a simple structure with a user friendly navigation element to reach each web application. Each application will also share a consistent base template utilising [Django](https://www.djangoproject.com/). The content specific to each page/child template will be controlled using Django specific extend/block content tags. The layout on child templates will also be controlled using Django, and [Python](https://www.python.org/downloads/) loop elements. An [Elephant SQL](https://www.elephantsql.com/) database will contain all Art products and review content, which the site will also display via Django and Python.

[Back to top](#CEB-Art)

### 4. **Skeleton Plane**

The initial layout and interface of the Website was created using Balsamiq Wireframes. The design/layout and feel of the site was created with UI in mind, which allows immediate interaction in first-time use, and meets the needs of the intended audience.

![Balsamiq-wireframes Blog/Home page](/media/bwhome.png)

![Balsamiq-wireframes About Us](/media/bwaboutus.png)

![Balsamiq-wireframes Products](/media/bwproducts.png)

![Balsamiq-wireframes Product details](/media/bwdetails.png)

![Balsamiq-wireframes Checkout page](/media/bwcheckout.png)

### 5. **Surface Plane**

#### **Color Scheme**

The aesthetics and framework used are primarily derived from the [Bootstrap Shop](https://startbootstrap.com/template/shop-homepage) Theme provided by [Start Bootstrap](https://startbootstrap.com/).

#### **Typography**

The fonts I used for the website were all included within the [Code Institute](https://learn.codeinstitute.net/dashboard) [Boutique Ado](https://learn.codeinstitute.net/ci_program/level5diplomainwebappdevelopment) project, which includes Lato for all text to give the site an art feel, with Roboto and Arial as fallback fonts .

#### **Imagery**

I have used an image by [Kevin Dorg](https://www.pexels.com/@kevin-dorg-136105/) named [Abstract Design Of Different Colors](https://www.pexels.com/photo/abstact-design-of-different-colors-2881262/) for the header image. A fallback color is included in the header-bg css element which will be added if the main header image doesn't load.

[Back to top](#ceb-art)

## **Features**

### **Current Features**

#### 1. **Header**

- The header occupies 100% width of the site and consists of a [main image](https://www.pexels.com/photo/abstact-design-of-different-colors-2881262/), title and search bar. The nav-bar contains a logo and three nav-links on the left that link to each site application, with user profile and shopping cart links on the right.

- The navigation bar is fully responsive on all device sizes. On desktop view, the user can see all nav-links, while on a smaller device, these collapse to a [Bootstrap Hamburger](https://getbootstrap.com/docs/5.3/components/navbar/#toggler) menu.

- The Nav-links have a subtle hover state when the user hovers over each link.

#### 2. **Home Page**

- The Home Page includes a title and sub-title to introduce the user, and a blog element to compliment the site's game theme. The template is taken from a base.html file within the CB-Suite project package, and [Routing](https://www.tutorialspoint.com/python_network_programming/python_routing.htm) is used to render each site page in the browser.

#### 3. **Games Page**

- The Games Page contains all games that the user will have the option to review, each set within a [Bootstrap card](https://getbootstrap.com/docs/5.3/components/card/#about) and housed within a [Bootstrap Carousel](https://getbootstrap.com/docs/5.3/components/carousel/#how-it-works). Information about each game is stored in a POSTGRES Database and displayed using [Flask](https://flask.palletsprojects.com/en/3.0.x/). The page template will taken from a base.html file within the project file package, and [routing](https://www.tutorialspoint.com/python_network_programming/python_routing.htm) is used to render the page in the browser. [BAFTA games awards](https://www.bafta.org/games) was used for guidance when adding game content to the site.

#### 4. **Reviews Page**

The Reviews Page displays any reviews that have been added to the site by the user. Reviews are also stored in a table in a POSTGRES database, my_suite, and displayed to the page using [Flask](https://flask.palletsprojects.com/en/3.0.x/). The page template is also taken from a base.html file within the CB-Suite file package, and [routing](https://www.tutorialspoint.com/python_network_programming/python_routing.htm) is used to render the template in the browser. A simple [star rating system](https://www.youtube.com/watch?v=0q6neX8jd44&t=69s) is included in the add_review form. [Den of Geek](https://www.denofgeek.com/games/reviews/) was used to get a general idea for the layout/aesthetics.

#### 5. **Footer**

The Footer provides social media links that all open in new tabs. The Footer also contains a copyright image with creation date using [Javascript](https://www.w3schools.com/jsref/jsref_getfullyear.asp) which will automatically update accordingly.

### **Features to be added in the future**

These features will be added where possible during further development phases:

- Adding CRUD function to the blog element, where users can leave their own content on the page for others to digest/share.

- Increasing the number of games on the site, allowing users to add their own too.

- A search feature to divide the games into groups/classes using their card info i.e. genre etc, if somebody was interested in something in particular.

- As the site grows, a generic search engine within the games/review pages navbar would be helpful to increase accessibilty.

- A function to take the average of the total number of star ratings and output an overall game review score, which could be added to the game cards.

[Back to top](#the-cb-suite)

## **Technologies Used**

### **Main Languages used**

[HTML5](https://en.wikipedia.org/wiki/HTML5) was used to create the front-end, base template of the website. A [Start Bootstrap](https://startbootstrap.com/) design theme was used for this.

[CSS3](https://en.wikipedia.org/wiki/CSS) was used to design the layout and aesthetics of the website. Again, most of the CSS was included in the [Start Bootstrap](https://startbootstrap.com/) theme file package.

[Python](https://www.python.org/) was used to create the back-end Relational Database, declaring tables used to store game/review data using Python database Models. [Routing](https://www.tutorialspoint.com/python_network_programming/python_routing.htm) was used to render each page's content based around route functions, in order to manage the structure of the website. Python also provided an __init__ and environment variable elements to the site.

### **Additional Languages Used**

[Javascript](https://en.wikipedia.org/wiki/JavaScript) controls the function of the navigation bar, and scripts are added to control the site's [date](https://www.w3schools.com/jsref/jsref_getfullyear.asp) in the footer of each page

### **Frameworks, Libraries and Programs Used**

1. [Start Bootstrap](https://startbootstrap.com/) provided the [Clean Blog](https://startbootstrap.com/theme/clean-blog) template for each site page.

2. [Bootstrap 5.3](https://getbootstrap.com/) was used to assist with the responsiveness and styling of the website, as well as adding components, such as a [card](https://getbootstrap.com/docs/5.3/components/card/) for each game, and [accordion](https://getbootstrap.com/docs/5.3/components/accordion/#how-it-works) for reviews.

3. [Flask](https://flask.palletsprojects.com/en/3.0.x/) reduced repitition when building the html/css site framework, and allowed back-end material to be injected into the front-end design.

4. [SQLAlchemy](https://www.sqlalchemy.org/) was utilised to create each table that made up the site's back-end database. SQL commands could be used to ALTER, ADD and DROP parts of the database as required, when used in conjunction with Python Models.

5. [Google Fonts](https://fonts.google.com/) provided Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif fonts for the header and titles and Lora, Times New Roman and serif fonts for the body of the site.

6. [Font Awesome](https://fontawesome.com/) was used throughout the website to add icons for aesthetic and UX purposes.

7. [Gitpod](https://gitpod.io/workspaces) IDE was used for creating the website and back end database in the terminal, and using the built in terminal to push the site to GitHub for version control.

8. [GitHub](https://github.com/) was used to store the project's code after being pushed from [Gitpod](https://gitpod.io/workspaces).

9. [Balsamiq Wireframes](https://balsamiq.com/wireframes/) were used to design the initial general layout and feel of the website.

10. [Autoprefixer CSS](https://autoprefixer.github.io/) was used to add vendor prefixes to the CSS rules, to ensure that they work across all browsers.

11. [Am I Responsive](https://ui.dev/amiresponsive?url=https://8002-coder4916-ci-milestone-ylxy4w9e48.us2.codeanyapp.com/index.html) was used to preview the website across a variety of popular devices.

12. [Squoosh](https://squoosh.app/) was used to reduce the file size of the images, and change from .jpg to .AVIF. This helped to improve the overall performance of the website.

13. [Heroku](https://www.heroku.com/home) was used to deploy the project.

[Back to top](#the-cb-suite)

## **Issues and Bugs**

- Issue: During the initial stages of the project I encountered a server error when trying to test the site.

Solution - After some tutoring, it was noticed that I had mistakenly placed my env.py file in my_suite directory instead of the root dir.

- Issue: I encountered an exe. issue when trying to test my site:

Solution - After researching what may have been the problem, making use of the information in the Slack channels, I found that my requirements.txt needed updating and syncing with my project.

- Issue: When trying to begin work on my project I found that Gitpod would not allow connection to my_database via the terminal. Tried several times to connect, and double checked project files for any obvious problems.

Solution - Slack channel suggested restarting Gitpod, but this did not fix the problem. I had to open a brand new workspace, and transfer everything over from Github. The requirements.txt and env.py files had to be recreated/updated. All imports needed re-initialisng. my_database also had to be built from scratch.

- Issue: Wrestled with the task of storing url images in my_database, and then injecting them into my project. I had first tried to add in the images and data from a JSON file, but wanted to find a much simpler solution.

Solution - I tried adding the images as urls as suggested by a tutor, and also as files to the database, but couldn't output the images from the database. After some more research (BLOBS, BYTEA etc) and getting some help from my mentor Koko, I added the urls as .Text data in my form and Model.py file. This solved the problem. I could then display the game images correctly.

- Issue: Tried to work out how to make the Bootstrap Accordion open one review at a time, rather than all, when clicking on the displayed dropdown buttons.

Solution - After a bit of research online, I found that loop.index could be utilised on the accordion buttons, giving more control over opening and closing each review.

- Issue: The list of site games would not show correctly in the select/dropdown box on my edit_review form when editing a review.

Solution - After re-writing my html code to make sure it was ok, as well as going back over the CI tutorials, I eventually found that I'd missed some code from the routes.py file, and hadn't declared the games variable properly when rendering the edit_review page. Once added, the edit_review form worked correctly.

- Issue: Creating the star rating in edit_review. Ratings were stored in the database as opposites, 1 star was 5, 5 was 1 and so on.

Solution - After some research online, I found that the values had to be written the opposite way round to reverse this. Once done, this fixed the issue.

- Issue: The main site header image in the base.html file flagged up a few problems in the terminal. When I researched this in slack, it was found that this was a problem with Gitpod not recognising the code in the IDE.

Solution - Double checked the above in slack. Tried making adjustments as per terminal instructions, did not remove the problems from terminal. Image continued to work when tested, regardless of problems raised by Gitpod.

## **Deployment**

The Website was developed using [Gitpod](https://gitpod.io/workspaces) as the IDE, committed to Git as a local repository and finally pushed/stored to [GitHub](https://github.com/). The website was then deployed to [Heroku](https://www.heroku.com/home) using the following steps:

### **Preparing my_database for deployment

1. Navigate to ElephantSQL.com and click “Log in”
2. Select “Sign in with GitHub”
3. Authorise ElephantSQL with a selected GitHub account
4. Create a new team form
5. Click “Create New Instance”
6. Select “Select Region”
7. Then click “Review”
8. Check your details are correct and then click “Create instance”
9. Return to the ElephantSQL dashboard and click on the database instance name for this project
10. In the URL section, clicking the copy icon will copy the database URL to your clipboard

### **Project deployment to Heroku**

1. Generate a requirements.txt file
2. Inside the root directory of your project, create a Procfile
3. Inside the file, add the following command: python3 run.py
4. Open your __init__.py file
5. Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, DATABASE_URL.
6. To ensure that SQLAlchemy can read an external database, its URL should start with “postgresql://”, changes should not be made to this in the environment variable. Instead, make an addition to the else statement from the previous step to adjust the DATABASE_URL in case it starts with postgres://:
7. Save all files and then add, commit and push changes to GitHub
8. Log into Heroku.com and click “New” and then “Create a new app”
9. Choose a unique name for the app, select a region and click “Create app”
10. Go to the Settings tab of your new app
11. Click Reveal Config Vars
12. Return to your ElephantSQL tab and copy your database URL
13. Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”
14. Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var.
15. Navigate to the “Deploy” tab of your app
16. In the Deployment method section, select “Connect to GitHub”

[Back to top](#the-cb-suite)

## **Testing**

### **User Stories Testing**

#### **First Time User Goal**

1. As a first-time user, I want to be able to navigate the website with ease.

- The navigation bar is clearly defined, with a subtle hover function when the user moves the cursor over the menu items.
- The title in the navbar leads the user back to the Home page increasing accessibility.
- Links to further information/social media can be easily accessed via the footer.

![Navigation Bar Screenshot](/my_suite/static/img/navbar.png)

2. As a first-time user, I want to know what type of games are listed on the site as required.

- Visitors to the site are greeted with a Home page that contains an introductory game blog; and navbar allows the user access straight to the games page. All games are displayed in a card, with a button to review for each game. A Bootstrap Carousel was initially used both in the design phase, and in initial development, however this was removed as it was slowing access to all games. This was considered to have added some frustration to UX when displaying/reviewing the site's games.

![Game Page Screenshot](/my_suite/static/img/games_page.png)

3. As a first-time user, I want to be able to review the site's games quickly and easily 

- A user can navigate easily to the games page via the navigation bar. All games are displayed in a card, with a button to review for each game.

![An example of a game card](/my_suite/static/img/game_card.png)

4. As a first-time user, I want to be able to see my review on the site, and be able to edit if needed.

- A reviews page holds all submitted reviews, and displays all reviews in a Bootstrap Accordion. The page is easily accessed via the navigation bar. Each review has an editing option available.

![Reviews page and reviews accordion](/my_suite/static/img/reviews_page.png)

5. As a first-time user, I want to be able to see other user reviews on the site.

- Other user reviews can be accessed via the reviews page, in the reviews accordion.

![Reviews accordion; unopened](/my_suite/static/img/reviews_accordion.png)

6. As a first-time user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.

- Social media links are stored in the footer.

![Links](/my_suite/static/img/footer_links.png)

#### **Returning User Goal**

1. (Refer to first time user goals)

#### **Frequent Visitor Goal**

1. As above.

## **Manual Testing**

### **Responsiveness**

I used web developer tools extensively throughout the project to update and correct code, adjust website aesthetics, and check/improve and confirm responsiveness accross all devices, using a Bootstrap 'Mobile First' approach.

Below are some examples of areas of the site that I have tested and checked for full responsiveness on all devices. These images show the sections at each [Breakpoint](https://getbootstrap.com/docs/5.3/layout/breakpoints/#core-concepts).

![Header-sm](/my_suite/static/img/header-sm.png)

![Header-md](/my_suite/static/img/header-md.png)

![Header-lg](/my_suite/static/img/header-lg.png)

![Header-xlg](/my_suite/static/img/header-xlg.png)

![games-sm](/my_suite/static/img/games-sm.png)

![games-md](/my_suite/static/img/games-md.png)

![games-lg](/my_suite/static/img/games-lg.png)

![games-xlg](/my_suite/static/img/games-xlg.png)

### **Links Testing**

Once deployed, the website links were tested to ensure that:

- All navigation external/internal links are working correctly, and filepaths are correct.
- The social media links are working and opening in a new tab.
- Hovering and Active states are working.

### **Forms Testing**

The CB Suite edit and add_review forms were tested to make sure that the required fields are working, and that the create and update and the form POSTs any input data correctly to the site. I have also included an image of the games added to the database using forms.

![Example of form data successfully posted to my_database](/my_suite/static/img/mydatabase-review.png)

![Example of form data successfully posted to my_database](/my_suite/static/img/mydatabase-game.png)

## **Autoprefixer CSS**

Autoprefixer CSS was used to add CSS vendor prefixes to the CSS rules after the developing process was completed.

## **W3C Validator Testing**

The following image shows the CSS code placed into the W3C validator testing app to check for any incorrect code. There were no errors or warnings to show:

![CSS checked](/my_suite/static/img/cssw3c.png)

## **Lighthouse Testing**

Chrome Lighthouse testing was used to check the performance, accessibility, best practices, and SEO. After applying some changes to make the performance faster, including compression and resizing of images, the results below were achieved:

- Desktop:

![The CB Suite Lighthouse testing](/my_suite/static/img/desktop-lh.png)

- Mobile:

![The CB Suite Lighthouse testing](/my_suite/static/img/mobile-lh.png)

## **Further Testing**

The Website was tested on Google Chrome, Microsoft Edge and Mozilla Firefox.

The website was viewed on a variety of devices such as:

Windows Laptop
Mobile: Samsung Galaxy S12
Web developer tools devices

Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## **Credits**

### **Code**

1. The [Code Institute Walkthrough project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DIWADRDB+2022_Q3/courseware/c0c31790fcf540539fd2bd3678b12406/6e44128b0b37416ab40c1a87ef2cb32a/) was used extensively to guide me through the creation of my site, through to project completion.

2. [Bootstrap 5.3](https://getbootstrap.com/): Bootstrap was used extensively throughout the project, including the use of the following components:

- [Cards for each game](https://getbootstrap.com/docs/5.3/components/card/#about)
- [Bootstrap grid system](https://getbootstrap.com/docs/5.3/layout/grid/#example)
- [A Bootstrap Accordion](https://getbootstrap.com/docs/5.3/components/accordion/#how-it-works)

3. [Stackoverflow](https://try.stackoverflow.co/explore-teams?utm_source=adwords&utm_medium=ppc&utm_campaign=kb_teams_search_brand_emea-dach&_bt=657236278306&_bk=stack+overflow&_bm=p&_bn=g&gad_source=1&gclid=Cj0KCQjwk6SwBhDPARIsAJ59GwcGy0TWHr4Xg0bldUwSZjn60NaaP0w7oL_qF8TbqwyaGXH6KOPf-jkaAk0jEALw_wcB) was used to find solutions to problems/issues when building the website, for example, finding out [more information](https://stackoverflow.com/questions/69673044/why-my-rating-is-going-reverse-direction) when trying to create a star rating system in the add_review page. 

4. [W3Schools](https://www.w3schools.com/) was used to get assitance with postgreSQL statements when manipulating data/tables in my_database.

5. [PostgreSQL Tutorial](https://www.postgresqltutorial.com/) was also used to get help with different statements/commands when trying to manipulate my_database. This included deleting the entire database, deleting and adding columns, and altering the data in a column.

6. [Autoprefixer CSS](https://autoprefixer.github.io/): was used to add different vendor prefixer to CSS.

7. [W3C Validator Testing](https://validator.w3.org/nu/#textarea) was used to check for any errors in my CSS code.

8. [Youtube tutorials](https://www.youtube.com/watch?v=0q6neX8jd44&t=69s) were used to help create certain aspects of the site, including a simple star rating system.

### **Images**

I used this [image](https://www.pexels.com/photo/set-of-modern-gadgets-on-table-5861322/) by [Athena](https://www.pexels.com/@athena/), which was sourced from Pexels for the header of each site page.

The following images I sourced from various sites to use for my game cards:

[Etsy image](https://www.etsy.com/uk/listing/1514733901/super-mario-wonder-poster-2?gpla=1&gao=1&&utm_source=google&utm_medium=cpc&utm_campaign=shopping_uk_en_gb_c-art_and_collectibles-prints-digital_prints&utm_custom1=_k_Cj0KCQjwqpSwBhClARIsADlZ_TlySr5JO1I4H-_Px_v7eXiz3FL1ViaL9xbqCVQTXdpjAz4fMwt3Gf0aAi6zEALw_wcB_k_&utm_content=go_12604170148_121488004522_508814058911_pla-328046931108_c__1514733901engb_102858184&utm_custom2=12604170148&gad_source=1&gclid=Cj0KCQjwqpSwBhClARIsADlZ_TlySr5JO1I4H-_Px_v7eXiz3FL1ViaL9xbqCVQTXdpjAz4fMwt3Gf0aAi6zEALw_wcB); used for the Super Mario game card.

[CD keys images](https://www.cdkeys.com/star-wars-jedi-survivor-pc-origin?__currency=gbp&gad_source=1&irclickid=xXpWqtXYmxyPUR9RiQWj01vfUkHUPSSG51yfS40&utm_source=impact&utm_medium=affiliate&utm_campaign=razorcreations&irgwc=1); used for Star Wars, Streetfighter and Resident Evil game cards.

[Gaming deals images](https://www.gamingdeals.com/games/marvels-spider-man-2/?edition=Standard+Edition&platform=PS5&track=css_pages&utm_source=google&utm_medium=css_pages&utm_campaign=comparison&gad_source=1&gclid=Cj0KCQjwqpSwBhClARIsADlZ_Tl9-y7izhY2hj-AO04YcCnGJiaPeoh_k28g17EuIXg1xbKJn6BqVn8aAsdYEALw_wcB); used for the Spider Man and Final Fantasy cards.

[Infinite Bargains image](https://infinite-bargains.co.uk/products/harry-potter-hogwarts-legacy-maxi-poster-print-61x91-5cm?variant=47551905530169&currency=GBP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gad_source=1&gclid=Cj0KCQjwqpSwBhClARIsADlZ_TlDyj48hEt7DcIKLn8ePMIZfBlXjEhMhom8Q0CERBJG1laTeqYqtAYaAhQQEALw_wcB); used for the Hogwarts game card.

All other game card images were sourced from [Wikipedia](https://en.wikipedia.org/wiki/Alan_Wake_2).

### **Additional contents**

The external links included in the blog page include [The Gamer](https://www.thegamer.com/best-pc-exploration-games/#avatar-frontiers-of-pandora), [nature](https://www.nature.com/articles/d41586-023-00065-6), and [philoso?hy Talk](https://www.philosophytalk.org/blog/game-or-not-game)

## **Acknowledgements**

- My mentor, Oluwaseun Owonikoko, for her guidance and helpful feedback on all aspects of the Website.
- The Code Institute tutors who helped me with some of the issues I had when building the site.
- My wife Beth for her constant support throughout, and for proof reading and testing my site material.

[Back to top](#the-cb-suite)