
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)


def test():

    # get a handle to the school database
    db = connection.school
    students = db.students

    # { "_id" : 39, "name" : "Mariette Batdorf", "scores" :
    #     [
    #         { "type" : "exam", "score" : 0.04381116979284005 },
    #         { "type" : "quiz", "score" : 90.25774974259562 },
    #         { "type" : "homework", "score" : 65.88612319625227 },
    #         { "type" : "homework", "score" : 16.40598305673743 }
    #     ]
    # }

    query = {'scores.type': 'homework'}
    remove_list = []
    prev_student_id = -1

    try:
        cursor = students.find(query)
        cursor = cursor.sort([('_id', pymongo.ASCENDING)])
        for doc in cursor:
            print doc
            prev_score = None
            scores = doc.get('scores')
            for score in scores:
                if score.get('type') == 'homework':
                    print score
                    if not prev_score:
                        prev_score = score
                    else:
                        if prev_score.get('score') > score.get('score'):
                            scores.remove(score)
                        else:
                            scores.remove(prev_score)
            print doc
            students.update({'_id': doc.get('_id')}, {'$set': {'scores': scores}})

    except Exception as e:
        print "Unexpected error: {}".format(e)



test()


