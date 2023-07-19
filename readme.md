# Instagram Bio Automatic Updater

***
# About:

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

Regardless of if you are running this code on a server or just for fun on your PC for a bit, first you need to create a env file in the project directory. If you fork this repository, don't commit this env file unless you want others to know your Instagram login.

```
USER=your username
PASS=your password
```
If you aren't putting this on a server, then just run the Python file with the requirements installed and you will see the automated browser pop up and hopefully work! If you are putting this on a server, it is probably better to use Docker. In order to have this work within a Docker container first SSH into your server. From here you only need to type the following commands:

```
1: git clone https://github.com/Jamal135/Instagram_Bio       # Download the repository.
2: cd Instagram_Bio                                         # Enter the right directory.
# Create your .env file!
3: docker-compose up -d                                     # Start the program.
```

The up command makes the code start (building a container if none already exists) and the -d argument detaches it from the terminal. Here are some other useful commands that may help as well!

```
docker-compose down                                         # Kill the container gracefully.
docker-compose build                                        # Rebuild container if you make changes.   
docker ps -a                                                # See Docker stuff.
docker logs --follow instagram_bio_instagram_bio_1          # Follow code logs (^C to exit).
```

If the code is breaking through Docker, you can uncomment the port in the docker-compose.yml file. Then build and put the container up, navigate to that port in a browser (ip:4444), click sessions, and click the camera icon to see what is happening. WARNING: This is not behind authentication, anyone who goes to this port can fully control your Instagram account through the Selenium session. So make sure to comment this out again after testing and kill the Docker container used for testing.

Do note, you may also need to tell Instagram your new login is not suspicious before everything works.

***
# Acknowledgements:

McJeffr was an absolute legend and the Docker side of this project would of been impossible without them!
Link: https://github.com/McJeffr

A lot of StackOverflow posts certainly helped as well.

***
# Future:

I have no idea when this code might be permanently broken by Instagram changes. None the less I will work to fix bugs and make small improvements as I see fit. This has been a fun project and makes for a funny talking point when adding people on Instagram at parties!

***
# License:

MIT LICENSE.


