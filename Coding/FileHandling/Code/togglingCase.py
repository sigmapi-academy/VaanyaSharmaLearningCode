# toggling the alphabets of the file
fileName = input('Enter any file name: ')
with open("FileHandling/DataFiles/"+fileName, 'r') as fo:
    content = fo.read()
    tfile = input('Enter the toggle case filename: ')
    with open("FileHandling/DataFiles/"+tfile, "w") as tf:
        for ch in content:
            if ch.isalpha():
                if ch.isupper():
                    ch = ch.lower()
                else:
                    ch = ch.upper()
            tf.write(ch)