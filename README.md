# Solid Properties Project

Solid Properties is a website where landlords\landladies and property managers can purchase a wide array of property services. The main purpose of the website is to provide to the users a **personalized shopping experience**.

## Table Of Contents
- [Solid Properties Project](#solid-properties-project)
  * [How It Works](#how-it-works)
    + [Instructions:](#instructions-)
    + [Further information:](#further-information-)
  * [Site Owners Goals](#site-owners-goals)
  * [User Stories](#user-stories)
    + [General Users](#general-users)
    + [Landlords/Landladies](#landlords-landladies)
  * [Design Choices](#design-choices)
    + [Images:](#images-)
      - [Hero Image From Home Page:](#hero-image-from-home-page-)
      - [Top Image from **Services** and **Profile** pages:](#top-image-from---services---and---profile---pages-)
      - [Category Images:](#category-images-)
    + [Fonts:](#fonts-)
  * [Colors:](#colors-)
    + [Icons:](#icons-)
      - [Services Icons:](#services-icons-)
    + [Extra:](#extra-)
      - [Brief Description Display For Each Service:](#brief-description-display-for-each-service-)
  * [Wireframes](#wireframes)
  * [Information Architecture](#information-architecture)
    + [Database Structure:](#database-structure-)
      - [Services App](#services-app)
        * [Category Model](#category-model)
        * [Services Model](#services-model)
      - [Profiles App](#profiles-app)
        * [LandlordProfile Model](#landlordprofile-model)
      - [Properties App](#properties-app)
      - [Properties Model](#properties-model)
      - [Checkout App](#checkout-app)
        * [Order Model](#order-model)
        * [OrderLineItem Model](#orderlineitem-model)
        * [OrderLineItemAnonym Model](#orderlineitemanonym-model)
  * [Technologies used](#technologies-used)
    + [Languages](#languages)
    + [Tools](#tools)
    + [Databases](#databases)
    + [Libraries and Frameworks](#libraries-and-frameworks)
  * [Features:](#features-)
    + [Fixed Navbar](#fixed-navbar)
    + [Footer](#footer)
  * [Individual List Of Properties](#individual-list-of-properties)
    + [Personalised shopping](#personalised-shopping)
    + [Automated Price Calculation](#automated-price-calculation)
  * [Activate & Deactivate Properties](#activate---deactivate-properties)
  * [Shopping Cart Table](#shopping-cart-table)
      - [Shopping cart table when the user is logged in and performs purchases for properties from her/his list:](#shopping-cart-table-when-the-user-is-logged-in-and-performs-purchases-for-properties-from-her-his-list-)
      - [Shopping cart table when the user is ***NOT*** logged in:](#shopping-cart-table-when-the-user-is----not----logged-in-)
  * [Testing](#testing)
  * [Bugs](#bugs)
  * [Deployment:](#deployment-)
    + [How to run this project locally:](#how-to-run-this-project-locally-)
    + [Instructions](#instructions)
    + [Deploying Solid Properties Project to Heroku:](#deploying-solid-properties-project-to-heroku-)
  * [Credits](#credits)
    + [Imgages:](#imgages-)
      - [Hero Image Home Page](#hero-image-home-page)
      - [Bakcground Image Secondary pages](#bakcground-image-secondary-pages)
      - [Category Images](#category-images)
    + [Code](#code)
    + [Aknowkedgments](#aknowkedgments)
  * [Disclaimer](#disclaimer)

## How It Works

Users are encouraged to sign up and register any number of properties from their profile section, thus creating their own list of properties on the website.

### Instructions:

1. Click the ```REGISTER``` tab and sign up on the website with your name and email address.
2. Go to your **PROFILE** page and register a property by clicking ```ADD PROPERTY```.
3. Complete the form provided with the property address, post code and number of bedrooms it comprises (please note that these are mandatory fields).
4. Activate your property from your *properties table* in the profile section.
5. Go to **SERVICES** page and choose a service.
**NOTE**: services differentiate between services with a fixed price and services for which the price varies (ex: **repainting**, **refurbishment**), depending on the number of bedrooms the service is purchased for*.
6. Below the service image, select from your list of properties the property for which you wish to purchase the service.
7. Based on the number of bedrooms the property selected comprises, a price will be instantly calculated. You will see displayed the **PRICE (per bedroom)** of the service, and next to it the **TOTAL COST** of the service for the property selected.

### Further information:

 * The ***shopping cart*** displays the price of the **service name**, the **price** of the service, **the property** for which the service has been purchased, the **price for the specific property** (as for many this varies from the initial price, depending on the number of bedrooms the property comprises of), the **total price of the service** for all of the properties that has been purchased for. At the bottom will be displayed the **total cost** of the shopping cart.
 * When the purchase is complete, a detailed **order history** will be provided in which the users will have a history 
of each service purchased and for which of their properties has been executed.
 * If a property is no longer required on the website, go to **PROFILE** page and from your list of properties table click on the ```DEACTIVATE``` tab to deactivate the property from the website. This will also disable your property from your list of properties when choosing a service.
**NOTE**: in your order history will be mentioned if a property is no longer active on the website*.

Of course, if a user doesn't wish to sign up, services can be purchased without the need of registration. Upon choosing a service, if its price depends of the number of bedrooms a property comprises, 
the user can choose for how many bedrooms a service can be purchased for.

## Site Owners Goals

* A personalised shopping experience for each user, where the price of each service will be calculated for each of their individual properties.
* A website that projects a clear representation of all the services provided, so that the client won't miss any oportunity in purchasing a service that is not well represented.
* A clear explanation of what every service is providing in detail, so that the client can easily find all the info on the webiste, without the need of callling the company for additional info.
* A clear explanation of how the prices are calculated, so that the client will have a better understanding of the total upon purchasing.
* A personalised profile where the client can add her/his properties, so that she/he can have the total cost of the each service in a quick manner, without having to enter the property details all the time when selecting a service.

## User Stories

### General Users
* As a user, I would like to be able to register to the website in a straight forward way, so I would have a profile where to be able to keep track of all my purchases. 
* As a user, I would like to be able to easily login or logout, so I can easily have access to my profile.
* As a user, I would like to be able to have clear live notifications on the screen everytime an important action was performed or is due to be performed, so I can be constantly up to date to what I'm doing and what I'm purchasing on the website.
* As a user, I would like to be able to have clear live notifications on the screen everytime an action cannot be performed or an error occurs, and a brief explanation, so I can correct the mistake and perform the action in cause again.
* As a user, I would like to be able to have a secure checkout so I know that the transaction and my card details are protected.
### Landlords/Landladies
* As a landlord\landlady, I would like to be able to see a full list of all services provided at once, so I can choose some to purchase.
* As a landlord\landlady, I would like to be able to see a list of categories of all services, so I can easily navigate to the ones that are within my interest.
* As a landlord\landlady, I would like to be able to see each service in detail, so can I have a clear understanding of what it's providing.
* As a landlord\landlady, I would like to be able to see price of each service depending on the size of the property, so I can have a clear understanding how much would cost for each of my properties.
* As a landlord\landlady, I would like to be able to search for a service by name, so I can easily find what I am looking for.
* As a landlord\landlady, I would like to be able to have a clear understanding of how the company works and how the prices are calculated, so I can be sure that my money are well spent.
* As a landlord\landlady, I would like to be able to have a clear display of my total spendings on the screen, so I can avoid going above my budget.
* As a landlord\landlady, I would like to be able to have a list of my own properties, so I when choosing a service, to know exactly the cost for that service for each of my properties.
* As a landlord\landlady, I would like to be able to deactivate a property anytime from the website, if that property is no longer required. Also, I would like to have the option to easily reactivate any property. 

## Design Choices

For Solid Properties I have used a dynamic, and in the same time professional style throughout all of its sections, creating a sense of professionalism and defining a target for active people.

### Images:

#### Hero Image From Home Page:

This image represents [Tower Bridge](https://en.wikipedia.org/wiki/Tower_Bridge), a renowned landlmark situated next to the City - one of London's main financial districts. This, in my opinion, gives the user a sense of dynamicity, meanwhile also providing a sense of familiarity, which can facilitate in creating a bond with the company **Solid Properties**. The source of this image can be found at the [Credits](#credits) section.

#### Top Image from **Services** and **Profile** pages:

This image represents London Bridge area in London, a dynamic and cultural area that is part of London's financial district. Its proximity to Tower Bridge gives the webisite with consistency. **Saint Paul** cathedral and **BT Tower** are also in the background, which again can provide a sense of familiarity. The source of this image can be found at the [Credits](#credits) section.

#### Category Images:

These images are representatives of each category of services. They contain suggestive images that help the user to better pin point the type of services within each category. The source of these images can be found at the [Credits](#credits) section.

### Fonts:

The fonts used in this project are the following:

* [LATO](https://fonts.google.com/?query=lato) I chose this font as a **main font** because I believe it offers a clear and professional look, which matches the website purpose.
* [NATO SERIF](https://fonts.google.com/specimen/Noto+Serif?preview.text_type=custom) I chose this font for **all titles** as it varies sufficent from the main font (Lato), offering a good enough contrast between them on the website's pages. In the same time, both of the styles blend in a smooth way together.

## Colors:

![Colors](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/colors.png)

The colors used in this project are the following:

* **Navy Blue** - This color is used for the navbar and footer plus on some other small elements in the project (like the head elements from the cart an checkout tables). I chose this color as, in my opinion, gives a professional appereance to the site and provides a clear contrast with the rest page.
* **White** - This color is used as a main background color throughout all pages of the website. I chose to use white because I believe it is the best color on which to display information in the most clear and intelligible way. This, among others, helps the user better focus on the functionality of a service.
* **Turquoise** - This color is used mainly for the call to action buttons and for the services' icons. It provieds a good contrast with both the white used for the main background and with the navy blue used for the navbar and footer. With the latter it also goes togeher, being part of the same family of colors.

### Icons:

#### Services Icons:

I chose to use icons as the website is selling services, rather than products, which can be represented by exact images of the product itself. Also, using just general images for each service might confuse the user in the first instance. The icons used are a representation of the category to which the service belongs to. Together with the brief description of the service below, they give the user a better understanding of what the service provides.

### Extra:

#### Brief Description Display For Each Service:

I chosed to use this design as I believe that, as stated above, it shows in a clear way what each service provides, thus making the user experience more intuitive.

## Wireframes

The wireframes for this project have been built using [BALSAMIQ](https://balsamiq.com/). Please see the wireframes below:

* [Desktop](https://github.com/Astig-1982/Solid-Properties-Project/blob/master/wireframes/wireframes_desktop.pdf)
* [Tablet](https://github.com/Astig-1982/Solid-Properties-Project/blob/master/wireframes/wireframes_tablet.pdf)
* [Mobile](https://github.com/Astig-1982/Solid-Properties-Project/blob/master/wireframes/wireframes_mobile.pdf)

**NOTE**: Parts of the wireframes differ from the website as during the development process I've reimagined the design and logic on certain pages in order to improve the overall UX. New elements have been introduced, while some of secondary importance have been discarted, mostly due to time constraints. For instance, the **PROFILE** page is completely different from the original wireframe as I thought that emphasizing on the list of properties rather than on the user's details is more important, considering the personalised shopping experience revolves around them. Nevertheless, the wireframes played a crucial role in the development process and served as excelent guidlines throughout.

[**Back to Top**](#table-of-contents)

## Information Architecture

During the development phase I worked with **sqlite3** database which is installed with Django.
For deployment, a **PostgreSQL** database is provided by Heroku as an add-on.

The **User** model used in this project is provided by Django as a part of defaults ```defaults django.contrib.auth.models```. More information about Django’s authentication system can be found [here](https://docs.djangoproject.com/en/3.1/topics/auth/default/).

### Database Structure:

#### Services App

##### Category Model 

| Field Name | Field Type | Validation | Key in db | 
--- | --- | --- | ---
**Name** | CharField | max_length=254 | name
**Friendly Name** | CharField | max_length=254, null=True, blank=True | friendly_name
**Image** | ImageField | null=True, blank=True | image
**Icon** | CharField | max_length=50, null=True, blank=False | icon

##### Services Model

This model is connected to **Category** model with a **ForeignKey**. 

| Field Name | Field Type | Validation | Key in db |
--- | --- | --- | ---
**Category** | FK to Category | null=True, on_delete=models.SET_NULL | category
**Name** | CharField | max_length=254, blank=False | name
**Price Variation** | BooleanField | default=False, null=True | price_variation
**Short Description** | TextField | blank=False | short_description
**Description** | TextField | blank=False | description
**Price** | DecimalField |max_digits=6, decimal_places=2 | price

#### Profiles App

##### LandlordProfile Model

This model contains **OneToOneField** connected to **User** model.

| Field Name | Field Type | Validation | Key in db |
--- | --- | --- | ---
**User** | OneToOneField to User | on_delete=models.CASCADE | user
**Default Full Name** | CharField | max_length=50, null=True, blank=False | default_full_name
**Default Email** | EmailField | max_length=254, null=True, blank=True | default_email
**Default Phone Number** | CharField | max_length=20, null=True, blank=True | default_phone_number
**Default Country** | CountryField | blank_label='Country *', null=True, blank=True | default_country
**Default Post Code** | CharField | max_length=20, null=True, blank=True | default_post_code
**Default Town Or City** | CharField | max_length=40, null=True, blank=True | default_town_or_city
**Default Street Address 1** | CharField | max_length=80, null=True, blank=True | default_street_address1
**Default Street Address 2** | CharField | max_length=80, null=True, blank=True | default_street_address2

#### Properties App

#### Properties Model

This model is connected to **LandlordProfile** model with a **ForeignKey**.

| Field Name | Field Type | Validation | Key in db |
--- | --- | --- | ---
**Landlord** | FK to LandlordProfile | null=True, on_delete=models.SET_NULL | user
**Street Address** | CharField | max_length=80, null=False, blank=Falsee | default_full_name
**House Name** | CharField | max_length=20, null=True, blank=True | default_email
**Post Code** | CharField | max_length=20, null=True, blank=True | default_phone_number
**Number Of Bedrooms** | DecimalField | max_digits=1, decimal_places=0 | default_country
**Activate** | BooleanField | default=False, null=True, blank=True | default_post_code

#### Checkout App

##### Order Model

This model is connected to **LandlordProfile** model with a **ForeignKey**.

| Field Name | Field Type | Validation | Key in db |
--- | --- | --- | ---
**Order Number** | CharField | max_length=32, null=False, editable=False | order_number
**LandlordProfile** | FK to LandlordProfile | on_delete=models.SET_NULL, null=True, blank=True | landlord_profile
**Full Name** | CharField | max_length=50, null=False, blank=False | full_name
**Email** | EmailField | max_length=254, null=False, blank=False |  email
**Phone Number** | CharField | max_length=20, null=False, blank=False |phone_number
**Country** | BooleanField | blank_label='Country *', null=False, blank=False | country
**Post Code** | CharField | max_length=20, null=True, blank=True | postcode
**Town Or City** | CharField | max_length=40, null=False, blank=False | town_or_city
**Street Address 1** | CharField | max_length=80, null=False, blank=False | street_address1
**Street Address 2** | CharField | max_length=80, null=False, blank=False | street_address2
**Date** | DateTimeField | auto_now_add=True | date
**Grand Total** | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 | grand_total

##### OrderLineItem Model

This model is connected to **Order**, **Services** and **Properties** models with **ForeignKeys**.

| Field Name | Field Type | Validation | Key in db |
--- | --- | --- | ---
**Order** | FK to Order | null=False, blank=False, on_delete=models.CASCADE | order
**Service** | FK to Services | null=False, blank=False, on_delete=models.CASCADE | service
**Property** | FK to Properties | null=False, blank=False, on_delete=models.CASCADE | the_property
**LineItem Total** | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | lineitem_total

##### OrderLineItemAnonym Model

This model is connected to **Order** and **Services** models with **ForeignKeys**. This model is used when the user checks out without being logged in.

| Field Name | Field Type | Validation | Key in db |
--- | --- | --- | ---
**Order** | FK to Order | null=False, blank=False, on_delete=models.CASCADE | order
**Service** | FK to Services | null=False, blank=False, on_delete=models.CASCADE | service
**Number Of Bedrooms** | DecimalField | max_digits=1, decimal_places=0, null=False, blank=False, editable=False | the_property
**LineItem Total** | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | lineitem_total

[**Information Architecture**](#information-architecture)

[**Back to Top**](#table-of-contents)

## Technologies used

### Languages

* [HTML](https://html.com/)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

### Tools

* [Gitpod](https://www.gitpod.io/) IDE used for developing this project.
* [Stripe](https://stripe.com) as payment platform to validate and accept credit card payments securely.
* [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
* [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) for version control.
* [GitHub](https://github.com/) to store and share project code remotely.
* [Heroku](https://www.heroku.com/) to deploy the project.
* [Balsamiq](https://balsamiq.com/) to create wireframes.
* [Tinypng](https://tinypng.com/) used to compress image files.

### Databases

* [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
* [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries and Frameworks

* [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.
* [Django Heroku](https://pypi.org/project/django-heroku/) to improve deployment of django projects on heroku.
* [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
* [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
* [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
* [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
* [Whitenoise](http://whitenoise.evans.io/en/stable/) to allows the web app to serve its own static files.
* [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
* [JQuery](https://jquery.com) to facilitate DOM manipulation.
* [Bootstrap](https://www.bootstrapcdn.com/) to facilitate the development of the website responsiveness and of the grid structure.
* [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for Vroom.
* [Google Fonts](https://fonts.google.com/) to style the website fonts.

[**Back to Top**](#table-of-contents)

## Features:

### Fixed Navbar

![navbar](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/navbar.png)

The navbar is fixed and on top of the screens and it's avaiable on all pages throughout. In it the user finds links to the following:
* **Home** page
* **Services** page
* **Categories** section
* **About** page
* **Profile** page - This will be displayed only if the user is logged in
* **Sign Out** call to action - This will be displayed only if the user is logged in
* **Register** call to action - This will be displayed only if the user is ***NOT*** logged in
* **Sign in** call to action - This will be displayed only if the user is ***NOT*** logged in
* **Search** box

Having the navabar fixed and accesible from all pages and sections, makes the site more easy and intuitive to use, thus improving the overall UX.

### Footer

![footer](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/Footer.png)

The foooter is fixed and visible an on pages. It contains the following:
* Links to social media. 
* Link to home page.
* Links to sign and register, and to profile page if the user is logged in. 
* Links to all categories.
* Company address.

I chose to display all categories on the footer as this makes them accesible to the user on all pages. It also impvroves the overall UX.

### Automated Price Calculation 

This feature will automatically calculate the price of the service, depending on the number of bedrooms the property comprises.

![total_price](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/total_price.png)

I chose to introduce this feature as the price of many of the services provided depends on how many bedrooms the property that it has been purchased for has. For example, the price for *Repainting* is **£500** per bedroom, so should it is purchased for a property comprising 4 bedrooms, the total price of the service will be **£2000**. This price is calculated automatically when the user selects the property she/he wishes the service to be purchased for. 
* I have realised this feature with the help of JavaScript. The code is located at the bottom of the page (*detailed_service.html*) in a ```script``` tag.

### Navbar Personalised Shopping Banner

This feature encourages the users to register and take advantage of the personalised shopping feature.

![activate](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/Screenshot+2021-04-03+at+14.06.33.png)

This banner takes the user to the **personalised shopping** page containing the instructions on how the personlised shopping experience works.

**NOTE**: This banner will be displayed only when the user is not logged in. This banner will also NOT be displayed on the **personlised shopping** page.

### Instructions For Personalised Shopping Experience

This feature has been created in order to clearly instruct the user on how the **personalised shopping experience** works.

![activate](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/personlised-instructions.png)

The page contains:

* Ordered list of instructions on how the **personalised shopping experience** works. **NOTE**: if the page is accessed when the user is logged in, the first instruction in the list will not be displayed as this specific instruction directs the user to register first.

* Call to action **REGISTER** button to encourage the user to register after reading the instructions. **NOTE**: this button is displayed only if the user is NOT logged in.

* Call to action buttons to take the user back to the page from where they accessed this section:
    * **BACK TO ABOUT** if the page has been accessed from **ABOUT** page.
    * **BACK TO PROFILE** if the page has been accessed from **PROFILE** page.
    * **CONTINUE SHOPPING** if the page has been accessed from anywhere else on the website except the above mentioned.

### Individual List Of Properties

This feature allows the user to create her/his own list of properties in the **PROFILE** section. 

![list_of_properties](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/list_of_properties.png)

This feature has been introduced to enable the **personalised shopping** feature listed below. The user can create her/his own list of properties. From this list she/he can choose the properties she/he wishes to purchase services for.

### Activate & Deactivate Properties

This feature allows the user to activate and deactivate properties from her/his list of properties.

![activate](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/activate.png)

If a property is no longer required on the website (maybe it's being sold or it's currently managed by a third party) the user can deactivate it from her/his **PROFILE** section. This will also disables the property from the options list upon choosing a service. And it will also be reflected in the **order history** where a red text below the property address will inform the user the *property is no longer active on the website*. Every property can be activated again at any point.
* This feature has been realised in the backend in the **properties** app. I created a ```BooleanField``` named ```activate``` in the **Properties** model. In **views.py** I created a function ```activate_deactivate``` that will update accordingly the ```BooleanField``` belonging to the specific instance of the **Properties** model.

### Personalised Shopping Experience

This feature allows the user to purchase services for each individual property from her/his list of properties.

![personalised](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/personalised_shopping.png)

I chose to implement this feature as it makes the experience on the site more dynamic. Most of the times the type of services provided by the webiste are to be executed to specific properties. In this case the user has the possibility to choose directly from the website the service and the property for which the service is purchased.
* This feature has been realised:
    * In the backend by accessing all the properties from the **Properties** model
    * In the front end by rendering them using a ```for loop``` in the ```select``` tag in the **detailed_service.html** template.

### Shopping Cart Table

This feature offers an in depth display of the shopping cart.

* This feature has been realised in the backend, in the **cart** app. 
    * In **views.py** I created a function ```add_to_cart```. This function takes the *street address* of the property from the front end and with its help retrieves the property from the **Properties** model. A dictionary will be created, that takes as ***key** the service and as **value** a list containing the id's of the properties retreived from **Properties** model.
    * In **context.py** I created ```cart_contents``` funnction that will use a **nested for loop** to iterate through the dictionary created in views.py. Within the first for loop a list named ```total``` will be created for each service. The second loop will iterate through the list of id's of each service, and will calculate the total cost of the service for the specific property. This will be appended to the ```total``` list created in the first iteration for each service. To calculate the total cost of a specific service for all of the properties purchased, I called python's ```sum()``` method to ```total```.
    * For **grand total**, in the same ```add_to_cart``` function I created a list named ```grand_total```. For each iteration of the first loop (for each service) to this list will be appended the sum of ```total``` list.   

Two variants of the **shopping cart** have been created, on if the user is logged in, and the other if the user is NOT logged in.

The same logic as stated above has been applied for displaying both of the shopping carts. Please see below:

#### Shopping cart table when the user is logged in and performs purchases for properties from her/his list:

This table contains:

* **Service Info** - This is the name of the service.
* **Service Price Per Bedroom** - This is the price of the service calculated for 1 bedroom property.
* **Property** - This is the property for which the service is due to be purhased.
* **Property Number Of Bedrooms** - This is the number of bedrooms the property comprises.
* **Total Cost Per Property** - This is the total cost of the service for the specific property.
* **Total Cost For All Properties** - This is the total cost of the service for all of the properties for which is due to be purhcased.

![cart_logged](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/cart_looged.png)

#### Shopping cart table when the user is ***NOT*** logged in:

This table contains:

* **Service Info** - This is the name of the service.
* **Service Price Per Bedroom** - This is the price of the service calculated for 1 bedroom property.
* **Number Of Bedrooms The Service To Be Executed For** - This is the number of bedrooms the services has been purhcased for.
* **Total Cost Per Property** - This is the total cost of the service for the specific property.
* **Total Cost For All Properties** - This is the total cost of the service for all of the properties for which is due to be purhcased.

![cart_not_logged](https://solid-properties-project.s3.eu-west-2.amazonaws.com/media/cart_not_logged.png)

I chose to use this feature as I believe the user should have a clean understanding of each service she/he buys, what property has been purhcased for, and how the total cost is calculated. In this case she/he will have a sense of veritable transparency and also it helps to keep the budget under control.

[**Back to Top**](#table-of-contents)

## Testing

Please see testing info in [TESTING.md](https://github.com/Astig-1982/Solid-Properties-Project/blob/master/TESTING.md).

## Bugs

During the development of the website, the following bugs have been detected:

* **Login bug** related to the shopping cart tables display - this bug has been documentated [here](https://github.com/Astig-1982/Solid-Properties-Project/blob/master/TESTING.md#known-bug-related-to-shopping-cart-tables-and-login-feature).

* **Shopping cart tables** bug - this bug has been documentated [here](https://github.com/Astig-1982/Solid-Properties-Project/blob/master/TESTING.md#detailed-shopping-cart-tables).

* **Deactivating Properties** bug - this bug has been documentated [here](https://github.com/Astig-1982/Solid-Properties-Project/blob/master/TESTING.md#deactivating-properties-from-the-website).

* **Order History** bug - this bug has been documentated [here](https://github.com/Astig-1982/Solid-Properties-Project/blob/master/TESTING.md#order-history).

* **Responsiveness** bug - this bug has been documentated [here](https://github.com/Astig-1982/Solid-Properties-Project/blob/master/TESTING.md#responsiveness).

## Deployment:

Solid Property Project was developed on GitPod using git and GitHub to host the repository.

### How to run this project locally:

To run this project on your own IDE follow the instructions below:

To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

Please click the links above for documentation on how to set these up and retrieve the necessary environment variables.

### Instructions

1. Save a copy of the github repository located at [Solid Properties repo](https://github.com/Astig-1982/Solid-Properties-Project) by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command

    ```
    git clone https://github.com/Astig-1982/Solid-Properties-Project
    ```

2. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:

    ```
    python3 -m .venv venv
    ```  

    ***NOTE**: The `python3` part of this command is for mac operating systems. Your command may differ, depending on the operating system you use*

4. Activate the .venv with the command:

    ```
    .venv\Scripts\activate
    ```

    *Again this **command may differ depending on your operating system**. Please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html).*

5. If needed, Upgrade pip locally with

    ```
    pip3 install --upgrade pip.
    ```

6. Install all required modules with the command

    ```
    pip3 -r requirements.txt.
    ```

7. Set up the following environment variables within your IDE.

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_SECRET_ACCESS_KEY | `<your secret key>`
DATABASE_URL | `<your postgres database url>`
DEVELOPMENT | `True`
SECRET_KEY | `<your secret key>`
STRIPE_PUBLIC_KEY | `<your secret key>`
STRIPE_SECRET_KEY | `<your secret key>`
STRIPE_WH_SECRET | `<your secret key>`
  

* If using an IDE that includes a `bashrc` file, open this file and enter all the environment variables listed above using the following format:

```
HOSTNAME="<enter key here>"
```

* `HOSTNAME` should be the local address for the site when running within your own IDE.

8. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with the command used at step 4.

9. Migrate the admin panel models to create your database template with the terminal command

```
python3 manage.py migrate
```

10. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:

```
python3 manage.py createsuperuser
```

11. You can now run the program locally with the following command:

```
python3 manage.py runserver
```

12. Once the program is running, go to the local link provided and add `/admin` to the end of the url.
13. Once instances of these items exist in your database your local site will run as expected.

### Deploying Solid Properties Project to Heroku:

* 1: **Create** a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```
* 2: **Create<** a Procfile with the following command.
```bash
echo web: python3 app.py > Procfile
```
* 3: **Push** these newly created files to your repository.
* 4: **Create** a new app for this project on the Heroku Dashboard.
* 5: **Provision** postgresql from Heroku Resources.
* 6: **Install** Dj Database Url with command:
```bash
pip3 install dj_database_url
```
* 7: **Install** Psycopg2 with command:
```bash
pip3 install psycopg2-binary
```
* 8: **Freeze** the new requirement using the same command as before.
```bash
pip3 freeze > requirements.txt
```
* 9: **Import** ```dj-database-url``` in the ```settings.py``` file.
* 10: **Add postgresql** as the default database in ```settings.py``` file.
* 11: **Run migrations** again for the new database.
```bash
python3 manage.py migrate
```
* 12: **Create superuser** again.
```bash
python3 manage.py createsuperuser
```
* 13: **Install**  ```gunicorn``` using the command.
```bash
pip3 install gunicorn
```
* 14: **Freeze** the new requirement using the same command as before.
* 15: In **Procfile** tell Heroku to create a web dyno which will run gunicorn and serve the solid_properties django app.
```bash
web: gunicorn solid_properties.wsgi:appllication
```
* 16: In **settings.py** add the host name of our heroku app to ALLOWED_HOSTS.
* 17: Connect Heroku to GitHub, in order to push directly to Heroku as well when pushing to GitHub. 
In **Heroku** go to ```Deploy``` tab, then click ```Connect to GitHub``` tab, serch for Solid-Properties-Project repository and click ```Connect```.
* Please make sure in the Heroku dashboard the following variables to be set:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_SECRET_ACCESS_KEY | `<your secret key>`
DATABASE_URL | `<your postgres database url>`
SECRET_KEY | `<your secret key>`
STRIPE_PUBLIC_KEY | `<your secret key>`
STRIPE_SECRET_KEY | `<your secret key>`
USE_AWS | `True`

[**Back to Top**](#table-of-contents)

## Credits

### Imgages:

#### Hero Image Home Page

* 

#### Bakcground Image Secondary Pages

* [telegraph.co.uk](https://www.telegraph.co.uk/travel/destinations/europe/united-kingdom/england/london/articles/)

#### Category Images

* **Repairs & Refurbishment** - [cpmcarpentry.com.au](https://cpmcarpentry.com.au/services/refurbishment/)
* **Marketing** - [shutterstock.com](https://www.shutterstock.com/search/marketing+plan)
* **Cleaning Services** - [topdowncleaning.co.uk](https://topdowncleaning.co.uk/blog/cleaning-home-against-covid19/)
* **Admin Services** - [rtpsurveyors.co.uk](https://www.rtpsurveyors.co.uk/services/architectural-design-project-services/contract-administration/)
* **Other Services** - [cloundlinkeduk.com](https://www.cloudlinkeduk.com/other-services/)
* **Free Of Charge** - [dreamstime.com](https://www.dreamstime.com/stock-illustration-free-charge-hand-ball-pen-writing-text-transparent-whiteboard-image59162021)
* **Plumbing & Electric** - [bestbettconstruction.com](https://bestbettconstruction.com/commercial-plumbing-and-electric/)
* **Legal** - [businessfirstfamily.com](https://businessfirstfamily.com/legal-contracts-business/)

### Code

* The course lessons from [CODE INSTITUTE](https://codeinstitute.net/) have provided an important reference in the development of this project. The code in the lessons has been a source of inspiration for many of the new notions approached in this project, especially the payment system.
* [Django Documentation](https://docs.djangoproject.com/en/3.1/) has proved to be a valuable and indispensable resource.
* [CSS-Tricks](https://css-tricks.com/) has been used as a source of inspiration for the **fixed footer**.

### Aknowledgments

Extra special thanks to my mentor [Simen Daehlin](https://github.com/Eventyret) who has been continually guiding and supporting me through the course. This had a great influence in my journey of becoming a junior developer.

All tutors from [CODE INSTITUTE](https://codeinstitute.net/) who have always been extremely responsive and offered excellent guidance and support on every approach.

Fellow coders from [Slack](https://slack.com/intl/en-gb/) who have been helpful and supportive during the development of all my projects.

Although I don't have yet an account and never communicated with coders from Stack Overflow, I would like to aknowledge the fact that many times when I simply googled an enquiry related to coding, I found myself navigating on the [Stack Overflow](https://stackoverflow.com/) page where I could find answers to my questions as many of them were already asked by fellow coders in the past. This contributed considerably to the development process and in the implementaion of some of the features.

## Disclaimer

This site is developed for **educational purposes** only. The company **Solid Properties** including its affiliated London address - **212 Marylebone Rd, London, NW1 5LS** - is purely fictional.

[**Back to Top**](#table-of-contents)





