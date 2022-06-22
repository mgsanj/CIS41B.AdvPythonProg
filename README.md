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







