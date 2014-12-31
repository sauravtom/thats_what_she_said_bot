from textblob.classifiers import NaiveBayesClassifier
import json

'''
train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
]
test = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]
arr = []

with open("twss.txt") as f:
    for i in f.readlines():
        d= {}
        d['text'] = i
        d['label'] = 'pos'
        arr.append(d)

with open("non_twss.txt") as f:
    for i in f.readlines():
        d={}
        d['text']=i
        d['label']='neg'
        arr.append(d)

with open("data.txt","w+") as f:
    f.write(json.dumps(arr))
'''

with open('train.json', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")

print cl.classify("Its huge and slimy.")


