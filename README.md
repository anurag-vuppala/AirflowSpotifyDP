# AirflowSpotifyDP

This contain an Airflow dag that send a get request to spotify api and downloads the liked songs tracke list of the user. 

##token need to be changed for every run as it expires every 10 runs and the dag is set to run every 3 mins as the token ususally expires in 5 min if not used.

Steps to run:-

1) Activate the virtual environment -YTVM
2) Run Airldfow webserver 
3) Run Airflow scheduler
4)DONE!!! The dag is activated. CAn check the status in airflow scheduler terminal.

