# List # how they work how to create what they are # Lists: ordered, mutable, allows duplicate elements # with that said some inventeed this list  just with those few words and made it special

mylist = ["banana", "cherry", "apple"]
print(mylist)

item = mylist[]
print(item)
# with this option when i do print() an a  number leys say 0 then 0 = to my banana in my list
# if i do 1 instea of 0 now that woould be cherry
# but if i put 3 thats an error now you see everything that start with en braclet [] is orders from 0,1,-1 and its has to be a negative number at the end so its now its ended

for i in mylist:
    print(i)
# now what this will do is print everything that mylist() hase in it 


if "banna" in mylist:
    print("yes")
else:    
    print("no")
# that lets me check my list() for stuff like items that i put in it 

print(len(mylist)
#
# well now this this code you can see how many elements you have in your list

mylist.append("lemon")
print(mylist)

# with that said i can add stuff to my list

mylist.insert(1, "blueberry")
print(mylist)

# with this command i can replace stuff within my list

item = mylist.pop()  # what this does is shows the last item in our list which rn is apple #
print(item)          # and here now when we print we will see that our aple is no longer in our list 

# we can also remove a specific item if we wont to with the command
item = mylist.remove()  # now if u put a number from 0 or 1 or -1 u can remove the first middle or the lst number deepends how many items you have in your list 
# so if you dont know remember to make sure that you check with other commands that you learn unelss you dont care that it can be removed and you go always go to the top and replace it if you wanted to
# to remove also if you want to you can just provide the identical name that its in this list and then its getting removed but if you provide a name then dont put any number into it or else it will fail the task 
# and it wont work

item = mylist.clear()  # i dont have to say much with this one it removes all itesm that are in your list

item = mylist.reverse() # with this like the word says just revers which means if the start was first then the end will take his spot and the start will take the end position
# with that said if u have something in ur list aht is specified to be first dont use it 
# its good to use for gambling i guess i think to revers itmes and then revers again after the 2nd launche so for each launch there will be also a diff result
# and how many result would you put in there is up to you

item = mylist.sort()  # well now this command is to sort your lsit if its contains letters from a to b 
                      # else you know what i want to say right ? its also for number so if you have numbers in ur list will sort them form 1 to -1   or will try at least depens how you type it
                      #   with that said thats all i can say about list and all what you can do with it # list is a good think for notes and to make a dic 
                      # well now dic is some sort of a list but different it comes with key.valuse and if u dont know what that means well then you will get rekt so google for that its hard to explain
                      # always is better to find a way on your own to write something down like i do right now which lets me to write all this which is a huge as text just for myslef
                      # so i can understand just how 1 simple code can change so many thing .\ well if you 
                      # @ if you use sort.mylist with number in it ti will take the negative from left to right which means -1 -2 -3 etc to end + positve at the end which could be 1 2 3 or 10
# now if you would like to replace your list with sorted sutff but also have the old one back there then do this
                     
new_list = sorted(mylist)   # with that you sorted your list and you can call that iwth a dif name but also you left the first list up there unahcanged 

# u can also put same name into the same list with different attributs what i want to say with that let me explain now well look

mylist = [0] * 5  # and u print the list now it will show you a list of this [0, 0, 0 , 0 ,0]
###############################################################################################

mylist2 = # now if you started a list with a list name and then name it mylist you can use the ssame name like i used which is mylist2 and assiged that lsit to do something different

# if u want both of the list to be prited do that
new_list = mylist + mylist2
# if u print this then both will be showed

mylist = [1, 2, 3 , 4, 5, 6, 7, 8, 9]

a = mylist[1:5]
print(a)
# with htis command i can assiged which number i wanted to call from that collum it this case its 1 to 5 and its will stop at 5
# if i dont specifed a number within the brackets and : it will asume i want the whole list or else
# if i do  2: and put nothing on the other side then it will prit from 2 till the end 
# same from  :2 same thing but different side
# or else what i can do is also ::2 and then it will make it to take every second item in that bracet 
# so if i want to do the asme thing but from behind i can do is ::-1 and it will start from a negative index which is on that list

list_org = ["banana", "cherry", "apple"]

list_cpy = list_org

# with that said i just made a copy of my list and named ir list_org but its still under the same name it just a copy 
# but if i do any adjustments to my list it will also affect my original list at the top
# for exaple if i use the command i used fro mthe top 

list_cpy.append ("lemmon")  # that command now will remove it from both  list the original and also the cpy version one 
# if we dont want to affect the list sry the orignial list with the cpy one then do this instead

list_cpy = list_org.copy() # with that we have a coppy that we can use for different thinks its more secure not to screw something up 
# if we forget about something 

# now list_cpy = list_org,copy()
#can be also typed in likes this #

list_cpy = list(list_org)
#  or #
list_cpy = list_org[:]
# this will make laso a copy of ur list


mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist ]     # this can create loop with ur list and make them look different

print(mylist)
print(b)
# this will make changed into our original list 

