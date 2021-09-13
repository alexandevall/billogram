# billogram
The task is to make a backend-service for "brands" (consumer-facing businesses) that generates discount-codes, and let users (our users) view and get these discount-codes.

I have modeled the problem as follows:
* A brand can create a Discount, which represents a collection of discount-codes along with some extra data such as name (the name of the discount) and webhook-url to call when users get discount-codes.
* A user can get a DiscountCode from a Discount. I am imagining that a user finds a discount that he/she wants to get a discount-code for, and asks this service to generate and/or retrieve the code.

One key design choice I have made is to not generate all discount-codes the moment a brand asks to have X discount-codes generated. Instead, these are generated on an ongoing basis whenever a user asks for a discount-code. The reasons for this are twofold:
* We can customize the discount-code with the user's username (or even name, perhaps) in mind. Instead of the code being a string of meaningless characters, we can make it part of a brand's customer experience. I have for instance made discount-codes look like this: "[brand_name]-thinks-[username]-is-awesome-[id for discount]", which looks way nicer than a random id.
* We make sure that every code generated is associated with a user.
  
An important assumption I have made is that authorization can be done by tokens passed in request headers. I have also assumed that authorizations is
different for "brands" and "users".

To run the project:
1) Make sure python3 and pip3 is installed: python3 --version and pip3 --version.
2) If you do not have virtualenv installed, install it: pip install virtualenv.
3) Go to the project root.
4) Create a new virtualenv: python3 -m venv env.
5) Activate the virtual environment: source env/bin/activate.
6) Install dependencies: pip install -r requirements.txt
7) Run the project: python3 main.py.

It is also possible to test creating and getting codes:
To test creating codes: python3 test/create_codes.py  
To test getting a code: python3 test/get_code.py. 
Note! This get codes you need to enter a valid discount-id as the last parameter in the get_code function in test/get_code.py. A valid discount-id is any filename found in database/Discount. If there are no files in database/Discount, start by creating codes.

