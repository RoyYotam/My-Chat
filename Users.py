import sqlite3

ERROR_1_PHONE_IN_USE = "This phone number is already in use."
ERROR_2_OTHER = "Other error."
CONFIRM_REGISTER = "Welcome to My Chat!"


class UsersDatabase:
    def __init__(self):
        self.con = sqlite3.connect("databases/Users.db")
        self.cur = self.con.cursor()
        self.validate_all()

    def validate_all(self):
        """
        The function checks all the SQl parameters are correct built.
        :return: None
        """
        self.cur.execute("CREATE TABLE IF NOT EXISTS Users(id number (10) primary key, password, chat_list [])")
        self.cur.execute("CREATE TABLE IF NOT EXISTS ContactCard(name, age integer, phone number (10) primary key)")
        self.con.commit()

    def new_user(self, phone, password):
        """
        Create a mew 'user' at Users table.
        :param phone: as a username.
        :param password: should be encoded with EncryptData, but there is no check for password.
        :return: None
        """
        self.cur.execute("INSERT INTO Users values(?, ?)", (phone, password))
        self.con.commit()

    def new_contact(self, name, age, phone):
        """
        Create a mew 'contact' at ContactCard table.
        :param name: the name will be displayed in chat.
        :param age: the user age.
        :param phone: as a username.
        :return: None.
        """
        self.cur.execute("INSERT INTO ContactCard values(?, ?, ?)", (name, age, phone))
        self.con.commit()

    def check_phone(self, phone):
        """
        The function checks whether this phone number in use or not.
        :param phone: representing the username.
        :return: boolean True/ False
        """
        result = self.cur.execute("SELECT * FROM ContactCard WHERE phone = %s" % phone)
        return result.fetchone() is None

    def register(self, phone, password, name, age):
        """
        A function register new user (including contact) if the phone number not in use.

        :param phone: as a username.
        :param password: should be encoded with EncryptData, but there is no check for password.
        :param name: the name will be displayed in chat.
        :param age: the user age.
        :return: a message of error / confirm, and the error code.
        """

        if self.check_phone(phone):
            self.new_contact(name, age, phone)
            self.new_user(phone, password)
            return CONFIRM_REGISTER, 0
        else:
            return ERROR_1_PHONE_IN_USE, 1

    def finish(self):
        self.cur.close()
        self.con.close()


if __name__ == "__main__":
    # Create interface
    userDatabase = UsersDatabase()

    # check if phone in use
    print(userDatabase.check_phone("1234567890"))

    # Try register new users.
    message, status = userDatabase.register("1234567890", "05123", "roy", 23)
    message2, status2 = userDatabase.register("1234567899", "05123", "roy", 23)

    print(message)
    print(message2)

    userDatabase.finish()


# TODO: connect
# TODO: connect chats to the user 'chat_list'
