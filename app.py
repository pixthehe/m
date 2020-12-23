from bottle import route, template, run
import praw

reddit = praw.Reddit(client_id='wl63O1RL45N4JQ',
                     client_secret='SLM_5hzJSFiEq_7gFGtIeDZvxESfnQ', 
                     password="devindrew12341",
                     user_agent='MemeAPI_Script',
                     username='DevinLittle-')

@route('/')
def hello_world():
    subreddit = reddit.subreddit("blursedimages")
    meme = subreddit.random()
    return template("<img src={{submission}}>",submission=meme.url)

run(host='10.0.0.79', port=8080, debug=True)
    