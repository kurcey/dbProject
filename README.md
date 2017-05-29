# dBProject:
 Answer the following questions fo the dbProject 2 in the Udacity fullstack web developer program:

* 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

* 2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

* 3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)



## Instructions and pre-requisite to run the program:

*    Load Udacity's vagrant virtual machine [here:](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
(this has the psql database running in the background) 

*    Downlad the data files [here:](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
 
*    On the running vagrant virtual machine in the folder that has the above downloaded file run the following from your psql command line (this will extract and instal the three news tables):
	psql -d news -f newsdata.sql
 
*    Switch to the directory that this README.md file is located

*    Run this code by typeing the following python 3 command:
	python3 dbProject.py

*    Bask in the beauty of the output!!!



## Description of program design:

The code works with the (unchanged) database schema from the lab description.The code is written in Python 3. It starts with a correct shebang line to indicate the Python version. The code presents its output in clearly formatted plain text. The code connects to and queries a SQL database. The code conforms to the PEP8 style recommendations. The SQL keywords written in UPPERCASE all the time. When the application fetches data from multiple tables, it uses a single query with a join, rather than multiple queries.



## SQL declarations:

	These answer the three qestions in the dbProject are declared as global varables in the program:
	1 mostPopularThreeArticles 
	2 mostPopularAuthors
	3 mostPopularAuthors



## Functions:
 *	Function used to connect to database "news"
		conect_db(database_name=DBNAME):
 *	Function to disconnect from database
		disconnect_db(database_connection):
 *	Function used to query database "news" with query passed as argument
		get_news(db_cursor, sqlQuery):
 *	Function used to iterated through results of query
		print_list(db_cursor, sqlQuery, Heading, lineEnding):



## Output of code:
'''
The most popular articles are: 
Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views

The most popular Authors are: 
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views

The days that we had more than 1% errors are : 
JULY      17, 2016 - 2.26% errors
'''
