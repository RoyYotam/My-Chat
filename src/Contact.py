

class ContactCard:
	def __init__(self, name, phone_number, age, contact_id):
		self.name = name
		self.phone_number = phone_number
		self.age = age
		self.id = contact_id

	# Setters
	def set_phone_number(self, new_phone_number):
		self.phone_number = new_phone_number

	# Getters
	def get_name(self):
		return self.name

	def get_phone_number(self):
		return self.phone_number

	def __str__(self):
		return f"Hello, i'm {self.name}, {self.age} years old.\n" \
				f"My phone number is {self.phone_number}, and my id is {self.id}."


class Contact(ContactCard):
	def __init__(self, name=None, phone_number=None, age=None, contact_id=None, contact_card=None):
		if contact_card:
			name = contact_card.name
			phone_number = contact_card.phone_number
			age = contact_card.age
			contact_id = contact_card.id
		super(Contact, self).__init__(name=name, phone_number=phone_number, age=age, contact_id=contact_id)
		self.uniq_id = ''
		self.group_list = []


if __name__ == '__main__':
	# Test ContactCard
	me = ContactCard('roy', '0544894060', 23, 206206206)
	print(me)

	# Test Contact
	player_me = Contact(contact_card=me)
	player_me_2 = Contact('roy', '0544894060', 23, 206206206)
