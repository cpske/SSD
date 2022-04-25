---
title: Resources for Database and Persistence
---

## Java

- [SQLite Java](https://www.sqlitetutorial.net/sqlite-java/) many tutorials on how to use SQLite with Java. Each tutorial covers a different topic, such as:
  - Connect to an SQLite database using JDBC
  - Create a new SQLite database
  - Create a new SQLite table
  - Insert data into a table
  - Download Sqlite-jdbc JAR: <https://mvnrepository.com/artifact/org.xerial/sqlite-jdbc> 
  - 

- [HyperSQL](https://hsqldb.org/) a fast, embeddable database written in Java. It has many datatypes and supports a large subset of the SQL standard.
  - Download JAR from SourceForge: <https://sourceforge.net/projects/hsqldb/files/>
  - Download JAR from Maven Repository: <https://mvnrepository.com/artifact/org.hsqldb/hsqldb>

- [Java Persistence API tutorial](https://medium.com/programming-geek/jpa-java-persistence-api-c93b648fc931) (JPA).  Simple explanation with code example.
  - to use JPA in a Java project you need (1) JPA JAR file containing the JPA standard classes and interfaces, (2) an implementation of JPA such as ORMlite, EclipseLink, or Hibernate (big), (3) a JDBC driver JAR for your database.

## Python

- [Data Management with Python, SQLite, and SQLAlchemy](https://realpython.com/python-sqlite-sqlalchemy/) on realpython.com
  - covers SQL basics, defining schema for SQLite, using SQLAlchemy for OR mapping (Books - Authors example), providing a service with Flask and REST.

- [Introduction to Python SQL Libraries](https://realpython.com/python-sql-libraries/) how to connection to an SQLite, MySQL, or Postgres database, and issue SQL commands in Python
  - each database requires a database-specific import and code to create a connection is slightly different for each database. This is unlike JDBC, where only the URL varies.

## Assignment

Write Python code to connect to a database, so that the application can connect to an SQLite, MySQL, or Postgresql database using the same code.

- define a factory for connections
- make the connection a singleton
- use the Bridge pattern for table creation?  connection creation?
  - abstraction is creating a table
  - implementation is the SQL commands to create a table for each database
