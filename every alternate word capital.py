#every alternate word of a sentence will be capital using while and for loop


while True:

    list1=[]
    
    sentence=input("Enter sentence or press 'N' to stop: ")
    
    if sentence=='N':
        break
        
    sentence=sentence.split()  #make it a list

    for i in range(len(sentence)):   
        if i%2==0:               
            sentence1=sentence[i].upper()
            list1.append(sentence1)
        elif i%2!=0:
            sentence1=sentence[i].lower()
            list1.append(sentence1)
            
    print(list1)