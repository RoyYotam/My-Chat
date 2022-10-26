"""
    A class take care for the file management ( chats backup files ).
"""

NEW_LINE = "\n"
DATABASE_DIR_PATH = "databases/chat_db/"
FILE_APPEND = "a"
FILE_CREATE = "x"


def create_chat_file(name):
    """
    Create a new file in the given name, at the chat storage directory.
    :param name: the filename (include the file type if there is).
    :return: None.
    """
    import os
    file_name = DATABASE_DIR_PATH + "%s" % name
    # if the file already exist do nothing.
    if not os.path.exists(file_name):
        open(file_name, FILE_CREATE)


def add_data(filename, data):
    """
    Open the file with 'append' option, and add the data to the end of the file.
    :param filename: the filename (include the file type if there is).
    :param data: the data to append to the file.
    :return: None.
    """
    with open(DATABASE_DIR_PATH + filename, FILE_APPEND) as f:
        f.write(data + NEW_LINE)
