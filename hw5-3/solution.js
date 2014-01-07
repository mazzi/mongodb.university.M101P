db.grades.aggregate( [{ $unwind : "$scores" } , {$match : { "scores.type" : { $ne : "quiz" } }}, { $group : { _id : { "class" : "$class_id", "student" : "$student_id" }, avg : { $avg: "$scores.score" } } }, { $group : { _id : { "class" : "$_id.class" }, avg : { $avg : "$avg"} } } , { $sort : { avg : 1 } } ])

