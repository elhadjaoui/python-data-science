ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

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