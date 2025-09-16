def array_of_names(a):
   return [f"{i.title()} {j.title()}" for i, j in a.items()]


persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
