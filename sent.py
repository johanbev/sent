import csv

sent_words = {}


DEBUG = True
MAX_MULTIWORD_LENGTH = 2

with open('bafs-norsk.txt','r') as dat:
    reader = csv.reader(dat, delimiter='\t')
    for point in reader:
        sent_words[point[0]] = int(point[1])


def score_sentiment(string):
    lc = string.lower()
    words = lc.split()
    sent = 0
    activation = 0

    agenda = []

    for word in words:
        agenda.append(word)


    while len(agenda)>0:
        for i in reversed(range(1, MAX_MULTIWORD_LENGTH + 1)):
            mw = agenda[:i]
            word = ' '.join(mw)
            if word in sent_words:
                sent += sent_words[word]
                activation += abs(sent_words[word])
                agenda = agenda[i:]
            if i == 1 and word not in sent_words:
                agenda = agenda[1:]


    if(DEBUG):
        print("I:{} S:{} A:{}".format( string, sent, activation))

score_sentiment('Dette er det beste programmmet i python jeg noensinne har sett')
score_sentiment('FAP-maskinene er jævlige å jobbe med')
score_sentiment('Jævlig bra nei')