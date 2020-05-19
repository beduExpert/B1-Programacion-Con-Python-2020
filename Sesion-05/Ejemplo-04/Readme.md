

## Conexión con bases de datos

### OBJETIVO

- Conectarse a una base de datos.
- Crear una tabla.
- Insertar datos en una tabla.
- Leer datos de una tabla.

#### REQUISITOS

1. Python 3 

#### DESARROLLO
SQLite en general, es una base de datos server-less que se puede utilizar en casi todos los lenguajes de programación, incluido Python. Server-less significa que no hay necesidad de instalar un servidor separado para trabajar con SQLite para que pueda conectarse directamente con la base de datos.

El SQLite3 connect es un método del objeto de conexión. Para ejecutar sentencias de SQLite3, primero se establece una conexión y luego se crea un objeto cursor utilizando el objeto.

En caso se que no exista el archivo .db, está sentencia lo crea.

Para crear una base de datos (y conectarse).
```
import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect(':memory:')

        print("Connection is established: Database is created in memory")

    except Error:

        print(Error)

    finally:

        con.close()

sql_connection()
```
El método execute de los objetos clase cursor nos permite usar sentencias SQL

Por ejemplo para crear una tabla:

```
import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

    con.commit()

con = sql_connection()

sql_table(con)
```
Para insertar datos en una tabla usamos INSERT:

```
import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_insert(con, entities):

    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    
    con.commit()

entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')

sql_insert(con, entities)
```
Para obtener los datos de una tabla podemos usar SELECT
```
import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)
```



