# Instagram Bio Automatic Updater

***
# About:
---
So long story short it was a cold hot winter in Australia and I decided my Instagram bio should update every hour for no reason. As a result, this repository was born. You might be asking why did I do this? The answer is simple. I don't know. None the less it is now here. If you use this, Instagram may decide you are a bot and permanently ban your account. So... it is super cool though and definitely worth the risk!

Currently the bio is updated with some cool text from the function below. Really you could make this put just about anything in your bio by modifying this function below to return a different string. The code will test every minute or so if new text doesn't match current text, if this evaluates as true it will update your bio. 

```python
def build_text():
    ''' Returns: Built Instagram biography string. '''
    current_time = datetime.now(pytz.timezone('Australia/Queensland'))
    hour = current_time.strftime("%I %p").replace(" ", "").lower().lstrip('0')
    day = calendar.day_name[current_time.weekday()]
    return f"Feels like {hour} on a {day} to me..."
```
Who knows maybe someone will do something really cool with this, goodluck!

Creation Date: 06/06/2022

***
# Setup:
---
Regardless of if you are running this code on a server or just for fun on your PC for a bit, the first thing you need to do is create a env file in the project directory. If you fork this repository, make sure you don't commit this env file to your repository unless you want others to log into your Instagram account.

```
USER=your username
PASS=your password
```
If you aren't putting this code on a server, then after doing that just run the Python file with the requirements installed and you will see the automated browser pop up and hopefully everything works! If you are putting it on a server, it is probably better to go the Docker direction! In order to have this work within a Docker container first SSH into your server. From here you only need to type the following commands:

```
1: git pull https://github.com/Jamal135/Instagram_Bio       # Download the repository.
2: cd Instagram_Bio                                         # Enter the right directory.
# Create your .env file!
3: docker-compose build                                     # Get everything ready.
4: docker-compose up -d                                     # Start the program.
```

The build command gets everything ready to go and will take a bit. The up command makes the code start and the -d argument detaches it from the terminal (so you don't see everything). Here are some other useful commands that may help as well!

```
docker-compose down                                         # Kill the code gracefully.
docker ps -a                                                # See Docker stuff.
docker logs --follow instagram_bio_instagram_bio_1          # Follow code logs (^C to exit).
```

If the code is failing in production and you want to investigate why, you can enable the commented out code in the docker-compose.yml file. Then re-build and put the container up, navigate to that port in a browser (ip:4444), click sessions, and click the camera icon. You can see and interact with the Selenium browser session and observe what is happening. Make sure to comment this out after troubleshooting as this is not behind any authentication meaning anyone else could access this as well. 

Do note, you may also need to tell Instagram your new login is not suspicious before everything works.

***
# Acknowledgements:
---
McJeffr was an absolute legend and I could not of done the Docker side of this project without them!
Link: https://github.com/McJeffr

A lot of StackOverflow posts certainly helped as well.

***
# Future:
---
I have no idea when this code might be permanently broken by Instagram changes. None the less I will work to fix bugs and make small improvements as I see fit. This has been a fun project and makes for a funny talking point when adding people on Instagram at parties!

***
# License:
---
MIT License.


