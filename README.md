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
