#LFG API(WIP)

## Description
A project based on an API with the purpose to search a party to play videogames.
People who like videogames can find a party to play their favorite games with people, 
because all of us know that: _**It's dangerous to go alone, take this API.**_

The Gamers(users) can register on the app, and immediately they can search a party 
and start sending messages with the other gamers to play.


The basic endponits of the API are:

**/register** -> The user can register to start using the API.

**/login** -> The user can log in to the API.

**/videogames** -> Here shows the list of the videogames in the API and allows the user to create a new one.
Using the same endpoint but adding the name of the game will show the game you want to look for. (e.g **/videogames/Tetris/**)

**/parties** -> Same as videogames but for parties to join and pla with others.

**/party/id/messages** -> Here the messages of the party are displayed.

**/gamer/usernam**e ->  Here you can see your profile and modify it.

## Set up
All the packages needed for the API are in the document "requirements.txt" and can be installed using the command :

`pip -r install requirements.txt`

## Stack
The technologies used on this project are listed below:
* Python as a base programing language
* Django to complete Python
* Django Rest Framework for developing the API
* PostgreSQL as a database system 
* JWT for authentication
* Git
