#!/usr/bin/env python3
import psycopg2
import sys

DBNAME = "news"

# plSQL Query Definitions
mostPopularThreeArticles = (
    "SELECT title, COUNT(*) "
    "FROM articles, log "
    "WHERE SUBSTRING(path,10,length(path)) = slug "
    "GROUP BY title "
    "ORDER BY COUNT(*) "
    "DESC LIMIT 3; ")

mostPopularAuthors = (
    "SELECT name, COUNT(*) "
    "FROM articles, log , authors "
    "WHERE SUBSTRING(path,10,length(path)) = slug "
    "AND articles.author = authors.id "
    "GROUP BY author, authors.name "
    "ORDER BY COUNT(*) DESC; ")

moreThanOnePercentError = (
    "SELECT TO_CHAR(date(a.time), 'MONTH DD, YYYY') "
    ",ROUND((AVG(numError)/ COUNT(*) ) * 100 ,2) "
    "FROM log AS a "
    "JOIN "
    "(SELECT DATE(time) as errDate "
    ",COUNT(*) AS numError "
    "FROM log "
    "WHERE status LIKE '%404%' "
    "GROUP BY DATE(time)) "
    "AS eror ON DATE(a.time) = eror.errDate "
    "GROUP BY DATE(a.time) HAVING (AVG(numError)/ COUNT(*) ) * 100  >= 1 ;")


# Function used to connect to database "news"
def conect_db(database_name=DBNAME):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Unable to connect to Database %s" % database_name)
        sys.exit(1)


# Function to disconnect from database
def disconnect_db(database_connection):
    try:
        database_connection.close
    except:
        print("Unable to disconnect from Database %s" % database_connection)
        sys.exit(1)


# Function used to query database "news" with query passed as argument
def get_news(db_cursor, sqlQuery):
    db_cursor.execute(sqlQuery)
    return db_cursor.fetchall()


# Function used to iterated through results of query
def print_list(db_cursor, sqlQuery, Heading, lineEnding):
    print(Heading)
    newList = (get_news(db_cursor, sqlQuery))
    for x in newList:
        print("%s - %s%s" % (x[0], x[1], lineEnding))
    print()


# main portion of program that is used to call functions
if __name__ == '__main__':
    db_connection, db_cursor = conect_db("news")
    print_list(
        db_cursor, mostPopularThreeArticles,
        "The most popular articles are: ",
        " views")
    print_list(
        db_cursor, mostPopularAuthors,
        "The most popular Authors are: ",
        " views")
    print_list(
        db_cursor, moreThanOnePercentError,
        "The days that we had more than 1% errors are : ",
        "% errors")
    disconnect_db(db_connection)
