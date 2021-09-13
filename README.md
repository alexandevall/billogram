# billogram
A task for interview: create a discount-code service

The task is to create a backend-service for "brands" (consumer-facing businesses) to generate discount-codes, and let users (our users) view and get these discount-codes.

I have modled the problem as follows:
* A brand can create a Discount, which represent a collection of discount-codes a long with some extra data such as name (the name of the discount) and webhook-url to 
call when users get discount-codes.
* A user can get a DiscountCode from a Discount. I am imagianing that a user finds a discount that he/she wants to get a discount-code for, and asks this service to generate and/or
retrive the code. 

One key design choice I have made is to not generate all discount-codes the moment a brand asks to have X discount-codes generated. Instead, these are generated on an ongoing basis,
whenever a user asks for a discount-code. The reasons for this are twofold:
1) We can customsize the discount-code with the user's username (or even name, perhaps) in mind. Instead of the the code being a string of meaningless charecters, 
we can make it part of a brand's customer experience. I have for instance made discount-codes look like this: "<brand_name>-thinks-<username>-is-awesome-<id of the discount>", 
which looks way nicer than a random id.
2) We make sure that every code generated is associated to a user.

An important assumptions I have made is that authorization can be done by tokens passed in request headers. I have aslo assumed that authorizations is  
different for "brands" and "users".

To run the project:
1) Make sure python3 and pip3 installed: python3 --version and pip3 --version.
2) If you do not have virtualenv installed, install it: pip install virtualenv.
3) Create a new virtualenv: virtualenv venv
4) Activate the virtual environmnent: source venv/bin/activate
5) Install dependencies: pip install -r requirements.txt
6) Run the project: python3 main.py

