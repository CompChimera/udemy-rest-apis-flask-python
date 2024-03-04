# Setup



## Using docker locally
TO setup the container `docker build -t flask-smorest-api .`

To run:
`docker run -dp 5000:5000 flask-smorest-api`

To mount the folder on Windows and use a volume:
`docker run -dp 5000:5000 -w /app -v %cd%:/app flask-smorest-api `





### Old
Create and activate the virtual environment
`python3.12 -m venv .venv`

Once you’ve created a virtual environment, you may activate it.

On Windows, run:
`.venv\Scripts\activate`

On Unix or MacOS, run:
`source tutorial-env/bin/activate`

To run app
`py -m flask run`