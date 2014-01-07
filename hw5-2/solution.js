db.zips.aggregate( [ { $match : { $or : [{"state" : "NY"}, { "state": "CA"}] } }, { $group : {_id : {st: "$state", ct :"$city"}, sum : { $sum : "$pop"}  } }, { $match : { "sum" : { $gt : 25000 } } }, { $group : {_id : "_id.st", avg : {$avg : "$sum"} } }  ]);


