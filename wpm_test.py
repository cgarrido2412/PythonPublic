from time import time
 
s = '''
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
“’Tis some visitor,” I muttered, “tapping at my chamber door—
            Only this and nothing more.”
'''
words = (len(s.split()))
print(s)
print("\nAfter you are done press enter to know your time and speed")
input("Press any key to Start:")
 
try:
    print("\nTimer Started\n")
    start = time()
    t = input()
    end = time()
    total = round(end - start, 2)
    print("\nVoila you typed that correctly")
    print("Your time was %s seconds" % total)
    total = int(total) / 60
    print("Speed was %s wpm" % (str(words // total)))
 
except KeyboardInterrupt:
    print("Program stopped.")

