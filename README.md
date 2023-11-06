# Model-API
This is our machine learning model exposed as an API using fastapi. This api code is written in python and is currently deployed using aws EC2 instance. 
The public url where this API is hosted is: http://52.66.196.169.
- Note: This url cannot be accessed through browsers because you have to do a post request and attach json data to the body with proper format.
- Browsers can only do HTTP Get requests not HTTP Post requests. The recommended way is to download and install a software like postman on your system.

Download postman here https://www.postman.com/downloads/

# How to use the model API
The link that I provided http://52.66.196.169. You have to do a `POST` request at that url and attach the required data in `proper format`. Web browsers cannot do `POST` requests they can only do `GET` requests so this link will not be accessible by the browser. \
In order to access the link you can install a software such as postman and follow the below steps:
- Set the method from get to post by clicking on get and selecting post from drop down menu
- Paste this URL http://52.66.196.169 in the url search bar
- Click on Body option select input type from Text to JSON and copy paste this input :-
```json
{
"teamA": 1000,
"teamB": 300,
"rankingdiff": 700,
"team_A_wins": 1
}
```
# `NOTE` 
```
Team_A_wins can only be 0 or 1.
1 means team A won 0 means it lost.
Rest 3 fields can be any number or even decimal number.
Also make sure that the rankingdiff is actually the difference of the ratings of teamA and teamB supplied in the above field.
It should work and return you with the predicted fluctuation.
```
