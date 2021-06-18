# P3 Web Error Battleship Site 
GitHub Repo for the Period 3 Web Error Team
# Links
- [Scrum Board with log of weekly changes](https://github.com/kylem314/p3-web-error-project/projects/1)
- [Project Plan](https://docs.google.com/document/d/1mxCPJsmhk86rFyu8uSxPnQBxzuSYuO-hp269rwPNfx8/edit)
- [Runtime Link](https://76.176.107.1)

# Creators & Heatmap Links
NAME             | GITHUB Link |
-------------    | -------------- |
Tyler Cloutier | https://github.com/GingerTC  |
Kyle Myint | https://github.com/kylem314 | 
Aidan Lin | https://github.com/aidanlin4 |
James Hunt   | you guys need to put your heat maps here |
Calvin Ni |https://github.com/statsprojectlol |

**Tickets**

| Kyle | James | Tyler | Aiden | Calvin |
| :---: | :---: | :---: | :---: | :---: | 
| [link](https://github.com/kylem314/p3-web-error-project/projects/1#card-57450505) | [link](https://github.com/kylem314/p3-web-error-project/projects/1#card-57450628) | [link](https://github.com/kylem314/p3-web-error-project/projects/1#card-57451796) | [link](https://github.com/kylem314/p3-web-error-project/projects/1#card-57451796) | [link](https://github.com/kylem314/p3-web-error-project/projects/1#card-57451412) |

**Umbrella ticket for P3 Web Error**

- [x] Database
- [x] Login System
     - [ticket](https://github.com/kylem314/p3-web-error-project/projects/1#card-61146210)
- [ ] Messaging System
- [ ] Battleship game
- [ ] Online multiplayer
- [ ] Leaderboard
- [x] API

# Project Scope

[Link to our project plan](https://docs.google.com/document/d/1mxCPJsmhk86rFyu8uSxPnQBxzuSYuO-hp269rwPNfx8/edit?usp=sharing)

**The Idea**
- A 1v1 battle ship game
- Online multiplayer interaction
- A point system where winning a game increases your points
    - users will be matched with other users with similar amount of points
- A leaderboard that displays users with highest amount of points
- A login system to create accounts on website
- Use of blueprints to format code

**College Board Requirements**
- Creative Development
    - Use web and program designs to create a plan for the project
    -Create Scrum Boards to track progress and development of the project
- Data
    - Using a SQLAlchemy database to save user information 
        - Use this information for user login
- Algorithms and programming
    - Use graphics/storyboard to plan the website design/UI 
    - Create design with HTML and CSS
- Computer Systems and Networks
    - Deploying website using a raspberry pi that runs 24/7
        - Internet domain
    - Using GET/POST
        - User information and login
        - Past game information
- Impact of computing
    - Website will not be used for illegal or malicious purposes
    - User credentials are secure and have protection from database leaks
    - Crediting work from first trimester to those who created that code

# How It's Made
## Theme Section (5 points)
- News page [web api](http://127.0.0.1:5001/news) (+.5 technical)
- [Messaging board](http://127.0.0.1:5001/MessageBoard) (+.5 technical +.5 user interaction +1 fun/creative)
- [Multiplayer battleship](http://127.0.0.1:5001/otherpage) (+.5 technical +.5 user interaction +1 fun/creative)
- Communicating through use of databases (+.5 user interaction)


## Individual Section
James Hunt
Calvin Ni
Kyle Myint
Technicals in Project


Minilabs
[Classes - Prime Number Check](https://github.com/kylem314/p3-web-error-project/blob/main/minilabs/kyleminilab/classes.py) 
[Classes minilab on live site])(76.176.107.1/kyleminilab/kyleclasses)
[Bubble sort](https://github.com/kylem314/p3-web-error-project/blob/main/minilabs/kyleminilab/bubblesort.py)
[Bubble sort on live site])(76.176.107.1/kyleminilab/kylebubblesort)

Tyler Cloutier
- Aidan Lin (5 points)
     - Labs (+2)
          - [Random Workout Generator Lab](https://github.com/kylem314/p3-web-error-project/tree/main/minilabs/aidanminilab/algo)
          - [Bubblesort Lab](https://github.com/kylem314/p3-web-error-project/tree/main/minilabs/aidanminilab/algo)
     - Technicals (+3)
          - Each minilab utilizes classes in order to pass in parameters that cause different functions to run
          - Minilabs uses jinja to store the output as "output" and display on the html page
          - [Bubblesort Lab](76.176.107.1/aidanminilab/bubblesort) demonstrates sorting of integers
          - [Bubblesort Lab](76.176.107.1/aidanminilab/bubblesort) also demonstrates sorting of strings in alphabetical order
          - [Random Workout Generator Lab](76.176.107.1/aidanminilab/) demonstrates pulling different workouts with a different output each time
          - [Rest API](https://github.com/kylem314/p3-web-error-project/tree/main/minilabs/calvinminilab/api) has CRUD operations and displays it on a [webpage](https://github.com/kylem314/p3-web-error-project/blob/main/minilabs/calvinminilab/api/crud.html) (I collaborated with Calvin on the API)

- James Hunt (5 points)
     -Labs (+2)
          - [Blueprint for battleship grid](https://github.com/kylem314/p3-web-error-project/blob/main/blueprints.py)
          - [Battleship grid](https://github.com/kylem314/p3-web-error-project/blob/d662ad5909352fe4b58a5c6ebe179f6f03d068b0/templates/otherpage.html#L80-L129)
          - [Also lots of minilab/playgorund code for learning](https://github.com/kylem314/p3-web-error-project/tree/main/minilabs/jamesminilab)
          - [Moving Image Lab Test](https://github.com/kylem314/p3-web-error-project/blob/main/templates/MovingImage.html)
          - [Moving Image lab test route](https://github.com/kylem314/p3-web-error-project/blob/d662ad5909352fe4b58a5c6ebe179f6f03d068b0/main.py#L103-L132) [and](https://github.com/kylem314/p3-web-error-project/blob/d662ad5909352fe4b58a5c6ebe179f6f03d068b0/main.py#L80-L90)
     -Technicals (+3)
          -[working home page](https://github.com/kylem314/p3-web-error-project/blob/main/templates/home.html)
          -[Working login system (made with Tyler)](https://github.com/kylem314/p3-web-error-project/blob/d662ad5909352fe4b58a5c6ebe179f6f03d068b0/main.py#L188-L236)
          -[Working User system + upgraded login syste,](https://github.com/kylem314/p3-web-error-project/blob/d662ad5909352fe4b58a5c6ebe179f6f03d068b0/main.py#L238-L269)
          -[Working Private messageing system](https://github.com/kylem314/p3-web-error-project/blob/d662ad5909352fe4b58a5c6ebe179f6f03d068b0/main.py#L238-L287)
          -[Working Multiplayer battleship](https://github.com/kylem314/p3-web-error-project/blob/d662ad5909352fe4b58a5c6ebe179f6f03d068b0/main.py#L188-L386) Do note Tyler made the try/execpt function in /blogin route
          -[More of Working Multiplayer battleship](https://github.com/kylem314/p3-web-error-project/blob/d662ad5909352fe4b58a5c6ebe179f6f03d068b0/main.py#L46-L61)
          -[More of Working Multiplayer battleship](https://github.com/kylem314/p3-web-error-project/blob/d662ad5909352fe4b58a5c6ebe179f6f03d068b0/templates/otherpage.html#L1-L179)
          -[Working User Page integrated with Database](https://github.com/kylem314/p3-web-error-project/blob/d662ad5909352fe4b58a5c6ebe179f6f03d068b0/templates/user.html#L1-L142)
          

## API Section (5 points)
- Rest API created [code](https://github.com/kylem314/p3-web-error-project/tree/main/minilabs/calvinminilab/api) (+2)
- Front end of API [code](https://github.com/kylem314/p3-web-error-project/blob/main/minilabs/calvinminilab/api/crud.html) (+1)
- Received API from another team [link](http://127.0.0.1:5001/crossoverapi) (+2)

## Deployment Section (5 points)
- [Commercial](https://youtu.be/HnA21yrnhtQ) (+2)
- How it’s made is the read.me (+2 and +1 visual/creativity)


# Mini Labs

Creator          | Blueprint Links|
-------------    | -------------- |
Tyler | [Blueprint](https://github.com/kylem314/p3-web-error-project/tree/main/minilabs/tylerminilab) |
Kyle | [Blueprint](https://github.com/kylem314/p3-web-error-project/tree/main/minilabs/kyleminilab) |
Aidan | [Blueprint](https://github.com/kylem314/p3-web-error-project/tree/main/minilabs/aidanminilab) |
James | [Blueprint](https://github.com/kylem314/p3-web-error-project/tree/main/minilabs/jamesminilab) |
Calvin | [Blueprint](https://github.com/kylem314/p3-web-error-project/tree/main/minilabs/calvinminilab) |

