def make_hashtable(size):
    table = []
    for unused in range(0, size):
        table.append([])
    return table

def find_bucket(htable,key):
    bucket = hashtable_get_bucket(htable, key)
    i=0
    for entry in bucket:
        if entry[0] == key:
            return bucket,i
        i+=1
    return bucket,None

def hashtable_update(htable, key, value):
    bucket,i = find_bucket(htable,key)
    if i!= None:
        bucket[i][1] = value
        return
    bucket.append([key, value])

def hashtable_lookup(htable, key):
    x,i=find_bucket(htable,key)
    if i!= None:
        return x[i][1]
    return i

def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]


table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print hashtable_lookup(table, 'Python')
