ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

new_list = list(ft_tuple)
ft_list[1] = "World"
new_list[1] = "Morocco"
ft_tuple = tuple(new_list)
ft_set.discard("tutu!")
ft_set.add("Benguerir")
ft_dict["Hello"] = "1337"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# list are a python data type that is ordered and changeable.
# Allows duplicate members.
# tuple are a python data type that is ordered and unchangeable.
# Allows duplicate members.
# set are a python data type that is unordered and unindexed.
# No duplicate members.
# dictionary are a python data type that is unordered, changeable and indexed.
# No duplicate members.
