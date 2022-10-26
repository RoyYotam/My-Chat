import sqlite3

ERROR_1_PHONE_IN_USE = "This phone number is already in use."
ERROR_2_PHONE_DOES_NOT_EXISTS = "This phone number is not register yet."
ERROR_3_PASSWORD_INCORRECT = "Password is incorrect."
ERROR_4_CHAT_DOES_NOT_EXISTS = "This chat ID is incorrect."
CONFIRM_MESSAGE = "Welcome to My Chat!"


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
        self.cur.execute("CREATE TABLE IF NOT EXISTS Users(id number(10) primary key, password char(64), chat_list)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS ContactCard(name, age integer, phone number(10) primary key)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Chats(id integer, name, date, primary key (id))")
        self.con.commit()

    def new_user(self, phone, password):
        """
        Create a mew 'user' at Users table.
        :param phone: as a username.
        :param password: should be encoded with EncryptData, but there is no check for password.
        :return: None
        """
        self.cur.execute("INSERT INTO Users values(?, ?, ?)", (phone, password, ""))
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
        :return: boolean, True if exists / False otherwise.
        """
        result = self.cur.execute("SELECT * FROM ContactCard WHERE phone = %s" % phone)
        return result.fetchone() is not None

    def check_chat(self, chat_id):
        """
        The function checks whether this chat is exist or not.
        :param chat_id: representing the chat id in the SQL table.
        :return: boolean, True if exists / False otherwise
        """
        result = self.cur.execute("SELECT * FROM Chats WHERE id = %s" % chat_id)
        return result.fetchone() is not None

    def register(self, phone, password, name, age):
        """
        A function register new user (including contact) if the phone number not in use.

        :param phone: as a username.
        :param password: should be encoded with EncryptData, but there is no check for password.
        :param name: the name will be displayed in chat.
        :param age: the user age.
        :return: a message of error / confirm, and the error code.
        """

        if not self.check_phone(phone):
            self.new_contact(name, age, phone)
            self.new_user(phone, password)
            return CONFIRM_MESSAGE, 0
        else:
            return ERROR_1_PHONE_IN_USE, 1

    def connect(self, phone, password):
        """
        A function made to check if user in database and if password fit the username.
        :param phone: as a username.
        :param password: the user password chosen at the register.
        :return: a message of error / confirm, and the error code.
        """
        # Checks if the phone is in the ContactCard table
        if self.check_phone(phone):
            result = self.cur.execute("SELECT password FROM Users WHERE id = %s" % phone)
            # Checks if the phone is in Users table
            row = result.fetchone()
            if row is not None:
                db_password = row[0]
                # Checks if the password fits the username
                if password == db_password:
                    return CONFIRM_MESSAGE, 0
                else:
                    return ERROR_3_PASSWORD_INCORRECT, 3
            else:
                return ERROR_2_PHONE_DOES_NOT_EXISTS, 2
        else:
            return ERROR_2_PHONE_DOES_NOT_EXISTS, 2

    def add_chat_to_user(self, phone, chat_id):
        """
        This function adds the chat to the user's chat list, if the chat exist.
        :param phone: as a username.
        :param chat_id: the wanted chat's id.
        :return: a message of error / confirm, and the error code.
        """
        if self.check_phone(phone):
            if self.check_chat(chat_id):
                result = self.cur.execute("SELECT chat_list FROM Users WHERE id = %s" % phone)
                row = result.fetchone()
                # Add the new chat id
                row = row[0] + chat_id + ","

                # Update data in the memory
                self.cur.execute("UPDATE Users SET chat_list = ? WHERE id = ? ;", (row, phone))
                self.con.commit()

                return CONFIRM_MESSAGE, 0
            else:
                return ERROR_4_CHAT_DOES_NOT_EXISTS, 4
        else:
            return ERROR_2_PHONE_DOES_NOT_EXISTS, 2

    def finish(self):
        self.cur.close()
        self.con.close()


if __name__ == "__main__":
    # Create interface
    userDatabase = UsersDatabase()

    # check if phone is not in use
    # print(userDatabase.check_phone("1234567890"))

    # Try register new users.
    # message, status = userDatabase.register("1234567890", "05123", "roy", 23)
    # message2, status2 = userDatabase.register("1234567899", "05123", "roy", 23)

    # print(message)
    # print(message2)

    # Try to connect.
    # message3, status = userDatabase.connect("123456", "05123")
    # message4, status = userDatabase.connect("1234567899", "051234")
    # message5, status = userDatabase.connect("1234567899", "05123")

    # print(message3)
    # print(message4)
    # print(message5)

    # message6, status = userDatabase.add_chat_to_user("1111", "1")
    # print(message6)

    userDatabase.finish()


