
import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

db=connection.school
students = db.students

try:
    sort = [('scores.score', pymongo.ASCENDING )]
    my_grades = students.find().sort( sort )

    for one_grade in my_grades:
        current = {}
        current['score'] = ''
        for grade in one_grade['scores']:
            if grade['type'] == 'homework':
                if grade['score'] < current['score']:
                   current = grade

        one_grade['scores'].remove(current)
        students.update( { "_id" : one_grade['_id'] } ,one_grade)

except:
	print "Unexpected error:", sys.exc_info()[0]
