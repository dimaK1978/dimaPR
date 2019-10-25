name = input("как тебя зовут?  ")

if name == "Дима":
    
    print("иди в жопу, ", name, "!")

elif name == "Оля":

    print("Привет, ", name, "!")

elif name == "Саша":

    print("Хорошего дня, ", name, "!")
    
elif name == "Сережа":

    print("Иди кушать, ", name, "!")
else:
    
    print("идите прочь, я вас не знаю!")

ask = input("ты хочешь есть?  " )
if ask == "да" :
   print("правильный ответ, ",name,"!") 
elif ask == "нет" :
   print("неправильный ответ, на самом деле, ДА, ",name,"!") 
else :
    print("так и знали, ты точно хочешь есть!", name,"!")
i=-10
s=list(name)
f=open('test.txt','w')
while i<-1:
    print(i,'\r')
    i+=3
    s.append(i*2)
 
s.append("конец")
print(s)
l="ты хоченшь есть "+'\n'+name
f.write(l)

f.close()
