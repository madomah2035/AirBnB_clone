# AirBnB Clone - The Console

## Project Goal

The primary goal of this project is to deploy a simplified version of the AirBnB website on a server. While not implementing all the features, it aims to cover fundamental concepts of the higher level programming track.

## First Step: Command Interpreter

The initial step involves building a command interpreter to manage AirBnB objects. This command interpreter is similar to a limited-use Shell, specifically tailored for our project's needs. It enables us to:

- Create new objects (e.g., User or Place)
- Retrieve objects from files or databases
- Perform operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

## Execution

The command interpreter can be used both interactively and non-interactively.

### Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
### Non-Interactive Mode
```bash

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Commands

- `create`: Create an object
- `show`: Show an object (based on id)
- `destroy`: Destroy an object
- `all`: Show all objects, of one type or all types
- `update`: Updates an instance based on the class name and id
- `quit/EOF`: Quit the console
- `help`: See descriptions of commands

# Getting Started

To start the console, type the following command in the shell:

```bash
AirBnB_clone$ ./console.py
(hbnb) 
```
# Object Management Commands

## Create

To create an object, use the format `create <class_name>`:

```bash
(hbnb) create BaseModel
```
## Show

To show an instance based on the class name and id, use:

```bash
(hbnb) show BaseModel 1234-1234-1234.
```
## Destroy

To delete an instance of an object, use:

```bash
(hbnb) destroy BaseModel 1234-1234-1234.
```
## All

To show all instances or all instances of a specific type, use:

```bash
(hbnb) all
(hbnb) all State
```

## Update

To update an instance based on the class name and id, use:

```bash
(hbnb) update BaseModel 1234-1234-1234 email "niyokwizerwajeanpaulelisa@gmail.com"
```

## Quit

To exit the console, use:

```bash
(hbnb) quit
```

## Help

To get help on commands, use:

```bash
(hbnb) help
(hbnb) help quit
```
# Supported Classes

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

# Authors

- `(Ndevu)` NIYOKWIZERWA Jean Paul Elisa - niyokwizerwajeanpaulelisa@gmail.com `linkedIn` - http://linkedin.com/in/jean-paul-elisa
- Musah Adomah - kwamemusah51@gmail.com
