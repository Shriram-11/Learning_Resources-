'''
Store the following information in a dict, course code, name, faculty, no. of registration
Perform the following operrations using functions:
1. Find Course Name that has the highest no. of registrations and
2. Given the course code , display the associated details
3. Display details of all Courses
'''
# Empty Dictionary
course={}
# Add a course
def add():
    courseCode=input("Enter Course Code:")
    if courseCode in course:
        print("Course Code Already Exists")
        return
    courseName=input("Enter Course Name:")
    fac=input("Enter Faculty Name:")
    reg=int(input("No. of registration:"))
   
    course[courseCode]=[courseName,fac,reg]
# Search for a course
def searchC():
    code=input("Enter Course Code")
    if code in course:
        li=course[code]
        print("Course Code:",code," Course Name:",li[0],"\nFaculty:",li[1]," No. of registrations:",li[2])
    else:
        print("Not Found")
# Display All Courses
def display():
    for key,li in course.items():
        print("Course Code:",key," Course Name:",li[0],"\nFaculty:",li[1]," No. of registrations:",li[2],"\n----------\n")
# Display course with max registration
def max_registrations():
    maxR=0
    maxK=""
    for key,li in course.items():
        if li[2]>maxR:
            maxR,maxK=li[2],key
    li=course[maxK]
    print("Course Code:",key," Course Name:",li[0],"\nFaculty:",li[1]," No. of registrations:",li[2])    
def main():
    while True:
        ch=int(input("Choices are:\n1. Add Course    2.Search Course    3.Course with max registrations    4: Display al    5.Exit\nEnter Choice"))
        if ch==1:
            add()
        elif ch==2:
            searchC()
        elif ch==3:
            max_registrations()
        elif ch==4:
            display()
        elif ch==5:
            break
        else:
            print("Invalid Input")
if __name__=="__main__":
    main()