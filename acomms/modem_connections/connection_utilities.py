import urllib

def connection_class_from_name(name):
    pass

def connection_from_string(connection_string):
    parsed = urllib.parse(connection_string)
    pass
    # Look at the scheme to decide what connection type to use.
