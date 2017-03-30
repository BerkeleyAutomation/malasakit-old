import environment
from pcari.models import UserData, QuantitativeQuestion, Rating, Comment, CommentRating
from django.contrib.auth.models import User
import numpy as np

def get_all_users():
    return User.objects.all()

def get_all_qr(u):
    rating_list = [-2]*8
    ratings = Rating.objects.filter(user=u)
    for r in ratings:
        rating_list[r.qid-1] = r.score
    return rating_list

def get_all_comment(u):
    comments = Comment.objects.filter(user=u)
    c = "--"
    if len(comments) > 0:
       c = comments[0].filipino_comment.encode('ascii','ignore')
    return [c]

def get_all_ratings_received(u):
    comments = Comment.objects.filter(user=u)
    if len(comments) > 0:
       c = comments[0].id
       recieved_ratings = CommentRating.objects.filter(cid=c, score__gte=0).values_list('score', flat=True)
       if len(recieved_ratings) > 0:
           return [np.mean(recieved_ratings), np.median(recieved_ratings), np.std(recieved_ratings), len(recieved_ratings)]
       else:
           return [-1, -1, -1, 0]
    else:
       return [-1, -1, -1, 0]


def get_demographics(u):
    users = UserData.objects.filter(user = u)
    if len(users) > 0:
       ud = users[0]
       return [ud.age, ud.barangay.encode('ascii','ignore'), ud.gender]
    else:
       return [-1, "--", "--"]

import csv
with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    row = ['id','Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Comment', 'Mean Rating', 'Median Rating', 'Std Rating', 'Num Rating', 'Age', 'Barangay', 'Gender']
    spamwriter.writerow(row)

    for i,u in enumerate(get_all_users()):
        row = []
        row.append(i)
	row.extend(get_all_qr(u))
	row.extend(get_all_comment(u))
	row.extend(get_all_ratings_received(u))
	row.extend(get_demographics(u))
        print(row)
        spamwriter.writerow(row)
