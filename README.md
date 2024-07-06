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
2. As a first-time user, I want to be able to purchase products safely and securely on the site.
3. As a first-time user, I want to know what products are listed on the site quickly and easily, being able to filter products where required.
4. As a first-time user, I want to be able to review the site's products safely and securely. 
5. As a first-time user, I want to be able to leave a review on the site if required, and see other user reviews on the site, safely and securely.
6. As a first-time user, I want to be able to locate the site's social media links to see their followings and find any future updates/products to the site.

#### **Returning User Goals**
  
1. As a returning user, I want to be able to navigate the website with ease via a main navigation menu and structured layout.
2. As a returning  user, I want to know what products are listed on the site quickly and easily, being able to filter products where required.
3. As a returning  user, I want to be able to purchase products safely and securely on the site.
4. As a returning  user, I want to be able to review the site's products safely and securely.
5. As a returning user, I want to be able to leave additional reviews on the site if required, and see other user reviews on the site, safely and securely.
6. As a returning  user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.
7. As a returning  user, I want to be able to access a history of my product purchases.

#### **Frequent User Goals**
  
1. As a frequent user, I want to be able to navigate the website with ease via a main navigation menu and structured layout.
2. As a frequent user I want safe, easy access to the site's products and reviews, as well as any additional information.
3. As a frequent user, I want to be able to leave additional reviews on the site if required, and see other user reviews on the site, safely and securely.
4. As a frequent  user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.
5. As a frequent  user, I want to be able to access a history of my product purchases.

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

![Balsamiq-wireframes Shopping Cart](/media/bwshopcart.png)

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

