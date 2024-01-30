import praw

# Initialisierung der Reddit API 
reddit = praw.Reddit(client_id='jMKrjZzhhZzQlCKTYT4C-g',
                     client_secret='hCoJLnr0CLUsIBPCvCfjLZXwbywjeA',
                     user_agent='con_taminada')

# Funktion, um die letzten X Posts in einem bestimmten Subreddit abzurufen
def get_last_posts_in_sub(subreddit_name, limit):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    
    for submission in subreddit.new(limit=limit):
        post_info = {
            'title': submission.title,
            'text': submission.selftext,
            'url': submission.url
        }
        posts.append(post_info)
    
    return posts


# Funktion, um die letzten X Posts zu einem bestimmten Thema in einem Subreddit abzurufen
def get_last_posts_by_topic_sub(subreddit_name, topic, limit):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    
    for submission in subreddit.search(topic, limit=limit):
        post_info = {
            'title': submission.title,
            'text': submission.selftext,
            'url': submission.url
        }
        posts.append(post_info)
    
    return posts


# Funktion, um die letzten X Posts zu einem bestimmten Thema in ganz Reddit abzurufen
def get_last_posts_by_topic_all(topic, limit):
    posts = []
    
    for submission in reddit.subreddit('all').search(topic, limit=limit):
        post_info = {
            'title': submission.title,
            'text': submission.selftext,
            'url': submission.url
        }
        posts.append(post_info)
    
    return posts


# Funktion zum Abrufen der letzten Beiträge eines bestimmten Users
def get_last_posts_by_user(username, limit):
    user = reddit.redditor(username)
    posts = []
    for submission in user.submissions.new(limit=limit):
        post_info = {
            'title': submission.title,
            'text': submission.selftext,
            'url': submission.url
        }
        posts.append(post_info)
    return posts


# Funktion zum Suchen nach einem Thema in den letzten Beiträgen eines bestimmten Users
def get_last_posts_by_user_topic(username, topic, limit):
    user = reddit.redditor(username)
    posts = []
    for submission in user.submissions.new(limit=limit):
        if topic.lower() in submission.title.lower() or topic.lower() in submission.selftext.lower():
            post_info = {
                'title': submission.title,
                'text': submission.selftext,
                'url': submission.url
            }
            posts.append(post_info)
    return posts


# Funktion zum Abrufen der letzten Beiträge eines bestimmten Users auf seiner Profilseite
def get_last_posts_by_user_on_profile(username, limit):
    user = reddit.redditor(username)
    posts = []
    for submission in user.submissions.new(limit=limit):
        post_info = {
            'title': submission.title,
            'text': submission.selftext,
            'url': submission.url,
            'subreddit': str(submission.subreddit)
        }
        posts.append(post_info)
    return posts


# Funktion zum Abrufen der letzten Beiträge eines bestimmten Users in einem bestimmten Subreddit
def get_last_posts_by_user_in_sub(username, subreddit_name, limit):
    user = reddit.redditor(username)
    posts = []
    for submission in user.submissions.new(limit=limit):
        if submission.subreddit.display_name.lower() == subreddit_name.lower():
            post_info = {
                'title': submission.title,
                'text': submission.selftext,
                'url': submission.url,
                'subreddit': str(submission.subreddit)
            }
            posts.append(post_info)
    return posts
