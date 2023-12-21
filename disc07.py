# THIS IS DISC07
# Q1: WWPD: Legally Blonde OOP
class Student:

    extension_days = 3 # this is a class variable

    def __init__(self, name, staff):
        self.name = name # this is an instance variable
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_extension_days(self, student, days):
        student.extension_days = days      # Q1 WWPD FINISHED

# Q2: Email
class Email:
    """
    Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    >>> email = Email('hello', 'Alice', 'Bob')
    >>> email.msg
    'hello'
    >>> email.sender_name
    'Alice'
    >>> email.recipient_name
    'Bob'
    """
    def __init__(self, msg, sender_name, recipient_name):
        "*** YOUR CODE HERE ***"
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name     # Q2: Email class finished

class Client:
    """
    Every Client has three instance attributes: name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    """
    def __init__(self, server, name):
        self.inbox = []
        "*** YOUR CODE HERE ***"
        self.server = server
        self.name = name
        self.server.register_client(self, self.name)    # 新建客户端后，直接注册在server上,初始化的时候就进行注册

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client."""   # 发送邮件给制定的接受者
        "*** YOUR CODE HERE ***"
        # 这里应该是先生成email再调用Server的send（）将邮件发送
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        "*** YOUR CODE HERE ***"
        # self.inbox.append(email.msg)  # 不是把email.msg给传递到inbox而是把整个email给传递到inbox
        self.inbox.append(email)      # inbox看做是一个装着emai这个对象的list而不是装着emal。msg的list

class Server:
    """
    Each Server has one instance attribute: clients (which
    is a dictionary that associates client names with
    client objects).
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """
        Take an email and put it in the inbox of the client
        it is addressed to.
        """
        "*** YOUR CODE HERE ***"
        # 如果是email中的接受者的名字在self.client中找不到，那么就应该先进行注册，如果能找到就直接发送
        #self.clients[email.recipient_name].inbox.append(email.msg)      # 写到这里⭐️
        # 应该是找到收件人的对应client 并直接调用receive即可
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """
        Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        "*** YOUR CODE HERE ***"
        # 当客户端进行注册的时候应该是将名称和对应的对象本身存在字典内
        self.clients.update({client_name: client})            # Q2: Email FINISHED


# Q4: That's inheritance, init?
class Butterfly():
    def __init__(self, wings=2):
        self.wings = wings

class Monarch(Butterfly):
    def __init__(self):
        #_________________________________________
        #super.__init__()
        super().__init__()
        self.colors = ['orange', 'black', 'white']

#class MimicButterfly(______________):
class MimicButterfly(Monarch):
    def __init__(self, mimic_animal):
    #    _______________.__init__()
        super().__init__()
        #______________ = mimic_animal
        self.mimic_animal = mimic_animal




        