- The Home Page includes a title and sub-title, which is linked to the products page. The template is taken from a base.html file, and [Django](https://docs.djangoproject.com/en/5.0/ref/templates/language/) is used to render each site page.

#### 3. **Products Page**

- The Products page contains all Artwork that the user will have the option to purchase, each set within a [Bootstrap card](https://getbootstrap.com/docs/5.3/components/card/#about). Information about each product is stored in an [Elephant SQL](https://www.elephantsql.com/) database and displayed using [Django](https://docs.djangoproject.com/en/5.0/ref/templates/language/). The page template is taken from a base.html file within the project file package, and [Python/Django](https://docs.djangoproject.com/en/5.0/ref/templates/language/) is used to render the page in the browser.

#### 4. **About Us Page**

The About Us page displays any reviews that have been added to the site by the user. Reviews are also stored in a table in an [Elephant SQL](https://www.elephantsql.com/) database, and displayed to the page using [Python/Django](https://docs.djangoproject.com/en/5.0/ref/templates/language/). The page template is also taken from a base.html file within the CEB Art package, and [Python/Django](https://docs.djangoproject.com/en/5.0/ref/templates/language/) is used to render the template in the browser.

#### 5. **Product Details**

The Product Details page displays all details of each product, including an image of the product and it's price. There is a button to add all products selected by the user, to the Checkout Page.

#### 6. **Shopping Cart Page**

The Shopping Cart page stores all the selected products and displays the individual products, delivery and total cost of anything added into the cart. There's a submit button to submit an order, and redirects the customer to a Checkout Page.

#### 7. **Checkout Page**

The Checkout Page displays the products that were selected and placed in the shopping cart as well as total cost. It contains a form that will hold the customers details, and a link and input, which is connected to the [Stripe](https://docs.stripe.com/development) online payment system.

#### 8. **User Profile Admin**

The built in Django Admin application provides a user profile functionality where a customer can create a user account for browsing and purchasing products securely. A superuser function allows site administrators to update the website if required.

#### 9. **Footer**

The Footer provides social media links that all open in new tabs. The Footer also contains a copyright image with creation date using [Javascript](https://www.w3schools.com/jsref/jsref_getfullyear.asp) which will automatically update annually.

### **Features to be added in the future**

These features will be added where possible during further development phases:

- Increasing the number of products on the site.

- A function to take the average of the total number of star ratings by user reviews and output an overall Art review score, which could be added to the Artwork details page.

[Back to top](#ceb-art)

## **Technologies Used**

### **Main Languages used**

[HTML5](https://www.w3schools.com/html/html_intro.asp) was used to create the front-end framework and base templates of the website. A [Start Bootstrap](https://startbootstrap.com/) design theme was used for this.

[CSS3](https://www.w3schools.com/css/) was used to design the layout and aesthetics of the website. 

[Javascript](https://en.wikipedia.org/wiki/JavaScript) controls the function of the navigation bar, and scripts are added to control the site's [date](https://www.w3schools.com/jsref/jsref_getfullyear.asp) in the footer of each page, as well as colors on the profiles app fields. [JSON](https://en.wikipedia.org/wiki/JSON) was utilised for storing the products/objects which were also loaded to the project database. Javascript also handles elements of the Stripe payment system.

[Python](https://www.python.org/) was used to create the website's applications, including functionality, and render the templates to the frontend framework.

### **Frameworks, Libraries and Programs Used**

1. [Start Bootstrap](https://startbootstrap.com/) provided the [shop style](https://startbootstrap.com/theme/clean-blog) template for each site page.

2. [Bootstrap 5.3](https://getbootstrap.com/) was used to assist with the responsiveness and styling/structure of the website, as well as adding components, such as a [card](https://getbootstrap.com/docs/5.3/components/card/) for each product and for the site reviews.

3. [Django](https://docs.djangoproject.com/en/5.0/ref/templates/language/) reduced repitition when building the html/css site framework, and allowed back-end material to be projected onto the front-end. Also provided a built-in administration application.

4. [Font Awesome](https://fontawesome.com/) was used throughout the website to add icons for aesthetic and UX purposes.

5. [Gitpod](https://gitpod.io/workspaces) and Gitpod Enterprise IDE was used for creating the website and back end database in the terminal, and using the built in terminal to push the site to GitHub for version control.

6. [GitHub](https://github.com/) was used to store the project's code after being pushed from Gitpod.

7. [Balsamiq Wireframes](https://balsamiq.com/wireframes/) was used to design the initial general layout and feel of the website.

8. [Autoprefixer CSS](https://autoprefixer.github.io/) was used to add vendor prefixes to the CSS rules, to ensure that they work across all browsers.

9. [Am I Responsive](https://ui.dev/amiresponsive?url=https://8002-coder4916-ci-milestone-ylxy4w9e48.us2.codeanyapp.com/index.html) was used to preview the website across a variety of popular devices.

10. [Squoosh](https://squoosh.app/) was used to reduce the file size of the images, and change from .jpg to .AVIF. This helped to improve the overall performance of the website.

11. [Heroku](https://www.heroku.com/home) was used to deploy the project.

[Back to top](#ceb-art)

## **Issues and Bugs**

- Issue: Migrating to Gitpod Enterprise.

Solution - env.py file was initially reinstated incorrectly and a new 'allowed host' in project settings.py also had to be updated correctly. The new url/endpoint in Stripe also needed fixing, to allow payments/webhooks to function properly. Sizes for all products had to be reset to true in the admin app, for sizes to display in products details. (Still missing in deployed version).

- Issue: Migrating products and categories from the Product and Category .models, error in console.

Solution - When migrating the product and category models for the first time, the migrations would not take effect. After some guidance and tutoring, I managed to makemigrations correctly, then migrate to the sqlite database.

- Issue: Displaying the Category badges on the products page.

Solution - After some debugging and checking the console for any clues, I contacted tutor support, who pointed out that I had not included the variable to get all the categories. Once this variable was added to the products view.py, the badges displayed ok.

- Issue: Requirements.txt not installing correctly, 'package not pip issue' error showing in console.

On migration to Gitpod Enterprise, I tried installing the requirements for my project in the new IDE. The installation stopped on the 3rd line of requirements, django-allauth. After investigating the issue in the console, I decided to install an updated version of django-allauth. This solved the issue.

- Issue: Sizes for products would not display in the shopping cart, once selected in the product details app.

When testing the products could be added to the shopping cart, I noticed that the sizes attached would not display in the cart. After printing the sizes to the console, I discovered that the sizes were not registering at all when the add to cart button was clicked. After some more investigation and tutor guidance, I discovered that the shopping cart would not accept the metadata I had attached to each size. Once removed, the products with sizes displayed correctly in the cart.

- Issue: Getting the webhooks to work, webhooks pending on Stripe website.

When trying to set up the Stripe payment system and connecting up Webhooks, I found that Webhooks were showing as pending on the Stripe website in developer tools. After some tutoring/guidance, I decided to revisit the Boutique Ado walkthrough, and discovered that several items were not linking up. This included having to set the wh_secret key correctly to get the Webhooks to work. Once the code was corrected, Webhooks were found to be working successfully on the Stripe website. 

- Issue: Static file not loading, 404 error in console.

After several different ways of trying to debug this issue, including changing file paths and positions, I contacted tutor support who pointed out after quite a while of debugging, that there was a single space that had been added accidentally included in the settings.py STATICFILES_DIRS variable. Once removed this solved the issue and the website displayed correctly once more.

- Issue: Webhooks suddenly stopped working when using a different device. Forbidden (CSRF cookie not set.) in console.

After trying to diagnose, copying code from the CI walkthrough, and noticing a 403 forbidden error on the Stripe website, I checked Slack for guidance and from there, found some information online which provided a workaround. After disabling the middleware csrf setting in settings.py the webhooks worked when tested.


## **Deployment**

The Website was developed using [Gitpod](https://gitpod.io/workspaces) and Gitpod Enterprise as the IDE, committed to Git as a local repository and finally pushed/stored to [GitHub](https://github.com/). The website was then deployed to [Heroku](https://www.heroku.com/home) using the following steps:

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
3. Save all files and then add, commit and push changes to GitHub
4. Log into Heroku.com and click “New” and then “Create a new app”
5. Choose a unique name for the app, select a region and click “Create app”
6. Go to the Settings tab of your new app
7. Click Reveal Config Vars
8. Return to your ElephantSQL tab and copy your database URL
9. Back on Heroku, add Config Vars for the ElephantSQL database, Stripe, and live emails. Make sure you click “Add”
10. Navigate to the “Deploy” tab of your app
11. In the Deployment method section, select “Connect to GitHub”
12. Deploy main branch, and view deployment.

[Back to top](#ceb-art)

## **Testing**

### **User Stories Testing**

#### **First Time User Goal**

1. As a first-time user, I want to be able to navigate the website with ease via a main navigation menu and structured layout.

- The navigation bar is clearly defined, with a subtle hover function when the user moves the cursor over the menu items.
- The title in the navbar leads the user back to the Home page increasing accessibility.
- Further information/social media links can be easily accessed via the footer.
- Links to all other pages are also displayed, with acces to a customers shop cart, and login/logout functions. 

![Nav Bar Screenshot](/media/navbar.png)

2. As a first-time user, I want to be able to purchase products safely and securely on the site.

- A Stripe payment system API and webhooks mean customers can pay for products safely and securely.

![Stripe payment example](/media/webhooksuccess.png)

3. As a first-time user, I want to know what products are listed on the site quickly and easily, being able to filter products where required.

- Visitors to the site are greeted with a Home page that contains a colorful header with search bar for further accessibilty, and introductory subtitle which links to the products page. The navbar allows the user access straight to the products page. All products are displayed in a card, with a button to view the product details. A filter/sorting dropdown is also included on the products page, and category badges are available.

![Search bar accessibilty](/media/Accessibility.png)
![Products accessibilty](/media/accessibilty-products.png)

4. As a first-time user, I want to be able to review the site's products safely and securely.

- A Django based admin app is built into the site, meaning a customer can create their own user account and browse the site securely.

![An example of a user account](/media/djangouserprofile.png)

5. As a first-time user, I want to be able to leave a review on the site if required, and see other user reviews on the site, safely and securely.

- User reviews can be accessed via the reviews page, in the About Us page.

![Reviews](/media/reviews.png)

6. As a first-time user, I want to be able to locate the site's social media links to see their followings and find any future updates/products to the site.

- Social media links are stored in the footer.

![Footer links]()

#### **Returning User Goal**

1. (As per first-time user tests)

#### **Frequent Visitor Goal**

1. (As per first-time user tests)

## **Manual Testing**

### **Responsiveness**

I used web developer tools extensively throughout the project to update and correct code, adjust website aesthetics, and check/improve and confirm responsiveness accross all devices, using a Bootstrap 'Mobile First' approach.

Below are some examples of areas of the site that I have tested and checked for full responsiveness on all devices. These images show the sections at each [Breakpoint](https://getbootstrap.com/docs/5.3/layout/breakpoints/#core-concepts).

![Header-sm](/media/headersm.png)

![Header-md](/media/headermd.png)

![Header-lg](/media/headerlg.png)

![Products-sm](/media/productssm.png)

![Products-md](/media/productsmd.png)

![Products-lg](/media/productslg.png)

### **Links Testing**

Once deployed, the website links were tested to ensure that:

- All navigation external/internal links are working correctly, and filepaths are correct.
- Hovering and Active states are working.
- All buttons are working as required.

### **Forms Testing**

The CEB Art details, shopping cart, checkout forms and emails were tested to make sure that the required fields and buttons/inputs are working, and the form POSTs any input data correctly to the site. I have included the following images, that display successful forms testing.

![Example of form data successfully posted to my_database](/media/orderssuccess.png)

![Stripe payment success](/media//paymentsuccess.png)

![Webhook success](/media/webhooksuccess.png)

![Console email confirmation](/media/console_email.png)

![Deployed email confirmation](/media/deployedemail.png)


## **Autoprefixer CSS**

Autoprefixer CSS was used to add CSS vendor prefixes to the CSS rules after the developing process was completed.

## **W3C Validator Testing**

The following image shows the CSS code placed into the W3C validator testing app to check for any incorrect code. There were no errors or warnings to show:

![Styles.css checked](/media/styles.css.png)

![Profiles css](/media/profiles.css.png)

![Checkout css](/media/checkout.css.png)

## **Lighthouse Testing**

Chrome Lighthouse testing was used to check the performance of the products app including accessibility, best practices, and SEO. After applying some changes to make the performance faster, including compression and resizing of images, the results below were achieved:

- Mobile:

![The CB Suite Lighthouse testing](/media/mobilelighthouse.png)

- Desktop:

![The CB Suite Lighthouse testing](/media/desktoplighthouse.png)

## **Further Testing**

The Website was tested on Google Chrome, Microsoft Edge and Mozilla Firefox.

The website was viewed on a variety of devices such as:

Windows Laptop
Mobile: Samsung Galaxy S12
Web developer tools devices

Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## **Credits**

### **Code**

1. The [Boutique Ado](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+3/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/) was used extensively to guide me through the creation of my site, through to project completion.

2. [Bootstrap 5.3](https://getbootstrap.com/): Bootstrap was utilised throughout, including the use of the following components:

- [Cards for each product and review](https://getbootstrap.com/docs/5.3/components/card/#about)
- [Bootstrap grid system](https://getbootstrap.com/docs/5.3/layout/grid/#example)

3. [Slack channels](https://app.slack.com/client/T0L30B202/C05E2K3NJTG) were used extensively to research debugging techniques and console issues.

4. [Autoprefixer CSS](https://autoprefixer.github.io/): was used to add vendor prefixer to CSS.

5. [W3C Validator Testing](https://validator.w3.org/nu/#textarea) was used to check for any errors in my CSS code.

### **Images**

I used this [image](https://www.pexels.com/photo/abstact-design-of-different-colors-2881262/) by [Kevin Dorg](https://www.pexels.com/@kevin-dorg-136105/), which was sourced from Pexels for the header of each application template.

The following images I sourced from various sites to use for my product cards:

Justin Maas's [Instagram](https://www.instagram.com/maas.art/); artwork was used for the pencil category cards, alongside some of my own sketches.

The Batman sketch was sourced from [Painting Valley](https://paintingvalley.com/download-image#batman-pencil-drawing-28.jpg)

The colorful eye was sourced from [Pinterest](https://www.pinterest.com/pin/1118018676229109658/)

[Pinterest](https://www.pinterest.com/search/pins/?q=paint%20art&rs=typed); was used to source all paint, Dali and Banksy images.

All chalk artwork was sourced from my own gallery.


## **Acknowledgements**

- My mentor, Oluwaseun Owonikoko, for her guidance and helpful feedback on all aspects of the Website.
- All Code Institute tutors for their patience and support, helping me with my coding issues, and assisting with debugging techniques.
- My wife Beth for her constant support throughout, and for proof reading and testing my site material.

[Back to top](#ceb-art)