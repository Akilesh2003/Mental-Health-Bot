import praw
import os
import time
import random

reddit = praw.Reddit(
  client_id = os.environ['client_id'],
  client_secret = os.environ['client_secret'],
  username = os.environ['username'],
  password = os.environ['password'],
  user_agent = "<MHBot1.0>",
)

subreddit = reddit.subreddit("mentalhealth")
key_terms = ["sad", "depressed", "lonely", "nervous", "upset", "hurt",
            "miserable"]
quotes = ["You don’t have to control your thoughts. You just have to stop letting them control you — Dan Millman", "There is a crack in everything, that’s how the light gets in. ― Leonard Cohen", "It is not the bruises on the body that hurt. It is the wounds of the heart and the scars on the mind. — Aisha Mirza",
          "Mental health…is not a destination, but a process. It’s about how you drive, not where you’re going. — Noam Shpancer, PhD", "Happiness can be found even in the darkest of times, if one only remembers to turn on the light. — Albus Dumbledore", "Just because no one else can heal or do your inner work for you doesn’t mean you can, should, or need to do it alone. – Lisa Olivera", "Nothing can dim the light that shines from within. – Maya Angelou", "You, yourself, as much as anybody in the entire universe, deserve your love and affection. — Buddha", "You are valuable just because you exist. Not because of what you do or what you have done, but simply because you are. — Max Lucado", "I am not afraid of storms for I am learning how to sail my ship. – Louisa May Alcott", "Being able to be your true self is one of the strongest components of good mental health. – Dr. Lauren Fogel Mersy"
]

for comment in subreddit.stream.comments(skip_existing=True):
  if hasattr(comment, "body"):
    comment_lower = comment.body.lower()
    if any(word in comment_lower for word in key_terms):
      print(comment.body)
      comment.reply(body=random.choice(quotes))
      time.sleep(600)
  