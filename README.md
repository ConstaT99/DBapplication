### Project Null Description, Team #76 (this project is no longer maintance)

### Description:
Our project is a visual summary of wildfire incidents in California. Users are permitted to upload the wildfire pictures and their contact information. Prediction can be made according to the weather information and users will receive an alert email if the place they registered is predicted to have wildfires in near future.

### Usefulness: 
Wildfires often happened in California especially in summer. Compared to the summary websites that already exist, we can make predictions according to wildfire records and weather information. Also, users can upload the picture they took and give others a clear awareness of the circumstance .Furthermore, we will send an alert email to the users and let them be well prepared. 

### Realness:
California wildfire data: contains all incidents from 2013-2020 which can be downloaded from this url (https://www.fire.ca.gov/imapdata/mapdataall.csv) or queried through this url (https://www.fire.ca.gov/umbraco/api/IncidentApi/List?inactive=true).

Weather data: contains history weather data from 2013-2020 which can be downloaded from this url (https://www.climate.gov/maps-data/dataset/past-weather-zip-code-data-table or https://www.wunderground.com/history) 

Air quality data: queried through this url (https://registry.opendata.aws/openaq/)

Users’ data (personal info + fire pictures + alert preferences): inserted by our friends

### Basic Functions
**Insert:**

- Users signup: personal info

- Users insert alert preferences

- Users upload active wildfire pictures

- Periodically sync with California wildfire data and Weather data by inserting new wildfire incidents

- Predict counties that are highly possible to have a wildfire in the near future and alert associated users.

**Update:**

- Users update their personal info

- Users update alert preferences

**Delete:**

- Users delete their account

- Users delete alert preferences

- Users disable alert system

- Remove predicted counties

**Search:**

- Search by location

- Search by date

- Together with above searches, top liked wildfire pictures or most recent wildfire pictures will be popped up and the wildfire incidents will be rendered on map through map API.

### Advanced Function
**Advanced Function 1 (AF1):** Interactive Visualization

We will create an interactive map that details the start date, acres burned, and pictures about the wildfire and the weather there. When the wildfire is happening in some places, those placed will be marked as red. The red will be darker when the county has a high percentage of areas are contained in the wildfire. Also, we will allow users to report wildfires by uploading photos. The previews on the website will only show the latest 3 photos.


**Advanced Function 2 (AF2):** Prediction

We will crawl wildfires’ data from different websites and store them in the No-SQL database. Based on this data, we will develop an algorithm to detect which counties will have a wildfire shortly with high possibility. Then our website will send an alert to users who registered in those areas.

### Some links
Team page: https://wiki.illinois.edu/wiki/display/CS411AAFA20/Project+Null  
Project Detail Link: https://wiki.illinois.edu/wiki/display/CS411AAFA20/Project+Track+1

### Backend Tutorial

Checkout backend.py(backend/backend.py) for more details.

#### SQL

After running any command, it will ask you for the password: *teamnull*

Load github sql database into local database.

```
mysql -u root -p db < db.sql
```

Store your local database into a sql file.

```
mysqldump -u root -p --databases db > db.sql
```

#### Mongodb
Mac user need to setup alias in .bash_profile
```
alias monogodstart="< path of mongodb >/bin/mongod --dbpath <path of database folder> --logpath <path of log file> --fork"
```
- `alias` is creating a command that will run the code at right hand side of Equals sign
- `--fork` means running database at background process.
- `--dbpath` define the path of database. `--logpath` define the path of log file.

Then run `source ~/.bash_profile`(you might need to run this everytime you open you terminal)

`monogodstart` is the command will connect to local database.

If connect successfully you will see
```
about to fork child process, waiting until server is ready for connections.
forked process: 12345 (this is id for backgroud process)
child process started successfully, parent exiting
```
then
```
mongo
```
Command to shut down database
```
db.adminCommand({"shutdown":1})
```
