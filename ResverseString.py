def reversestring(sentence):
        reversewords=[]
        words=sentence.split(" ")
        for word in words:
            newword=word[::-1] 
            #print(newword)
            newstring=newword.capitalize()
            print(newstring)
        
reversestring("This is a demo string My name is shriSHTI")
            