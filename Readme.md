
# SQL chart
Draw chart for any SQL queries


## What is this?
A simple web application to visualize data from any arbitrary SQL query.

## How it is working?
* set `DB_CONNECTION` string either in env variable or in `config` file
* Start the application by running `run.sh`. Visit 'http://127.0.0.1:8000/index.html'
* Enter the SQL query in the text box and submit.
* available columns in the data will be shown in UI. visualize the data by dragging columns into required axis. Also choose requied aggregation function for pivot table
* Entire state of the graph ( SQL, columns in each axis, aggregation function etc ) is stored in the URL ( in URL hash ) so that we can reload the page without loosing the data.

## How to run this
```bash
git clone https://github.com/harish2704/sql-chart
cd sql-chart
pip2 install -r requirements.txt --user
# Edit config file and set database connection url. For details, refer https://docs.sqlalchemy.org/en/latest/core/engines.html
./run.sh
```

## Screencast
![Screencast](https://github.com/harish2704/harish2704.github.io/blob/master/sql-chart/screencast.gif?raw=true "sql-chart quick usage")

[Watch video](http://bit.ly/2y0J8QL)

## Thanks
* Authors of pivottable ( https://github.com/nicolaskruchten/pivottable ). The UI code is shamelessly copied from one of the examples given in this project.
* Simple backed api server ( server.js ) is written in https://falconframework.org/.
* https://plot.ly/javascript/
