# Sort-It
Get the Sort it Bot! The Sort it bot categories your apps, by providing folder suggestions, for you and suggests apps that should be deleted based on past usage.

This was my submssion for the Sunhack 2021 Hackathon. The end prouct was created with the help of three other teamates.

# Inspiration
Apart from our college dorm, the send most disorganized this in a college student's life is the application on their phone or their laptop. Therefore, we built sort it!

# What it does
Sort it is a bot that runs on python and sorts any new applications downloaded to your phone based on how you previously have organized your folders. We utilized different Natural Language processing techniques such as stop word removal and keyword/category matching in order to determine the appropriate folder for an application. The bot also suggests applications that need to be deleted based on past activity.

# How we built it
We started by build two python scripts: one that categorized the files and the second that suggested what files had to be deleted. The data for categorizing the files were collected by scraping data from the App store.

For the front end, we built a basic HTML page and connected it to our python scripts using Django.

# Challenges we ran into
The biggest challenge we ran into was the fact that none of our teammates know how to use Django and had to learn the skill overnight.

# Accomplishments that we're proud of
We are extremely proud that we managed to implement Django in our code and complete all the main components of the MVP in such a short amount of time.

# What we learned
Time management and good communication were key to completing this project. We also discovered skills that we lacked or had to strengthen during this hackathon.

# What's next for Sort it!
Presently, Sort it is just a website. We aim to convert it into a complete bot that runs in their background on your phone and laptop and continuously collects data on how a user sorts their application. Eventually, we want the bot to be able to predict how the user sorts data and do it automatically as well as continuously collect data and learn user sorting preferences. We also plan to develop or utilize a more robust clustering algorithm such as kmeans to help partition apps into folder using user data.
