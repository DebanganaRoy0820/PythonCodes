# Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open("../MailMerge/Input/Names/invited_names.txt", mode='r') as invite:
    names = invite.readlines()

# Replace the [name] placeholder with the actual name.

for name in names:
    with open("../MailMerge/Input/Letters/starting_letter.txt", mode='r') as letter:
        name = name.strip("\n")
        text = letter.readlines()
        text[0] = text[0].replace("[name]", name)
        # Save the letters in the folder "ReadyToSend".
        fn = "C:/Users/dbsr6/PycharmProjects/MailMerge/Output/ReadyToSend/" + name + '.txt'
        with open(fn, mode='w') as new_letter:
            new_letter.writelines(text)
        new_letter.close()
        letter.close()
invite.close()

