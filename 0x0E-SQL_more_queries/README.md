# SQL Queries Project

This project includes a set of SQL scripts and queries designed to perform various tasks on a MySQL server using the provided specifications.

## Table of Contents

1. [My Privileges](#1-my-privileges)
2. [Root User](#2-root-user)
3. [Read User](#3-read-user)
4. [Always a Name](#4-always-a-name)
5. [ID Can't be Null](#5-id-cant-be-null)
6. [Unique ID](#6-unique-id)
7. [States Table](#7-states-table)
8. [Cities Table](#8-cities-table)
9. [Cities of California](#9-cities-of-california)
10. [Cities by States](#10-cities-by-states)
11. [Genre ID by Show](#11-genre-id-by-show)
12. [Genre ID for All Shows](#12-genre-id-for-all-shows)
13. [No Genre](#13-no-genre)
14. [My Genres](#14-my-genres)
15. [Only Comedy](#15-only-comedy)
16. [List Shows and Genres](#16-list-shows-and-genres)
17. [Not My Genre](#17-not-my-genre)
18. [No Comedy Tonight](#18-no-comedy-tonight)
19. [Rotten Tomatoes](#19-rotten-tomatoes)
20. [Best Genre](#20-best-genre)

## 1. My Privileges

[Script: 0-privileges.sql](./0-privileges.sql)

Task Description: Display privileges for MySQL users 'user_0d_1' and 'user_0d_2' on the localhost server.

...

## 20. Best Genre

[Script: 103-rating_genres.sql](./103-rating_genres.sql)

Task Description: List all genres in the database 'hbtn_0d_tvshows_rate' by their rating.

...

## Usage

To execute any of the scripts, you can use the following command format:

```bash
$ cat script_name.sql | mysql -hlocalhost -uroot -p [database_name]

## 1. My Privileges

[Script: 0-privileges.sql](./0-privileges.sql)

Task Description: Display privileges for MySQL users 'user_0d_1' and 'user_0d_2' on the localhost server.

...

## 20. Best Genre

[Script: 103-rating_genres.sql](./103-rating_genres.sql)

Task Description: List all genres in the database 'hbtn_0d_tvshows_rate' by their rating.

...

## Usage

To execute any of the scripts, you can use the following command format:

```bash
$ cat script_name.sql | mysql -hlocalhost -uroot -p [database_name]

Replace script_name.sql with the desired script and [database_name] with the relevant database name.
Author

[Adegboyega Ademola]
