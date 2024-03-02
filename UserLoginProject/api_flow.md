### Django MVT architecture Overview
- Important files in django framework to check 
  - urls.py
  - views.py
  - models.py
  - apps.py
  - tests.py
  - admin.py
  - settings.py
- urls.py
  - Contains the URL routing for each view
- views.py
  - Contains the backend processing for each view
- models.py
  - Contains the fields of the table, and model function which can be executed on an object of that table
- apps.py
  - Contains the init sequence that needs to be executed to setup the application
- tests.py
  - This contains unit testing for model function, unit testing, integration tests, and scaling tests for views
- admin.py
  - This contains the models that are to be registered in the django administrator which lets you see the records of each table
- settings.py
  - This contains all project related settings and configuration 
  which are required to run the application
 
### API flow in Django 

    - User will send a request to the server then request goes to urls.py and search for path then navigate to views.py
    - From views will connect to database models to fetch data or to do CRUD operations
    - Implemented Token based authentication. When user login user will get token so user should send token in each request 
    to access resources
    - After successfull login user will add customers .User must be authenticated to add customers. so each customer should have unique email.
    - Validating customer data and storing data in database 
    if not valid then throwing error messages
    - After adding customers user will logout with token. User must send token in headers to logout then user will be logged out from current session.

----------------------------------------------
----------------------------------------------
### React App Overview
  - Important files to check 
    - index.tsx 
    - App.tsx
    - AddCustomer.tsx
    - Login.tsx
    - Logout.tsx
    - backendinterface.ts

- index.tsx
    - The entry point for rendering your React app into the DOM.
- App.tsx
    - The main component that serves as the entry point for your React application. It may contain the main routing logic and the overall structure of your app
- AddCustomer.tsx
    - This is the component where user can add customers with all valid details
- Login.tsx
    - This is the component where user first need to login with his username and password 
- Logout.tsx
    - User will get success message after logout and link to navigate to login page again
- backendinterface.ts
    - In this file we have stored request URLs 


### React App flow
    - Index component will load for rendering your React app into the DOM.
    - App component will have all the routers to navigate to perticular component when component rendered. so here first login component will rendered
    - User will get login page on initial load. User must login with valid credentials provided below
        - username: admin
        - password: admin
    - Added validation if user is not existed or user entered invalid credentials.
    - after successfull login user will get token storing token in localstorage for further operation.
    - Next page user can add customers with valid data. if user provide invalid data throwing error messages.
    - Added validation for empty fields 
    - Added validation for duplicate email id and invalid email format
    - Added validation for invalid phone number format 
    - User will provide valid data of customers and save the data into db after solving all errors
    - User can safely logout from page with token .




