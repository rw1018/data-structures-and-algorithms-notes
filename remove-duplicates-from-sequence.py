#Remove duplicates from a sequence while maintaining order

#for hashable sequences
def deduplicate(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,1,2,1,3,4,2,3,5,7,3,12,8]
print(list(deduplicate(a)))

#deduplicate for unhashable types (such as dicts)

def deduplicate_hash(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]


print(list(deduplicate_hash(a, key=lambda d: (d['x'],d['y']))))
#[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]


print(list(deduplicate_hash(a, key=lambda d: d['x'])))
