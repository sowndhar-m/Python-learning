#Iterators 
#An iterators is an object that contains countable numbers of values.
#An iterator is an object that can be iterated upon meaning, that you can traverse through all the values.
#Iterator vs Iterable
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#Which consist of the methods _iter_() and _next_
#fruits = ["apple" , "Orange" , "kiwi"]
fruits = "apple"
f = iter(fruits)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))