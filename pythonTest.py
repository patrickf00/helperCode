# reference about pythons use of objects --> https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/
# reference on tuples --> https://www.w3schools.com/python/python_tuples.asp

def main():
	# string object created and bound to some_guy
	some_guy = "Fred"
	# empty list object created and bound to to first_names
	first_names = []
	# empty list object is operated on
	first_names.append(some_guy)

	# another_list_of_names and first_names bound to same list object, ONLY 2 OBJECTS EXIST
	another_list_of_names = first_names
	# list object bound to another_list_of_names is operated on
	another_list_of_names.append("George")
	# a new string object created and bound to some_guy
	some_guy = "Bill"

	print("List: ", some_guy, first_names, another_list_of_names, "\n")	
	# outputs Bill, ['Fred', 'George'] ['Fred', 'George']
	# this is because first_names and another_list_of_names are bound to the same list object
######################################################################################################################################################################## tuples

	# tuples are immutable lists, declared w/ parenthesis 
	# can be accessed like list
	another_name = "Todd"
	name_tuple = (some_guy, another_name)
	print("Tuple: ", name_tuple, name_tuple[0], "\n")
######################################################################################################################################################################## sets

	# sets: unordered unindexed list, cannot access individual index usint set[i]
	# declared w/ curly brace
	# cannot chnage objects in set once declared but can add objects
	name_set = {some_guy, another_name}
	print("Set: ", name_set)
	for x in name_set:
		print(x) 
	print("\nFred in set: ", "Fred" in name_set)
	name_set.add("Hank")
	print("Hank in set: ", "Hank" in name_set)
	name_set.update(["Will", "Olive", "Cheese"])
	print("\nUpdated Set: ")
	for x in name_set:
		print(x)
	print("\nLength of set: ", len(name_set))
	name_set.remove("Cheese")
	print("Length of set after removal: ", len(name_set))
	# set.remove() will raise error if object doesnt exist, can use set.discard() and will not raise error if object not in set
	# can use pop() to remove last object, but because of nature of set, will be random
	# clear() clears content of set, del() deletes set completely
	# set3 = set1.union(set2) creates new set w/ content of both sets

######################################################################################################################################################################## dictionaries
	# disctionaries: unordered, changable and indexed
	# has keys and values
	testDic = {
		"name": "Patrick",
		"age": 24,
		"major": "compsci"
	}
	print("\nDictionary: ", testDic)
	# access values --> use keys
	x = testDic["age"]
	print("Age: ", x)
	x = testDic.get("name")
	testDic["name"] = "Haquah"
	print("Name: ", x, "\n")
	for x, y in testDic.items():
		print(x, ": ", y)



main()