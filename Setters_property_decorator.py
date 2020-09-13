class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@buyrentbd.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property

    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not found. Please add email using setter"
        return f"{self.fname}.{self.lname}@buyrentbd.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split("@")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None






sabbir = Employee("Sabbir", "Ahamed")
michael = Employee("Mike", "Biondi")

print(sabbir.explain())

print(sabbir.email)

sabbir.fname = "US"

print(sabbir.email)

sabbir.email = "this.that@buyrentbd.com"
print(sabbir.lname)
print(sabbir.email)

del sabbir.email
print(sabbir.email)