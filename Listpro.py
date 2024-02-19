#List  is a collection of item
def yoyo():#list method

     #variable declare in list with square bracket
     name = ["Pema", "pakpa", "Simi", "somi"]

     #Declaring another varible with oman name
     oman = [4, 5, 6, 7]

     #This is add the list in name variable using append
     name.append("Yoyo")

    #this is Cancat the two list
     print(name[1:3]+oman)

    #Repetation in list
     print(name[0]*4)

     #access list
     print(name[:-2])

     #access before and after from list
     print(oman[1:3])

     #access list item as same print(name)
     print(name[:])

     #update list item
     name[1:3]='x','y','z'
     name[1]="hoiram"
     #add item in list we have append and insert keyword
     name.append(oman)
     #insert can chage value also with location
     oman.insert(0, 'Ram')
     print(oman)

     #Remove item and object from list
     oman.remove(4)
     print(oman)

     #pop in list where we can remove argument with index
     oman.pop(2)
     print(oman)

     #delete keyword in list that can delete
     del oman[1]
     print(oman)

     #now item show using for loop in list lets know the idea
     samir=[3, 5, 6, 7, 8]

     for i in samir:
         print(i)
#list comprehension technique remaining
#sort in list
     num = [6, 2, 4, 7, 8, 5]
     num.sort()
     print(num)

#copy method in list
    #Join keyword in list
     l1=[4, 5, 6]
     l2=[1, 2, 3]
     l2+=l1
     l1.extend(l2)
     print(l2)
     print(l2)


#Method call
yoyo()