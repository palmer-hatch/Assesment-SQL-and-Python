


#opening the .txt. file and setting it to a variable
log_file = open("um-server-01.txt")

#function
def sales_reports(log_file):
    #for loop
    for line in log_file:
        #removing any trailing characters at the end of a string
        line = line.rstrip()
        #setting an item in the list to a variable to call it
        day = line[0:3]
        #if function to print the day variable if it is equal to the value
        if day == "Mon":
            #console.log
            print(line)

#inciting the function
sales_reports(log_file)

#DB DESIGN
# https://dbdesigner.page.link/5bSdhGAg3GKRaEHD6
