# CIS41B.AdvPythonProg
## Lab 0 - Data Acquisition: (Lab0.py)
Using BeautifulSoup, scrape this website:
 
"https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"
 
Scrape the "List of countries by carbon dioxide emissions" for the data.  Use the functionality of Beautifulsoup to scrape the data.  Note that Pandas does have scraping abilities available, however, use the Beautifulsoup functionality for this assignment.  Scrape the column:  "2017 (% of world)".
Store the scraped data in a defaultdict.  To demonstrate your program successfully scraped the data, output your defaultdict to the monitor.

## Lab 1 - Databases: (Lab1.py, Co2.html, SeaLevel.csv)
Purpose:  Create and use a Database

Data Files: Use BS4, Regular Expressions or Pandas to read in the two data files for this assignment:

Co2.html:
<TBODY><TR><TD>2002</TD><TD>4</TD><TD>2002.292</TD>... <br/>
<TBODY><TR><TD>2002</TD><TD>5</TD><TD>2002.375</TD>... <br/>
<TBODY><TR><TD>2002</TD><TD>6</TD><TD>2002.458</TD>... <br/>
... <br/>

SeaLevel.csv: <br/>

2002.3797,3.43000,1.23000,, <br/>
2002.4069,1.13000,0.33000,, <br/>
2002.4340,-5.67000,-2.17000,, <br/>
...

Where necessary, reduce the data from either Monthly or Daily to Annual data.  Use Python iterators and reducers to handle converting the data to Annual data. Store the data in a Pandas Dataframe.
 
Database:

Store the Dataframes in an SQLite data base.  Design a class to interface to the SQLite database:

    class Database: <br/>
        def __init__(self): <br/>
            self.db = sqliteConnection() <br/>

            ...

and add functionality for table creation, inserting, searching and deleting entries in the database.  

An additional feature is to program an automatic "query_builder" that can build database queries for any database operation.  The QueryBuilder also needs to support any type of data that is required for the operation. Please refer to Sqlite.py example file for examples of building queries for different operations.

Usage:  Insert the Dataframes from the datafiles, or the dataframe data, into your Database.  Validate your Database operations by outputting the stored data.

## Lab 2 - Data Visualization (Lab2.py)

Scrape, using BeautifulSoup, this webpage:  

https://worldpopulationreview.com/country-rankings/pollution-by-country 

Scrape the table representing the list from "Pollution by Country 2022".  Write a function to take each country's data from the table and insert it into your SQLite database from lab1 country by country.  Extract the country data from the SqLite database and use MatPlotLib to plot the data into a Pie Graph.
 

## Lab 3 - Sockets (Lab3.py, Client3.py, UNData.xml)
Process: 
The user (client) requests data from the (server) database.  The database sends back the data to the user.  At acquisition of the data an XYPlot is drawn.

DataFile: 
UNData.xml

User Layer:
The user selects a country, and passes the country name to the Business Layer.  Use TKinter to produce a pull-down for the user to select a country. Send the selected country to the Business Layer.

Business Layer:
Receives the information from the User Layer and constructs a SQL query to send to the Data Layer.  The query extracts the yearly data (1990,2017) for the requested country.  The data may be queried either country year-by-year or in one query for year range.  After receiving the JSON string back from the Data Layer, send the data to the Graphic Layer for plotting.

Data Layer:
Construct a SQL Database based on the data from the DataFile.  Processes the queries from the Business Layer.   Sends back a JSON string for the requested query.  

Graphic Layer:
Use your Graphic Class or module defined in previous assignments to draw a MatPlotLib XYPlot.

Server Layer:
The database access is controlled by the Server Socket.  The client sends a query, and the server sends a JSON string.

Client Socket:
Requests data from the server.  After receiving the data from the server, the client displays the data.




