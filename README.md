# MachLeData-Project
Develop a web app that displays data science job salaries and uses a machine learning model to predict a user’s net income based on key indicators.
Dataset: [Data Science Salaries from Kaggle](https://www.kaggle.com/datasets/sazidthe1/data-science-salaries)

back-end: code for back-end of the MachLeData project<br>
front-end: code for front-end of the MachLeData project<br>
model: code for the model deployment<br>
postgres: development files for the postgres database and initialization of the database<br>
dockerconfig: docker-compose file for VM<br>
serverconfiguration: Reverse proxy configuration files for the server<br>


## Postgres configuration
In order to be able to connect to the postgres Docker container you have to configure the pg_hba.conf and postgresql.conf files.<br>
In the pg_hba.conf add: host    all             all             0.0.0.0/0               scram-sha-256 <br>
And in postgresql.conf add: listen_addresses = '*'<br>
After the two changes the database is available for connection.<br>

Additionally on the serverside open up the specific port for the database connection.<br>
