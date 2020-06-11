import re
text = "random string"
mail =  "some random_string- . somerando dots 123abcdef@website.com"                                                                                              # or "ABCabc123@gmail.com"
check = re.compile("a random string")
check1 = re.compile("[rdm]")
che = re.compile("[a-zA-Z0-9]+") # + : 1 and more than one
e = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]")
d = re.compile("[a-zA-Z0-9\.\-\_\]+@[a-zA-Z0-9]+\.[a-zA-Z]")

result = check.search(text)                                            # search will only search for the 1st occurence
result1 = check1.search(text)
result2 = che.search(text)
resulte = e.search(mail)
res = d.findall(mail)
print(result) ; print(result1) ; print(result2) ; print(resulte) ; print(res)