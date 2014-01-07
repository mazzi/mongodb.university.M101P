db.zips.aggregate([{$project: { first_char: {$substr : ["$city",0,1]}, pop : 1 } }, { $match : { first_char : { $regex : '[0-9]' }} }, { $group : { "_id" : null, "total": { $sum : "$pop" } } } ])
