1) Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?
    LibraryItem provides a blueprint for child classes Books, Magazine and DVD. It is declared abstract because it enforces child classes to implement the abstract method. Here "late_fee" is an abstract method because it enforces child classes of LibraryItem to implement it.
    If late_fee() is missed to be implement in DVD it will return "TypeError" as it can't instantiate abstract class without abstract method implementation.

2) What happens when you read item.__available from outside the class, and why do we use is_available() instead?
    Variables starting with '__' will make Name Mangling automatically applied which appends class name before the variable name. So accessing item.__available outside the class will return an "AttributeError". Using is_available() will work because it is a function within the class which accesses this variables and returns the result.

3) What is the difference between LibraryItem.total_items and self.title?
    LibraryItem.total_items is a static variable common to all objects of the class "LibraryItem" and have a single location in memory so the value changed by one object will reflect to every other object.
    self.title is a non-static variable and is specific to the current object and can be accessed only by that object so the values differ.