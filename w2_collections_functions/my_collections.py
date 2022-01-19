#*****************************
#     СПИСКИ И КОРТЕЖИ
#*****************************

#animals = ['cat1', 'cat2', 'axolotle', 'zebra', 'good dog', 'Forest cat']

#for number, animal in enumerate(animals):
#    print(f'#{number} is {animal}')

#print(min(animals))
#print(max(animals))
#print(sum(animals))

#print(', '.join(animals))
#print(sorted(animals))
#print(sorted(animals, reverse=True))


#import random
#import statistics

#numbers = []
#numbers_count = random.randint(10, 100)

#for _ in range(numbers_count):
#    numbers.append(random.randint(1, 50))

#print(numbers)
#numbers.sort()
#print(numbers)

#median_1 = None
#median_2 = None
#if numbers_count % 2 == 1:
#    median_1 = numbers[numbers_count // 2]
#else:
#    median_1 = sum(numbers[(numbers_count // 2) - 1: (numbers_count // 2) + 1]) / 2

#median_2 = statistics.median(numbers)

#print(f'median 1: {median_1}')
#print(f'median 2: {median_2}')

#*****************************
#         СЛОВАРИ
#*****************************

#from collections import Counter
#import operator

zen = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

#zen_map = dict()

#for word in zen.split():
#    clear_word = word.strip(',.-!').lower()

#    if clear_word not in zen_map:
#        zen_map[clear_word] = 0

#    zen_map[clear_word] += 1

#zen_items = zen_map.items()
#word_count_item = sorted(
#    zen_items, key=operator.itemgetter(1), reverse=True
#)
#print(word_count_item[:3])

#cleaned_list = []
#for word in zen.split():
#    cleaned_list.append(word.strip(',.-!').lower())

#print(Counter(cleaned_list).most_common(3))

#*****************************
#          МНОЖЕСТВА
#*****************************

#import random

#odd_set = set()
#even_set = set()

#for n in range(10):
#    if n % 2:
#        odd_set.add(n)
#    else:
#        even_set.add(n)

# union_set = odd_set.union(even_set)
#union_set = odd_set | even_set
#print(union_set)

# intersection_set = odd_set.intersection(even_set)
#intersection_set = odd_set & even_set
#print(intersection_set)

# difference_set = odd_set.difference(even_set)
#ifference_set = odd_set - even_set
#print(difference_set)

# symmetric_difference_set = odd_set.symmetric_difference(even_set)
#symmetric_difference_set = odd_set ^ even_set
#print(symmetric_difference_set)

#random_set = set()

#while True:
#    number = random.randint(1, 100)
#    if number in random_set:
#        break
#    random_set.add(number)


#print(random_set)
#print(len(random_set))
