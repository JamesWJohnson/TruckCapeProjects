#!/usr/bin/env python3

# This is called an import statement. It allows us to bring code written by
# other people into our program.
from hv_networks import J1708Driver

# We could have written "import hv_networks" and then referred to the J1708Driver
# module as hv_networks.J1708Driver , but this allows for less typing.


# J1708Driver is a module, and it contains a class called J1708Driver. To get a
# J1708Driver that we can use, we have to instantiate the class

driver = J1708Driver.J1708Driver(J1708Driver.ECM)

# The J1708Driver.ECM argument tells the driver class which J1708 interface we
# want to communicate with. In practical usage, you'll probably always want that one.


#Here we are going to read 10 messages.
for i in range(10):
    # driver is an instance of a class; to do things with it we need to call a
    # method of the instance. A method is a function that is a part of the instance
    # that can access data in the instance and make the instance do things.

    # To call an instance method, write instance_variable.method_name(<arguments>)
    # Here, declare a variable called msg. Set the value to be the result of a
    # call to a method of driver called "read_message" with the arguments checksum=False
    # and timeout=0.5
    # Then, print the variable msg

    msg = driver.read_message(checksum=False, timeout=0.5)
    print(msg)

    # checksum=False is called a "named argument." It tells the driver not to include
    # the checksum byte at the end of the message. timeout=0.5 tells the driver to wait
    # 0.5 seconds to receive a message before giving up. If we set it to 0 it would give
    # up immediately; if we set it to None it would wait forever.

