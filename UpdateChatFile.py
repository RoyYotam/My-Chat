from datetime import datetime
import Users
import ReadWriteFileManagement

TIME_FORMAT = "<%d-%m-%Y %H:%M:%S>"


def update_file(chat_id, message):
    # Create interface
    user_database = Users.UsersDatabase()
    # Checks that the chat id is valid
    if user_database.check_chat(chat_id):
        ReadWriteFileManagement.add_data(str(chat_id), message)


def new_message_protocol(name, data, message_type):
    """
    A function create the message in the protocol to save in the chat backup.
    :param name: the name to display (who wrote the message).
    :param data: hold the message in the protocol.
    :param message_type: an integer, representing type of message (1 - user, 2 - Server).
    :return: The message at the protocol, encrypted.
    """
    return (str(message_type) + "" + current_time() + name + ": " + data).encode()


def current_time():
    """
    :return: The current time in custom format
    """
    return datetime.now().strftime(TIME_FORMAT)


if __name__ == "__main__":
    print(new_message_protocol("roy", "message", 1))
