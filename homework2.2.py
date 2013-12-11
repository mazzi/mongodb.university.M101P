
import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

db=connection.students
grades = db.grades    

try:
	query = { 'type' : 'homework' }
	sort = [('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING )]
	my_grades = grades.find( query ).sort( sort )

	current = ''
	for one_grade in my_grades:
		if one_grade['student_id'] != current:
			grades.remove(one_grade)
			current = one_grade['student_id']
        
except:
	print "Unexpected error:", sys.exc_info()[0]
