# Docstring is the way that most python files are documented.
# They are written in between triple quotes and can span multiple lines.
# They are usually placed at the beginning of a module, class, or function.
# There are a few popular styles for writing docstrings, including Google style and NumPy style.

# NOTE: There seem to be many ways to write docstrings. So it might just depend on the comapny and team you end up working for.

class GoogleStyleDocstring:
    """
    This is an example class to demonstrate docstrings.

    Attributes:
        attribute1 (str): Description of attribute1.
        attribute2 (int): Description of attribute2.
    """

    def __init__(self, attribute1, attribute2):
        """
        The constructor for GoogleStyleDocstring.

        Parameters:
            attribute1 (str): Description of attribute1.
            attribute2 (int): Description of attribute2.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def example_method(self, param1):
        """
        An example method that does something.

        Parameters:
            param1 (str): Description of param1.

        Returns:
            str: A description of the return value.
        """
        return f"Attribute1 is {self.attribute1} and param1 is {param1}"


class NumPyStyleDocstring:
    """
    This is an example class to demonstrate NumPy style docstrings.

    Attributes
    ----------
    attribute1 : str
        Description of attribute1.
    attribute2 : int
        Description of attribute2.
    """

    def __init__(self, attribute1, attribute2):
        """
        The constructor for NumPyStyleDocstring.

        Parameters
        ----------
        attribute1 : str
            Description of attribute1.
        attribute2 : int
            Description of attribute2.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def example_method(self, param1):
        """
        An example method that does something.

        Parameters
        ----------
        param1 : str
            Description of param1.

        Returns
        -------
        str
            A description of the return value.
        """
        return f"Attribute1 is {self.attribute1} and param1 is {param1}"