# Midterms
## Midterm 1
Instructions: Explicitly answer each question with required features and functionality.  It is not necessary to include non-related code to the answer, as this makes the test harder to grade.  It is NOT required to write a complete program to answer the questions.  If you decide to include non-related code in your answer, please mark clearly where the explicit code is located so it can be easily graded. 

You are free to pick what methodology and design features your classes have.  Be sure the features match the requirements.  For example, choose the container, list, tuple or dictionary that best solves the problem.  You may also interpret the questions the way you think best, so it's not necessary for me to interpret the questions for you.

-----------------------------------------
### Question 1
Design a Product class to handle the data from the Product.csv file.  Here is an excerpt:

    Product,Price,Quantity
    Lemons,5.54,511
    Paprika,19.80,768
    Steak,20.49,199
    ...

Your class should support initialization, string conversion, sorting and searching.  Add additional functionality as needed.  Note:  writing the sort and the search functions is NOT required.

### Question 2
Design a Product Warehouse class to store the Products defined in question 1.  Add the ability to iterate over the products in the warehouse and support for indexing individual products in the warehouse.

### Question 3
Read the CSV data.  Store each Product data in a Product object and insert the Product object into Product warehouse.

### Question 4
Sort the Product Warehouse products by name.  Use the built-in Python sorting routines to sort the products.

### Question 5
Insert a Product object into an Sqlite database.  Assume the table in the database has been created.

## Midterm 2
Explicitly answer each question with required features and functionality.  It is not necessary to include non-related code to the answer, as this makes the test harder to grade.  It is NOT required to write a complete program to answer the question.  

If you do decide to include non-related code to your answer, please mark clearly where the explicit code is located so it can be easily graded.  Otherwise I may not find the code to be graded.

--------------------------------
### Question 1
Scrape this text file from:

https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt

Use BS4, Pandas or Regex to parse the data.  Here is an excerpt:


 year        decimal       monthly    de-season  #days  st.dev  unc. of </br>
 year          date         average     alized          of days  mon mean </br>
 1958    3   1958.2027      315.70      314.43     -1   -9.99   -0.99 </br>
 1958    4   1958.2877      317.45      315.16     -1   -9.99   -0.99 </br>
 1958    5   1958.3699      317.51      314.71     -1   -9.99   -0.99 </br>
 1958    6   1958.4548      317.24      315.14     -1   -9.99   -0.99 </br>
 1958    7   1958.5370      315.86      315.18     -1   -9.99   -0.99 </br>
 1958    8   1958.6219      314.93      316.18     -1   -9.99   -0.99 </br>
 1958    9   1958.7068      313.20      316.08     -1   -9.99   -0.99 </br>
 1958   10   1958.7890      312.43      315.41     -1   -9.99   -0.99 </br>
 1958   11   1958.8740      313.33      315.20     -1   -9.99   -0.99 </br>
 1958   12   1958.9562      314.67      315.43     -1   -9.99   -0.99 </br>
 
 
Save the data to a JSON string.

### Question 2
Write a Server that streams the Jason string from question1 to a Client defined in question3.

### Question 3
Write a Client that accepts a stream from the Server in question2.

### Question 4
The Client in question3, converts the stream from the Server in question2 into a dataframe.

### Question 5
Show how to run the Server in question2 and the Client from question3 on separate threads.


