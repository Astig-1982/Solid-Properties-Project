# Solid Properties Project

Solid Properties is a website where landlords\landladies and property managers can purchase a wide array of property services. The main purpose of the website is to provide to the users a personalized shopping experience.

## How It Works

Users are encouraged to sign up and register any number of properties from their profile section, thus creating their own list of properties on the website.
When registering a property, the mandatory info will be the property address and the number of bedrooms it comprises.
Based on the number of bedrooms each property comprises, a price will be instantly calculated upon choosing a specific service. 
The shopping cart will display the price for each service for each individual property (as for many the price varies, depending on the number of bedrooms the property comprises), and also the 
total price of the service for all of the properties that has been purchased for. When the purchase is complete, a detailed order history will be provided in which the users will have a history 
of each service purchased and for which of their properties has been executed. If a property is no longer required on the website, the user can deactivate it anytime from his/her profile section. 
In fact, every property can be activated and deactivated as many times as the user wants.

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

## Deployment:

Solid Property Project was developed on GitPod using git and GitHub to host the repository.

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
