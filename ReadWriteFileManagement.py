"""
    A class take care for the file management ( chats backup files ).
"""

NEW_LINE = "\n"
DATABASE_DIR_PATH = "databases/chat_db/"


def create_chat_file(name):
    import os
    file_name = DATABASE_DIR_PATH + "%s" % name
    if not os.path.exists(file_name):
        f = open(file_name, "x")


def add_data(filename, data):
    # open the file with 'append' option, and add the data to the end of the file.
    with open(DATABASE_DIR_PATH + filename, "a") as f:
        f.write(data + NEW_LINE)
