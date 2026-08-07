# weatherapi_fastapi
This is a quick project to create a weather app using a third party data.This is built using python's FastAPI framework.
I was introduced to this project from roadmap:
https://roadmap.sh/projects/weather-api-wrapper-service

<h2>Quick info on the project</h2>

I have been working on the backend server side for around 3 years now, performing server maintenance, writing python API 
wrappers, bash scripting and setting up the infrastructure for data platforms using opensource tools on our environment.
I stumbled on this cool project and thought of creating one as its fun to set up such projects.

So here is a quick info on the files: so you will have to create few files which are part of the setting up the work setup when coding:
1. app.py - this is the main python application we are writing in this project
2. cache.py - this is because we are using redis for caching and so integrating the variables 
3. weather.py - this is our main API vendor that we are wrapping around and creating our own api from.essentially data is from them.

other files:
4. .env  : for storing sensitive data ofcourse
5. gitignore : for GIT to not push sensitive files entered into this file unto the github repository
6. you can do a pip freeze requirement to get requirements.txt later
7. As usual using a dedicated python env ceates a .venv folder 
