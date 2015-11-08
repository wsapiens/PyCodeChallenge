
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)


def test():

    # get a handle to the school database
    db = connection.students
    grades = db.grades

    query = {'type': 'homework'}
    remove_list = []
    prev_student_id = -1

    try:
        cursor = grades.find(query)
        cursor = cursor.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.DESCENDING)])
        for doc in cursor:
            print doc
            if prev_student_id != doc.get('student_id'):
                prev_student_id = doc.get('student_id')
            else:
                remove_list.append(doc)
        print '--------- remove list----'
        for doc in remove_list:
            print doc
            grades.remove(doc)

    except Exception as e:
        print "Unexpected error: {}".format(e)



test()


