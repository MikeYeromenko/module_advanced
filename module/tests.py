from django.test import LiveServerTestCase



class UserCaseTest(LiveServerCaseTest):
    pass




"""
User opens the main page of the shop. On it he sees a list of goods. He sees
title of goods, its description, price, /*photo*/, quantity of goods left.
The description field is not longer then 40 symbols. If its longer, user can 
watch just first 37 symbols, which end with three dots (...)

Near every product there a text input to enter a quantity of goods he wants 
and button "buy". User can also click on one of the goods, and after that he 
comes to a page with details about the one of goods he had chosen. On that page
he sees all information he saw before, plus full description of the chosen goods


He has links in nav-bar to login and to registrate. Theres also about link,
which redirects to the page "About" where a user can see information about the 
shop

When user opens login page, he sees to fields for entering username and password.
The field for password is password input, so user doesn't see the text he prints
in this field.



If a superuser logins, he is redirected to the admin page,
where he sees pages: Watch goods, Add goods, Change goods (one per an action)
and Watch returns

"""
