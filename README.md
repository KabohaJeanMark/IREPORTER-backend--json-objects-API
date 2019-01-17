

[![Build Status](https://travis-ci.com/KabohaJeanMark/IREPORTER2.svg?branch=develope)](https://travis-ci.com/KabohaJeanMark/IREPORTER2)
[![Maintainability](https://api.codeclimate.com/v1/badges/49bf7c17c87a537a1de3/maintainability)](https://codeclimate.com/github/KabohaJeanMark/IREPORTER2/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/KabohaJeanMark/IREPORTER2/badge.svg?branch=bug-coveralls-163284492)](https://coveralls.io/github/KabohaJeanMark/IREPORTER2?branch=bug-coveralls-163284492)

## About
iReporter gives all citizens a platfrom to raise concerns about corruption and corruption red-flag cases and the need for government intervention in situations.


## Features
1. Users can sign up.
2. Users can create incidents (red-flag records or intervention records)
3. Users can edit the locations and comments of their incidents.
4. Users can delete their incidents.
5. Administrators can update the statuses of these incidents. 

## Prerequisites
- A computer with an OS running python 3.6
- Gitbash installed to navigate between the branches.
- A preferred text editor for example VS Code.
- Postman to locally check the API endpoints acting as your application client. 
- Pytest, nosetest or a preferred python testing tool.

## How to install and deploy
Clone this project to your computer on yourFolder by typing these commands in the terminal.
```
$ mkdir yourFolder
$ cd yourFolder
$ git clone https://github.com/KabohaJeanMark/IREPORTER2
$ cd IREPORTER2
$ virtualenv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ python run.py
```
## Test your endpoints
Run the command in your virtual environment
```
$ pytest
```
## Deployment
The application is hosted on Heroku at https://kjmkireporter.herokuapp.com/api/v1/

## Endpoints
| Endpoints                                         | Functionality                       |                             
| --------------------------------------------------|:-----------------------------------:|
|```POST /api/v1/users```                           |Create a user                        |
|```POST /api/v1/redflags```                        |Create red-flag record               | 
|``` GET /api/v1/users```                           |Fetch all users                      |
| ```GET /api/v1/redflags```                        |Fetch all red-flag records           |
| ```GET /api/v1/redflags/<redflag_id>```           |Fetch a particular red-flag record   |                   
| ```DELETE /api/v1/redflags/<redflag_id>```        |Delete a specific red-flag record    |
| ```PATCH /api/v1/redflags/<redflag_id>/status  ```|Update a specific red-flag's status  |
| ```PATCH /api/v1/redflags/<redflag_id>/location```|Update a specific red-flag location  | 
| ```PATCH /api/v1/redflags/<redflag_id>/comment``` |Update a specific red-flag comment   | 


## Built using:
- Language : Python
- Framework : Flask

## Author
>Kaboha Jean Mark Kairumba.

>email: kabohajeanmark@gmail.com

## Licensing
The is an opensource application. All users are free to edit and improve it. Code away.

## Appreciation
Thank you ANDELA for the opportunity to learn new skills and improve with this bootcamp.
