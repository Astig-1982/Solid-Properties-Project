# Testing

## Automated Testing

I have used the following validation services to test the code used to built this webiste:

* [W3C Markup Validation](https://validator.w3.org/) - used to validate **HTML** code.
* [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) - used to validate **CSS** code.
* [JSHint](https://jshint.com/) - used to validate **JavaScript** code.
* [Python Extension For Visual Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Test Driven Development

I chose not to use Test Driven Development for this project as being my first encounter with Django I was still in the learning process while working on this project. Hence it was difficult to apply automated testing on models and functions which at the time of development I was yet to have a full comprehension of.

Now that I have a much better understanding of Django, I am plannig to subject the entire project to automated testing in the very near future.

## Manual Testing

### Navbar&Footer

* Clicked each link in the navbar to confirm that it leads to the correct page.
* Confirm that when the user is logged in, ***Profile*** and ***Sign Out*** are displayed and when the user is logged out, ***Register*** and ***Sign In*** are displayed.

### Website links

* Clicked on every link on the webiste to see if it takes the user to the correct pages.

### Categories Display

* Confirm that every **Category** call to action from the home page retrieves the expected categories. I confirm the same outcome when selecting a category from the **Category** dropdown list on **Services** page.

### Sort By 

* Confirm that the selected sorting from the **Sort By** dropdown list on **Services** page works as expected.

### Serch box

* I've tested multiple times this feature performing the following:

    * **Finding services based on key words** - I've typed in the input area and submitted key words and every search retireved all services that contain the respective words.
    * **Behaviour when submitting an empty search box** - I've submitted an empty query by clicking on the serch button without having anything typed in the input area. The feature works as expected - the user is notified by a *WARNING* message that ***no entry has been detected***.
    * **Behaviour when submitting key words not contained by any service provided** - I've submitted an entry containing key words to check how this feaure behaves. 
        * At first it returned the user to the **Services** page without any service displayed on it.
        * I've corrected this UX inconvenient by simply introducing an ```If``` statement in the **services.html** template to check if the template variable ```services``` exists, and if it does the code to retrieve all services was executed. If not, a message will be displayed stating that ***no services within your search criteria have been detected***. 
The feature works now as expected.

### Adding properties to the list in the **Profile** section and diplaying them in the **Select a property** dropdown list on the **detailed_service** page

* I have tested this feature multiple times by simply adding properties to the list in the **Profile** section and checking that the same properties are rendered in the dropdown list on the **detailed_service** page. I have repeated this action severall times throught the development and the feature works everytime as expected. 

### Automated calculation of the total price

* This feature calculates the price for each service, depending on the number of bedrooms the property comprises.
    * The testing for this feature was very straight forward. Upon selecting the preferred property (or the number of bedrooms if the user is not logged in) from the dropdown list on the **detailed_service** page, I ws checking if the total price displayed was updating accordingly - **price per bedroom * the number of bedrooms**. I have performed this action multiple times with different services for different properties and the feature works as expected every time.

### Detailed shopping cart tables

This feature went under strong scrutinity as it represents one of the most important features of the personalised shopping experience.

* The testing has been performed by adding different services for different properties in the shopping cart. Afterwords i was checking the table to make sure the correct properties are attributed to the correct services, as selected when they were added to the cart. Equally important I was checking to make sure the price for each service is calculated accordingly - for each individual property and also for all of the properties that is due to be purchased for. The following **bug** has been detected:
    * In the corresponding field, instead of displaying the price of the service for ALL of the properties that is due to be purhcased for, it displayed the price calculated only for the last property. 
    * **Cause** - this is because in the **cart** app in **context.py** at ```cart_contents``` function created to display the shopping cart, I created the empty list named ```total``` (where the price of all of the properties is appended) in the second ```for loop``` of the nested loop. This loop was used to iterate through the list of properties of the specific service - **the logic of this feature has been documentated in the README.md file [here](https://github.com/Astig-1982/Solid-Properties-Project#detailed-shopping-cart-table)**.
    * **Correction** - I've corrected this bug by simply creating the empty list named ```total```  in the first ```for loop``` of the nested loop (when iterating through services). Thus, for each service, ```total``` list will append the price for each of the property associated with that specific service.

I've since performed multiple tests by adding different services for different properties and I am happy to announce that the feature now works as expected.

### Payment System

I have strongly emphasised on the testing of this feature as it was my first time working with [STRIPE](https://stripe.com/gb). The following have been carried:

* Using the mock card number provided by Stripe, I performed multiple payments for various services.
* In my Stripe account I checked every single payment that went through to match 100% with the payment performed on the webiste.
* Checking the behaviour if incorrect or incomplete cart details are entered. I can confirm that by introducing incorrect or incomplete card details the payment will not take place and the user will be notified with a *WARNING* message as expected. 

Throughout the testing of this highly important feaure of the website no errors have been detected and the payment works as expected.

### Authentification System

I have used as authentification system the built-in components of Django [allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) package.

* This feature has been tested multiple times by creating different accounts, then logging in and out.

No errors have been detected and the feature works as expected.

### Deactivating properties from the website

When it was first designed, the purpose of this feature was to remove the property entirely from the list of properties. It was working as expected, however 2 **bugs** have been detected:

* **Bug** - when the property was removed from the website, an error was occurring in the *order history* section, if services have been purchased for the specific property. This is because the order history retrieves the properties from the **Properties** model and based on the number of bedrooms the property comprises, it calculated the total amount of the specific service. If the property is no longer available in the **Properties** model, the price for the specific service comes as 0. 
    * **Correction** - I have amended this error by choosing to deactivate the property from the website, rather than completely remove it. This actually improves the overall UX as thus the user has the possibility  to reacitvate the property back anytime.

* **Bug** - if the user adds services to her/his shopping cart and after navigates to the **Profile** section and decides to deactivate  a property for which a service has been prior added to the shopping cart, when returning to the shopping cart the property will still be there - which is wrong because the property is no longer active on the website and services cannot be purchased for it.
    * **Correction** - In the **properties** app in **views.py** I have modified the ```activate_deactivate``` function, and now this function first checks if the property is in the current shopping cart session, and if it is, it will be removed and the shopping cart will be updated accordingly. 





