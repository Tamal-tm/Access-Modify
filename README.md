# Access-Modify
Traditional and Property way of accessing and modifying elements with the use of getter and setter methods for private and protected attributes in a class. 

It covers:

Public, Protected, and Private attributes

Getter and Setter methods

Property decorators for controlled access and modification

IN DETAIL:

1. Public Attributes

Accessible from anywhere in the program.

No special restrictions.

2. Protected Attributes (_attribute)

Indicated by a single underscore (_).

Intended for internal use (convention, not enforced).

Still accessible, but should not be modified directly outside the class.

3. Private Attributes (__attribute)

Indicated by a double underscore (__).

Python performs name mangling (_ClassName__attribute).

Cannot be accessed directly.

4. Getter and Setter Methods

Getter → Retrieve private data safely.

Setter → Modify private data with validation/control.

5. Property Decorators (@property)

Pythonic way to use getters and setters without explicit method calls.
