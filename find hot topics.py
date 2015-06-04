import os
txt_dir = './split/pgs/txt/'
files = os.listdir( './split/pgs/txt/' )

sentences = []
for fname in files:
    fpath = os.path.join( txt_dir, fname )
    with open( fpath ) as f:
        x = f.read().split('.')
        
        sentences += x

enum_sentences = list( enumerate( sentences ) )
sent_enum_dict = dict( [ (i,idx) for (idx,i) in enum_sentences ])
print len( sentences )


import collections
import re


sent_count = collections.Counter( sentences ).items()
sent_count.sort( key=lambda x: x[1], reverse=True )
long_count = [ i for i in sent_count if len( i[0] ) > 25 ]
idx = 1
for i in long_count:
    #if sentences[ sent_enum_dict[i[0]] - 1 ][1:]
    year = sentences[ sent_enum_dict[i[0]] - 1 ][1:]
    if re.match("[12]", year) != None:
        print "%s." % idx, i[0][1:]
        idx += 1
        print "Author(s):", sentences[ sent_enum_dict[i[0]] - 2 ][:]
        print "Year:", sentences[ sent_enum_dict[i[0]] - 1 ][1:]
        print "Citations: ", i[1]
        print
