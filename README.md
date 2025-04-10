# MachLeData-Project
Master

First Commit

## Postgres Docker container

In order to be able to connect to the postgres Docker container you have to configure the pg_hba.conf and postgresql.conf files.
In the pg_hba.conf add: host    all             all             0.0.0.0/0               scram-sha-256
And in postgresql.conf add: listen_addresses = '*'
After the two changes the database is available for connection.
