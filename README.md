# Huduma-Mart :globe_with_meridians:

This is a team project that we built, as part of our portfolio project during our Software Engineering Programme. Our project aimed at addressing two of Africa's biggest problems namely, access to income and income generating opportunities. With this in mind, we hoped to bridge this gap by increasing the visibility and accessibility of the Africa's biggest workforce i.e the informal sector and effect the much needed technological disruption in this space. Our web application provides a platform for service providers to be more visible and accessibile to a vast network of potential clients all the while ensuring clients have a range service providers within their reach at any location and at any given time.

# Set up

### Clone the repository to your local terminal
```
git clone https://github.com/Bsakwa/Huduma-Mart.git
```

### Step 2: Set up your database

Assuming you already have a mySQL server installed and running, these commands will automatically create
the database. You might have to adjust your mysql password validation policies. 

```
cat huduma_db_setup.sql | sudo mysql 
cat huduma_db_setup.sql | mysql -u root -p
```

### Step 2: Populate your database with all the required objects for the project
```
HUDUMA_MYSQL_USER=huduma_dev HUDUMA_MYSQL_PASS=huduma_dev_pwd HUDUMA_MYSQL_HOST=localhost HUDUMA_MYSQL_DB=huduma_db HUDUMA_MYSQL_STORAGE=db ./fakecategories.py
HUDUMA_MYSQL_USER=huduma_dev HUDUMA_MYSQL_PASS=huduma_dev_pwd HUDUMA_MYSQL_HOST=localhost HUDUMA_MYSQL_DB=huduma_db HUDUMA_MYSQL_STORAGE=db ./fakelocations.py
HUDUMA_MYSQL_USER=huduma_dev HUDUMA_MYSQL_PASS=huduma_dev_pwd HUDUMA_MYSQL_HOST=localhost HUDUMA_MYSQL_DB=huduma_db HUDUMA_MYSQL_STORAGE=db ./fakeserviceproviders.py
HUDUMA_MYSQL_USER=huduma_dev HUDUMA_MYSQL_PASS=huduma_dev_pwd HUDUMA_MYSQL_HOST=localhost HUDUMA_MYSQL_DB=huduma_db HUDUMA_MYSQL_STORAGE=db ./fakeusers.py
HUDUMA_MYSQL_USER=huduma_dev HUDUMA_MYSQL_PASS=huduma_dev_pwd HUDUMA_MYSQL_HOST=localhost HUDUMA_MYSQL_DB=huduma_db HUDUMA_MYSQL_STORAGE=db ./fakereviews.py
```
* It is important to run these commands in the order they are listed inorder to observe the mapping and relationship rules between the database objects

### Step 3: CD into huduma-app directory to install the necessary dependencies for the project
```
npm install
```

### Step 4: Set up your Flask API to run in one terminal window
```
HUDUMA_MYSQL_USER=huduma_dev HUDUMA_MYSQL_PASS=huduma_dev_pwd HUDUMA_MYSQL_HOST=localhost HUDUMA_MYSQL_DB=huduma_db HUDUMA_MYSQL_STORAGE=db HUDUMA_API_HOST=0.0.0.0 HUDUMA_API_PORT=5000 python3 -m api.v1.app
```

* You can test API endpoints to be sure that everything works fine. This can be done using the curl command for example, in another terminal window
```
curl http://localhost:5000/api/v1/stats
curl http://localhost:5000/api/v1/locations
curl http://localhost:5000/api/v1/serviceproviders
curl http://localhost:5000/api/v1/categories
curl http://localhost:5000/api/v1/users
curl http://localhost:5000/api/v1/reviews
```

### Step 5: Run the huduma-app web application
```
npm start
```
* This command will run the app in development mode on http://localhost:3000

# Huduma-App Screenshots

* These are some of the pages that you should expect to see should the app launch without any problems and it should.

<p align="center">
  <img src="https://github.com/Bsakwa/Huduma-Mart/blob/main/assets/sc1.png"
       alt="scr">
</p>

---

<p align="center">
  <img src="https://github.com/Bsakwa/Huduma-Mart/blob/main/assets/sc2.png"
       alt="scr">
</p>

---

<p align="center">
  <img src="https://github.com/Bsakwa/Huduma-Mart/blob/main/assets/sc3.png"
       alt="scr">
</p>

---
<p align="center">
  <img src="https://github.com/Bsakwa/Huduma-Mart/blob/main/assets/sc4.png"
       alt="scr">
</p>

---
<p align="center">
  <img src="https://github.com/Bsakwa/Huduma-Mart/blob/main/assets/sc5.png"
       alt="scr">
</p>

---

* As you can see the project is still in it's MVP stage with the most important functionality already in place. The search and filter functionality which enables users to access service providers signed up on the platform. We are inviting collaborators so that we can take this great project a notch higher. The scope of the project remains big but we believe that if we do it one step at a time we will be on the verge of a long overdue technological disruption in Africa's informal sector. 

## Technical Challenges

Our project took us on a rollercoaster of wins and setbacks. There is still alot to be done but we might be limited in terms of the technical know how since we are still learning the ropes of Software Development. One significant challenge that we encountered in the course of building our web application was intergrating out API built in python to serve our front end built in Javascript. It works when we run our API from localhost but over a web server the browser `blocks loading mixed active content`. We were made aware that using Flask API for our REACT application was not the most sound approach based on the traditional stack approaches . LAMP, MERN or MERP ought and should be the guidelines. However, we built the project based on what we knew at the time and we will continue to do so whilst making the necessary trade offs. All the same we remain immensely proud of what we were capable of doing and we are looking forward to see the project grow and evolve in the future.


---
## :coffee: Buy us a coffee and support us in our journey

[![PayPal](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/donate/?hosted_button_id=WTJ7G8WQJZKKW)

Support us by buying a coffee! Click the PayPal icon above to make a donation directly to our PayPal accounts. Thank you

**Brian Sakwa:** `www.sakwabrian23@gmail.com`
**Myra Sukantet:** `myrasanaa17@gmail.com`
