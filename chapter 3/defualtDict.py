import sys
import re
import collections
import builtins


WORD_RE = re.compile('\w+')
    

index = collections.defaultdict(list)
fp = dict([('2','two'),('4','four'),('','')])
for line_no, line in enumerate(fp,1):
    for match in WORD_RE.finditer(line):
        word = match.group()
        column_no = match.start()+1
        location = (line_no, column_no)
        index[word].append(location)


for word in sorted(index, key=str.upper):
    print(word, index[word])
    # 2 [(1, 1)]
    # 4 [(2, 1)]
    # 5 [(3, 1)]


# better solution

WORD_RE = re.compile('\w+')
    

index = {}
fp = dict([('2','two'),('4','four'),('5','')])
for line_no, line in enumerate(fp,1):
    for match in WORD_RE.finditer(line):
        word = match.group()
        column_no = match.start()+1
        location = (line_no, column_no)
        index.setdefault(word,[]).append(location)
        # is the same as
        # if key not in my_dict:
        #         my_dict[key]=[]
        #         my_dict[key].append(new_value)

for word in sorted(index, key=str.upper):
    print(word, index[word])

# mapping with flexible key lookup
print('mapping with flexible key lookup')
d = {'one': 1, 'two': 2}
print(['one'])
print(d.get('one'))
print(d.get('three','yeganeh'))