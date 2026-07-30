I have been working in the backend for now more than 2 years and setup APIs, wrote small automation using python and Linux bash and 
suddenly realised "why not create some projects to be able to relate my work"
So here is me trying to do some relatable projects and posting on github.

Typical Weather API app where we use a third party API to grab data.

For beginners, I did the following:

I first created a folder on vscode named myweatherapp and then following files as:

1. .env fiel for env variables
2. .gitignore  ## for not pushing my security credentials into github and make a joke of myself lol
3. app.py    ## Main app file in python format ofcourse. this is the MAIN app that is being built
4. cache.py    ## We intend to use redis for caching and so a dedicated code page for that
5. readme.md   ## me explaining my code and related magic
6. weather.py  ## app file in python format, this file is just used to fit in logic for talking to third party app in our case we are using "Visual Crossing"
7. requirements.txt is created as simple as "pip freeze > requirements.txt" on the terminal y navigating into the right directory


