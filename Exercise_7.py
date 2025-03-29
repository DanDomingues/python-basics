#Ex 7.1


class Person:
    def __init__(self, name:str, b_day:str, email:str):
        self.email = email
        self.name = name
        self.b_day = b_day

    def __str__(self):
        return f"{self.name} ({self.b_day})"

#Ex 7.2
class ContactList:
    def __init__(self):
        self.contacts = list()

    def add_contact(self, contact:Person):
        self.contacts.append(contact)

    def remove_contact(self, contact:Person):
        if contact in self.contacts:
            self.contacts.remove(contact)

    def lookup_contact(self, contact:Person):
        return  contact in self.contacts

    def print_contact(self, contact:Person):
        if self.lookup_contact(contact):
            print(contact)

    def print_list(self):
        print("Listing contacts...")
        for contact in self.contacts:
            print(contact)
        print("Listing over")

#Ex 7.3
class Television:

    def __init__(self):
        self.status = "Off"
        self.volume = 0
        self.channel = 0

    def __str__(self):
        return f"TV is {self.status}, Channel {self.channel}, Volume: {self.volume}"

    def set_on(self, status:bool):
        if status:
            self.status = "On"
        else:
            self.status = "Off"

    def switch_status(self):
        self.set_on(not self.status == "On")

    def set_volume(self, volume:int):
        self.volume = volume

    def raise_volume(self):
        self.set_volume(self.volume + 1)

    def lower_volume(self):
        self.set_volume(self.volume - 1)

    def set_channel(self, channel:int):
        self.channel = channel

    def raise_channel(self):
        self.set_channel(self.channel + 1)

    def lower_channel(self):
        self.set_channel(self.channel - 1)

class RemoteControl:
    def __init__(self, tv:Television):
        self.tv = tv

#Runtime
person = Person("Dan", "1995/06/26", "not.an@email")
girl = Person("Ayra", "1996/01/24", "an.not@gmail")

c_list = ContactList()
c_list.add_contact(person)
c_list.add_contact(girl)
print(f"Contains: {c_list.lookup_contact(person)}")
c_list.print_list()
c_list.print_contact(person)
c_list.remove_contact(person)
c_list.print_contact(person)
print(f"Contains: {c_list.lookup_contact(person)}")

remote = RemoteControl(Television())
print(remote.tv)
remote.tv.set_on(True)
remote.tv.set_channel(14)
remote.tv.set_volume(7)
print(remote.tv)
remote.tv.lower_volume()
remote.tv.lower_volume()
remote.tv.raise_channel()
print(remote.tv)
remote.tv.switch_status()
print(remote.tv)

