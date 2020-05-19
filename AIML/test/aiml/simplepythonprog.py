import aiml

#create the kernel and learn ATML files 
kernel=aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

#press CTRL+C to break this loop
while True:
    print (kernel.respond(input("Enter your message >> ")))