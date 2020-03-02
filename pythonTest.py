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

	# tuples are immutable lists, declared w/ parenthesis 
	name_tuple = (first_names, another_list_of_names)

	print(some_guy, first_names, another_list_of_names, name_tuple)	
	# outputs Bill, ['Fred', 'George'] ['Fred', 'George']
	# this is because first_names and another_list_of_names are bound to the same list object

main()