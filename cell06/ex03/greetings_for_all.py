def greetings(a=None):
  if a == None:
    print("Hello, noble stranger.")
  elif isinstance(a, (int, float)):
    print("Error! It was not a name.")
  else:
    print("Hello , ",a,".")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
