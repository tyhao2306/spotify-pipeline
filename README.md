# spotify-pipeline
ETL pipeline that uses spotify API to get data about users listening history

Tools used in this project: Python,Airflow,Docker,Postgresql,Metabase

<img width="813" alt="Image" src="https://github.com/user-attachments/assets/4d199240-1031-4695-879e-3eb0736f352c" />

**Part 1: Spotify API**

To get my own user data from the spotify API, first login my account into spotify web api page and create a dashboard to create the client id ,client secret and Redirect URI. This is used to get the access token as well as the refresh token to request data from the API. After that is setup, using the recently_played endpoint we can call the recent 50 songs that were played on my account and store that data into a postgresql database. Second code is to add another column to the database which is the 'genre' column which gets the artist id for the songs in the database and matches it to the artist endpoint in the API to get the genre of the music as it is tied to the artist endpoint. 

**Part 2: Docker and airflow**

Docker was setup with requirements.txt, docker-compose.yaml and Dockerfile to set up the airflow, postgresql and metabase containers. Next the DAG schedules the order of execution for the two codes as well as the frequency of when it executes. The DAG is set to daily so any new song that i listen to is added every day. 

**Part 3: Metabase**

Metabase was used for data visualizations. It connects to the internal postgresql and also has its own version of sql. After query, the data can be visualized into tables and graphs for insights of the listening data.
