#!/usr/bin/env python3
import psycopg2

# plSQL Query Definitions
mostPopularThreeArticles = (
    "select title, count(*) "
    "from articles, log "
    "where substring(path,10,length(path)) = slug "
    "group by title "
    "order by count(*) "
    "desc limit 3; ")

mostPopularAuthors = (
    "select name, count(*) "
    "from articles, log , authors "
    "where substring(path,10,length(path)) = slug "
    "and articles.author = authors.id "
    "group by author, authors.name "
    "order by count(*) desc ; ")

moreThanOnePercentError = (
    "select TO_CHAR(date(a.time), 'MONTH DD, YYYY') "
    ",ROUND((avg(numError)/ count(*) ) * 100 ,2) "
    "from log as a "
    "join "
    "(select date(time) as errDate "
    ",count(*) as numError "
    "from log "
    "where status like '%404%' "
    "group by date(time)) "
    "as eror on date(a.time) = eror.errDate "
    "group by date(a.time) having (avg(numError)/ count(*) ) * 100  >= 1 ;")


# Function used to query database "news" with query passed as argument
def get_news(sqlQuery):
    DBNAME = "news"
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sqlQuery)
    return c.fetchall()
    db.close()


# Function used to iterated through results of query
def print_list(sqlQuery, Heading, lineEnding):
    print(Heading)
    newList = (get_news(sqlQuery))
    for x in newList:
        print("%s - %s%s" % (x[0], x[1], lineEnding))
    print()


# main portion of program that is used to call functions
if __name__ == '__main__':
    print_list(
        mostPopularThreeArticles,
        "The most popular articles are: ",
        " views")
    print_list(
        mostPopularAuthors,
        "The most popular Authors are: ",
        " views")
    print_list(
        moreThanOnePercentError,
        "The days that we had more than 1% errors are : ",
        "% errors")
