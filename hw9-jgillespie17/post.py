from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
POST = {
    "version": "2.0",
    "0": {
        "title": "HELP",
        "body": "javascript keeps destroying my webpage",
        "link": "true",
        "url": "https://www.google.com",
        "timestamp": get_timestamp(),
        "user_id": 1,
        "category_id": 0,
        "vote_count": 100
    },
    "1": {
        "title": "HELP(part 2)",
        "body": "CSS keeps destroying my webpage",
        "link": "true",
        "url": "https://www.google.com",
        "timestamp": get_timestamp(),
        "user_id": 1,
        "category_id": 0,
        "vote_count": 150
    },
    "2": {
         "title": "HELP(part 3)",
         "body": "HTML keeps destroying my webpage",
         "link": "true",
         "url": "https://www.google.com",
         "timestamp": get_timestamp(),
         "user_id": 1,
         "category_id": 0,
         "vote_count": "-150"
    }
}

# Create a handler for our read (GET) post
def read():
    """
    This function responds to a request for /api/post
    with the complete lists of POST

    :return:        sorted list of POST
    """
    print("Version : " + POST["version"])
    print(sorted(POST.keys()))
    # Create the list of people from our data
    return [POST[key] for key in sorted(POST.keys())]
