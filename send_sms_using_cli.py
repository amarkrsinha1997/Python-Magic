# we are importing a package for messaging called Nexmo
#install it using pip install nexmo and then import it
import nexmo


#Replace the number with the verified number of your account
number=['9891943414','7896121314']


#Here we have to assign the key and secret that is provided to us by nexmo
#on its website www.nexmo.com ou have to signup
client = nexmo.Client(key='7864490e',secret='e2b024b515702196')

# Creating the message
def create_message():
    message= raw_input('Enter your message: ')
    
    
    print('select number 1 or 2',number)
    choice=int(raw_input('Your Choice : '))
    
    send(message,choice)

# sending the message
def send(message,choice):
    #if you had buyed an number replacce it with "Nexmo"
    #or you can buy something else for that money
    response = client.send_message({
    'from': 'Nexmo',
    'to': '+91' + number[choice-1],
    'text': message
    })

    # calling the response_text function
    response_text(response)

#Collecting responses
def response_text(response):
    #getting the response from the dict response
    response= response['messages'][0]

    #checking if the message was delivered or not
    if response['status']=='0':
        print 'Send message: ',response['message-id']
    else:
        print "Error: ",response['error-text']


create_message()


