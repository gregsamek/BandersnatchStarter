# Bandersnatch Project
[Deployed App](https://bandersnatch.herokuapp.com)

### Tech Stack
- Logic: Python3
- API Framework: Flask
- Templates: Jinja2
- Structure: HTML5
- Styling: CSS3
- Database: MongoDB
- Graphs: Altair
- Machine Learning: Scikit
- Hosting: Heroku

### Primary Features by URL
- `/`: Splash Page
- `/data`: Tabular Data
- `/view`: Dynamic Visualizations
- `/model`: Interactive Machine Learning Model

### OS Specific Notes: Gunicorn is not Windows compatible!
- Windows users should not use the `run.sh` shell script, as it depends on gunicorn.
- Windows users should use `py -m app.main` to start the app with Flask acting as the server.
- Mac and Linux users can use `./run.sh` script or type the command directly `python3 -m gunicorn app.main:APP`.
- Feel free to modify the shell scripts to suit your needs, these are intended to run locally.
- In any case you should not modify the Procfile, this is the run script for the remote server.
