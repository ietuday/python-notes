# MASTER YODA:
# Given a sentence, return a sentence with the words reversed


def master_yoda(text):
    return ' '.join(text.split()[::-1])


test = master_yoda('I am home')
print(test)
