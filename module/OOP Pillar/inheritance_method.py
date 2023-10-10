class Parent:
    def say_hello(self):
        print("Hello from Parent")

class Child(Parent):
    def say_hello_from_child(self):
        print("Hello from Child")

# Create an instance of the child class
child_instance = Child()

# Call the inherited method from the child instance
child_instance.say_hello()  # Output: "Hello from Parent"

# You can also call the method from within other methods of the child class
child_instance.say_hello_from_child() 