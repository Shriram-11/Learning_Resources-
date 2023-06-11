#write a python program to create a list of n names and display them
li=eval(input("Enter list:"))
occ=int(input("Enter element to count its occrences and remove it:"))

if occ not in li:
    print("Element not in the list")
else:
    count=0
    while occ in li:
        count+=1
        li.remove(occ)
    print("Updated list:",li,"\nOccrences of ",occ,":",count)
