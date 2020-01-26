# Pullit

Pullit is a real-time credential finder. 

<img src="https://i.imgur.com/PUx1oiG.png">

### Installation

- ``` git pull https://github.com/filtration/pullit.git ```
- ``` sudo chmod +x install.sh  ```
- ``` . ./install.sh ```
- ``` cp config.example.yml config.yml ```
- Edit your metadata or add more, then run:
- ``` python ./pullit.py  ```



### Features

- Find Github credentials
- Save credentials to database
- Post credentials to slack

### Modules:

- Github
- Bitbucket (todo)
- Gitlab (todo)


### todo:


- Rate limiting:
    - Check current token's rate limit
    - If it has expired, move on to the next token
    - If all tokens are rate-limited, print a message "We recommend you create and add another token"
- Email notifications
- Credentials:
    - Use selector to show just the credentials rather than (twitter_api_key=12345), because we can use 'name' column in database 
    - merge the credentials together, api_key=(...) api_secret(...)
- Database:
    - Better database management, don't run queries individually, run in bulk...
    - Check if repo has already been checked
    - Add commit id to database