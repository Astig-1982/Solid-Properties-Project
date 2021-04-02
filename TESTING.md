# Testing

[README.md](https://github.com/Astig-1982/Solid-Properties-Project#table-of-cart_contents) file.

## Table Of Contents 
- [Testing](#testing)
  * [Automated Testing](#automated-testing)
  * [Test Driven Development](#test-driven-development)
  * [Manual Testing](#manual-testing)
    + [Navbar&Footer](#navbar-footer)
    + [Website links](#website-links)
    + [Categories Display](#categories-display)
    + [Sort By](#sort-by)
    + [Serch box](#serch-box)
    + [Adding properties to the list in the **Profile** section and diplaying them in the **Select a property** dropdown list on the **detailed_service** page](#adding-properties-to-the-list-in-the---profile---section-and-diplaying-them-in-the---select-a-property---dropdown-list-on-the---detailed-service---page)
    + [Automated calculation of the total price](#automated-calculation-of-the-total-price)
    + [Shopping cart tables](#shopping-cart-tables)
    + [Payment System](#payment-system)
    + [Authentification System](#authentification-system)
    + [Deactivating Properties From The Website](#deactivating-properties-from-the-website)
      - [Further testing on this feature:](#further-testing-on-this-feature-)
    + [Activating properties on the website](#activating-properties-on-the-website)
    + [Order History](#order-history)
    + [Saving and updating user's details at billing_details section](#saving-and-updating-user-s-details-at-billing-details-section)
    + [Responsiveness](#responsiveness)
  * [Further Testing](#further-testing)

## Automated Testing

I have used the following validation services to test the code used to built this webiste:

* [W3C Markup Validation](https://validator.w3.org/) - used to validate **HTML** code.
* [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) - used to validate **CSS** code.
* [JSHint](https://jshint.com/) - used to validate **JavaScript** code.
* [Python Extension For Visual Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Test Driven Development

I chose not to use Test Driven Development for this project as being my first encounter with Django I was still in the learning process while working on this project. Hence it was difficult to apply automated testing on models and functions which at the time of development I was yet to have a full comprehension of.

Now that I have a much better understanding of Django, I am plannig to subject the entire project to automated testing in the very near future.

[**Back to Top**](#table-of-contents)

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

* I have tested this feature multiple times by simply adding properties to the list in the **Profile** section and checking that the same properties are rendered in the dropdown list on the **detailed_service** page. I have repeated this action severall times throught the development and the feature works every time as expected. 

### Automated calculation of the total price

* This feature calculates the price for each service, depending on the number of bedrooms the property comprises.
    * The testing for this feature was very straight forward. Upon selecting the preferred property (or the number of bedrooms if the user is not logged in) from the dropdown list on the **detailed_service** page, I ws checking if the total price displayed was updating accordingly - **price per bedroom * the number of bedrooms**. I have performed this action multiple times with different services for different properties and the feature works as expected every time.

### Shopping cart tables

Both shopping cart tables have been tested -  for logged in and not logged in users.

This feature went under strong scrutinity as it represents one of the most important features of the personalised shopping experience.

* The testing has been performed by adding different services for different properties in the shopping cart. Afterwords I was checking the table to make sure the correct properties are attributed to the correct services, as selected when they were added to the cart. Equally important I was checking to make sure the price for each service is calculated accordingly - for each individual property and also for all of the properties that is due to be purchased for. The following **BUG** has been detected:
    * In the corresponding field, instead of displaying the price of the service for ALL of the properties that is due to be purhcased for, it displayed the price calculated only for the last property. 
    * **Cause** - this is because in the **cart** app in **context.py** at ```cart_contents``` function created to display the shopping cart, I created the empty list named ```total``` (where the price of all of the properties is appended) in the second ```for loop``` of the nested loop. This loop was used to iterate through the list of properties of the specific service - **the logic of this feature has been documentated in the README.md file [here](https://github.com/Astig-1982/Solid-Properties-Project#detailed-shopping-cart-table)**.
    * **Correction** - I've corrected this bug by simply creating the empty list named ```total```  in the first ```for loop``` of the nested loop (when iterating through services). Thus, for each service, ```total``` list will append the price for each of the property associated with that specific service.

I've since performed multiple tests by adding different services for different properties and I am happy to announce that the feature now works as expected.

[**Back to Top**](#table-of-contents)

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

### Deactivating Properties From The Website

When it was first designed, the purpose of this feature was to remove the property entirely from the list of properties. It was working as expected, however 2 **BUGS** have been detected:

* **BUG** - when the property was removed from the website, an error was occurring in the *order history* section, if services have been purchased for the specific property. This is because the order history retrieves the properties from the **Properties** model and based on the number of bedrooms the property comprises, it calculates the total amount of the specific service. If the property is no longer available in the **Properties** model, the price for the specific service comes as 0. 
    * **Correction** - I have amended this error by choosing to deactivate the property from the website, rather than completely removing it. Documentation for this feature can be found [here](https://github.com/Astig-1982/Solid-Properties-Project#activate--deactivate-properties). This actually improves the overall UX as now the user has also the possibility to reactivate the property back anytime.

* **BUG** - if the user adds services to her/his shopping cart and after navigates to the **Profile** section and decides to deactivate  a property for which a service has been prior added to the shopping cart, when returning to the shopping cart the property will still be there - which is wrong because the property is no longer active on the website and services cannot be purchased for it.
    * **Correction** - In the **properties** app in **views.py** I have modified the ```activate_deactivate``` function, and now this function first checks if the property is in the current shopping cart session, and if it is, it will be removed and the shopping cart will be updated accordingly.

Now this feature works as expected.

#### Further testing on this feature:

* Confirm that when a property is deactivated from the website, the specific property will be disabled from the **Please select a property** dropdown list on the **detailed_service** page.
* Confirm that when a property is deactivated, in the **order history** section a red text below the respective property will be displayed, notifying the user the *property is no longer available*

### Activating properties on the website

* Confirm that this feature works as expected - every time a property is being activated or reactivated, the **detailed_service** and **order history** sections will update accordingly.

### Order History

 * This feature manifested the **BUG** mentioned at the testing of **deactivating properties** feature and its description and correction have been documentated above. No other bugs have been detected during the development and testing of this feature.

Confirm that the order history works as expected and the services together with their corresponding properties and correct prices are displayed correct.

[**Back to Top**](#table-of-contents)

### Saving and updating user's details at billing_details section

* **Note**: this feature works only if the user is logged in. 

* Confirm that every time a user checks out, if *save details* checkbox is being clicked her/his billing details will be saved at **billing_details** section.
* Confirm that when a user updates her/his details in the **billing_details** section, her/his details will update accordingly.
* Confirm that if a user is NOT logged in, the message ***Save these details to my profile*** will NOT be displayed.
    * **Note**: I chose not to display this message if the user is not logged in, in the favour of another message that encourages the user to log in in order to benefit of the personalised shopping experience. I chose to emphasize more on the **personalised shopping experience** feature as I believe it is more important and it will better persuade the user to sign up.

No bugs have been detected and this feature works as expected.

### Responsiveness

This website has been developed to be responsive on all major type of screens:

* **Extra Large Desktops** ```@media (min-width: 1500px)``` - fully responsive.

* **13 inch Macbook Screens** ```@media (min-width: 1200px) and (max-width: 1499px)``` - fully responsive.

* **Large Tablets** (Ex: IPad Pro) ```(min-width: 1024px) and (max-width: 1199px)``` - fully responsive.

* **Tablets** ```@media (min-width: 768px) and (max-width: 1023px)``` - fully responsive.

* **Large Mobiles Screens** (Ex: IPhone 6/7/8 Plus) ```@media (max-width: 576px)``` - fully responsive.

* **Regular Mobiles Screens** (Ex: Iphone 6/7/8, Huawei P30) ```@media (max-width: 375px)``` - fully responsive.

During the development of the website's responsiveness, the following **BUG** has been detected:

* **Overflow**
    * *Checkout* page exhibits small padding/margin on the right hand side of the screen. The bug behaves exactly the same on all types of screens. My attemps in removing it have been unsuccesfull and due to time constraints I've decided to postpone further investigation.

I am confident I will completely crush this bug in the very nearest future.

## Known **BUG** related to shopping cart tables and login feature.

A bug has been detected at ```cart_contents``` function at **contexts.py**.

### Description:

The website has been developed to function different if the user is logged in, compared to if the user is logged out.

If the user is **logged in**:

* the cart table will display the property for which a certain service is being purchased. To achieve this, in **cart** app the ```add_to_cart``` function in **views.py** will store in a list the ***id*** of the property submitted. Please see below:

```bash
cart[service_id].append(the_property.id)
```

The **cart** session will be a dictionary that looks like this:

```bash
cart = {
    'service_id': [property.id, property.id],
    }
```


If the user is **logged out**:
* the cart table will display the number of bedrooms for which a certain service is purchased. To achieve this, in **cart** app the ```add_to_cart``` function in **views.py** will store in a list the ***number the bedrooms*** submitted. Please see below:

```bash
cart[service_id].append(no_of_bedrooms)
```

The **cart** session will be a dictionary that looks like this:

```bash
cart = {
    'service_id': [no_of_bedrooms, no_of_bedrooms],
    }
```

Consequently, the logic of ```cart_contents``` function -- the function that handles the shopping cart -- is different for each of the above cases.

In the former case, the ```nested for loop``` in the ```cart_contents``` function iterates through the **shopping** cart and it retrieves the **property** from the Properties model, using the ***id*** stored in a list at ```add_to_cart``` function in **views.py**. It will then append ***the property*** to the **list_properties_or_bedrooms** list. Please see below:

```bash
for service, properties_or_bedrooms in cart.items():

        ...

        list_properties_or_bedrooms = []
        service = get_object_or_404(Services, pk=service)
        for property_or_bedrooms in properties_or_bedrooms:
            if request.user.is_authenticated:
                the_property = get_object_or_404(Properties,
                                                 pk=property_or_bedrooms)

                ...

                list_properties_or_bedrooms.append({
                    'property': the_property,
                    ...
                })
```

**NOTE**: **property_or_bedrooms** in this case represents the ***id*** of each of the properties.

In the latter case, the ```nested for loop``` in the ```cart_contents``` function will iterate through the **shopping cart** and will retrieve from the list the ***number of bedrooms***. It will then append the ***no_of_bedrooms*** to the **list_properties_or_bedrooms** list. Please see below:

```bash
for service, properties_or_bedrooms in cart.items():

        ...

        list_properties_or_bedrooms = []
        service = get_object_or_404(Services, pk=service)
        for property_or_bedrooms in properties_or_bedrooms:

                ...

                list_properties_or_bedrooms.append({
                    'no_of_bedrooms': property_or_bedrooms,
                    ...
                })
```

**NOTE**: **property_or_bedrooms** in this case represents the ***no_of_bedrooms*** added.

The **bug** manifests in the following way:

If a user is **NOT** logged in and adds items to her/his **shopping cart**, and afterwords decides to **log in** *without emptying the cart or completing the purchase*, the **shopping cart** will still contain the items added prior to log in and the website will exhibit the following behaviours:

* The **shopping cart** table will contain the services added and also random properties. 

#### Explanation:

This is because the ```for loop``` at ```cart_contents``` will attempt to retrieve **properties** from Properties model using as ***id's*** the ***number of bedrooms*** added prior to the cart.

* The website will crush and will throw a **404 error** with the message:

```No Properties matches the given query.```

#### Explanation:

Again the  ```for loop``` will iterate through the **shopping cart** and will attempt to retrieve properties using the ***id's*** found in the list.

But if there are no properties in the model with the specific ***ids***, the site will crush and throw the above error.

Both of the above outcomes are wrong and unwanted. The latter is because of obvious reasons - the site will crash.

The former is because the properties displayed in the **shopping cart** table do not belong there (neither the services in the first place) as they have been retrieved using wrong ***id's*** (the **id's** representing actually the **number of bedrooms** added to the list prior to loggin in).

### Solution:

I believe the bug will be solved if the **shopping cart** will be empty and ready to go as soon as a user logs in. I am confident this can be achieved by overriding the **Django login view** - deleting the cart session variable upon logging in. As this being my very first project using Django and still learning while developing and mostly due of exigent time constraints and the fact that I understand that the login view contains about 900 lines of code, I decided not to approach this solution for the the being. 

### Attempts in solving the bug without overriding the Django login view:

1. Adding a ```try/except``` block at ```cart_contents```. 

This solves the issue only if the ***id*** of the property doesn't correspond with the ***number of bedrooms*** added in the list. The ```for loop``` will try to retrieve the property, will not find it based on the ***id*** and the ```exception``` will take place. However if it finds a property with an ***id*** corresponding with the number of bedrooms, the ```exception``` will not happen. Consequently, the first behaviour mentioned above will take place.

Therefore I decided to abandon this solution.

2. In ```cart_contents``` function at the ```for loop```, before retrieving the property, I check if the element (**property_or_bedrooms**) retrieved from the list represents the ***id*** of a property, or the ***no_of_bedrooms***. In order to do this, I believe the easiest way is to check the type of the element. Currently, the type of the element is ```integer``` in both cases. So I decided the **id's** of the properties to be added as ```float``` numbers and the ***no_of_bedrooms*** to be added as integers. Please see below: 
    * In **views.py** at ```add_to_cart``` function:

        ```bash
        cart[service_id].append(float(the_property.id))
        ```
    * In **contexts.py** at ```cart_contents``` function:

        ```bash
        for service, properties_or_bedrooms in cart.items():

        ...

        list_properties_or_bedrooms = []
        service = get_object_or_404(Services, pk=service)
        for property_or_bedrooms in properties_or_bedrooms:
            if request.user.is_authenticated:
                if isinstance(property_or_bedrooms, int):
                    del request.session['cart']
                    break

                    ...
        ```
**NOTE**: If the type of the element is ```integer```, it means that the **shopping cart** contains the ***no_of_bedrooms*** and **NOT** the ***id's*** of the properties.

Unfortunately this fails as upon loggin in, the website throws a **KeyError exception** as **cart** session variable is not found.

3. Based on the same logic mentioned above, I try to clear the **shopping cart** dictionary stored in **cart** variable, instead of deleting the session variable. This is achieved using ```cart.clear()```.

This also fails and the folowing error is thrown:

     dictionary changed size during iteration

I believe this is because the external ```for loop``` will still take place after the ```nested for loop``` breaks. However, because the cart dictionary is modified inside the nested loop, the error occurs. 

A way around it is to break from both the nested and external loops as soon as the ```if statement``` "discovers" that the element retrieved is an ```integer```. But because the external loop acts in the same way if the user is logged in or not (only the nested loop is different), this involves re-creating the whole logic of ```cart_contents``` function, even possibly creating 2 different functions for each of the situations (user logged in, user logged out). 

I decided again not to approach this solution because of exigent time constraints.

### Verdict:

I cannot emphasize strong enough on the fact that my belief is that the cleanest and simplest solution to the problem is overriding the **Django login view**. However, I am confident I could possibly work my way around it using similar methods as stated above, although I believe this is not the most productive way and will only complicate the code.

**Rest assured that as soon as this project will be finished and the results from the school will be in, I will do research on how to override the login function and I will completely crush this bug!!**
 
## Further Testing

* During the develpment process the website was constantly testing locally with debugger: ```debug=True```. Every time the website crashed the debugger displayed a message describing the error. This helped me find the location of the error and fix it.
* Friends and familiy members have been kindly asked to test the website multiple times and offer feedback on its design and functionality. Their feedback helped me improve the overall UX.

[**Back to Top**](#table-of-contents)




