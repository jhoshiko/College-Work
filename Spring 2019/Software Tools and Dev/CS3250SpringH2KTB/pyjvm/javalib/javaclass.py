"""This module emulates a Java class."""


class JavaClass:
    """
    This class serves to emulate a java class for the java library.

    Attributes:
        methods:            The methods within a java class.
        fields:             The fields within a java class.
        attributes:         The attributes within a java class.
        instance_fields:    The instance fields within a java class.
        file_path:          The directory path to the java class.
        class_name:         The name of the java class.
        static_initialized: The status of whether or not a class is static.
        initialized:        The status of initialization for a java class.
    """
    def __init__(self):
        """The constructor for JavaClass class."""
        self.methods = []
        self.fields = []
        self.attributes = []

        self.instance_fields = {}
        self.file_path = None
        self.class_name = 'java/lang/Object'
        self.static_initialized = False
        self.initialized = False

    def name(self):
        """Returns class_name."""
        return self.class_name

    def python_initialize(self, *args):
        """This function has yet to be implemented."""
        pass

    def __repr__(self):
        """This function formats the name and instance fields for a class."""
        return '<{} - {}>'.format(self.name(), self.instance_fields)

    def get_field(self, name):
        """
        This function fetches fields from a class.

        :param name:                    The name of the field to be fetched.
        :return instance_fields[name]:  The fetched field.
        """
        return self.instance_fields[name]

    def set_field(self, name, value):
        """
        This function instantiates the values of a field.

        :param name:    The name of the field.
        :param value:   The value to be added to the field.
        """
        self.instance_fields[name] = value

    def has_method(self, name, desc):
        """This function has yet to be implemented."""
        return False

    def run_method(self, name, desc, frame):
        """This function has yet to be implemented."""
        pass

    def run_static(self, name, desc, frame):
        """This function has yet to be implemented."""
        pass
