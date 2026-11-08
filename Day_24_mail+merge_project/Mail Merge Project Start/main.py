#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() # Readlines reads all the lines of names into a list variable 'names'

with open("./input/letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read() # reads the entire content of the starting letter into a string variable 'starting_letter'

    for name in names:
        stripped_name = name.strip() # Remove any leading/trailing whitespace
        personalized_letter = starting_letter.replace("[name]", stripped_name) # Replace the placeholder with the actual name using the replace method
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:  # creates the file for the current person, and writes the personalized letter into it
            completed_letter.write(personalized_letter) # Write the personalized letter into the file for the current person
            print(f"Letter for {stripped_name} created.")