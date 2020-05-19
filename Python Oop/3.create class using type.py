#How to create a Class using type Keyword?

#The type keyword used to create a new class on the fly and then instantiate it.

e1 = type('Employee', (), {})()
print(e1)
 
e1.name = "John Doe"
print(e1.name)
