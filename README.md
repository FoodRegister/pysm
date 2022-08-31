# pysm / Python Syntax Manager

This project aims to enhance python with a tool to enhance the default syntax to allow for more complex projects that may involve new syntaxes like the implementation of JSX in python.

# disclaimer

This project is still under developpement and I must stay that it might not be entirely stable. But if you plan on using it in production, you might want to check if the compiled code is equivalent to the code you wanted to do without the extension. If so, it is completely safe to use it in production because the release will always compile your code in a same way. But there might be issues i did not see or there might be a problem in your configuration. And in this case, you might have issues of collisions between the syntax you want to implement and an existing python syntax

# Zeus

Zeus is the main tool you should use if you are starting to use pysm. It includes many rules component, deriving from the base component of the Chronos router

# Chronos

Chronos is the low level part of pysm, it uses basic rules to allow for complex syntaxes and handles import routing and import state matching, it has only one basic component, which is the building block for all the components in the Zeus syntax framework
