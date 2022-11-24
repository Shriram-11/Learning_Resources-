## How does a java code works

Java makes use of Java Virtual Machine which cotains different libraries for the code to work. The strps involved are:

1. Type your code
2. An interpretor converts the source code into BYTECODE
3. The byte code is futher compoled by JAVA compiler to make it machine readable

## Object oriented concepts

**Class**: A class is a User-defined datatype, which contains a collection of similar objects.

**Object**: An object is an instance of a class.

**Encapsulation**:Encapsulation is defined as the wrapping up of data under a single unit. It is the mechanism that binds together code and the data it manipulates. Another way to think about encapsulation is, that it is a protective shield that prevents the data from being accessed by the code outside this shield.

**Abstraction**:Data abstraction is the process of hiding certain details and showing only essential information to the user.

Abstraction can be achieved by using an abstract class or method.

**Inheritence**:Each class has a potential of becoming a super class having unlimited sub-classes,the sub-clasees bear some of the properties from its super-class.(_a sub class can have on direct super class_)

**Polymorphism**:

**Dynamic Biniding**:When a method is called within a program, it associated with the program at **run time** rather than at **compile time** is called dynamic binding.

## Features of Java

1. Simple:
   -Java is very simple to learn.The syntax is clean and easy to understand.
   -Removed some comlicated features such as pinters,operator overloading.
   -Automatic garbage collection.
   -Rich pre defind library.
2. Object Oriented:
   -Focus on data and methods of data manipulation.
   -All methods are associated with objects.
   -Rich pre-defined libraries.
3. Compiled,Interpreted and high performance:
   -Java compiler can create byte code,not native machine code.
   -The compiled byte codes are platform independent.
   -They are converted to machine code at runtime using JVM
4. Portable:
   -Same program can run on all platforms.
   -The libraries define portable interfaces.
5. Reliable:
   -Extensive compile time and run time checking.
   -Secre
   -Access restrictions are forced.
6. Multithreaded:
   -No need to wait for one task to finish before starting new task.
7. Dynamic:
   -Libraries can freely add new methods and new instance variables without any effect on client.
   -Flexibility and reusability in code.
8. Distributed:
   -Java is designed for distributed environment of theinternet as t supports TCP/IP.
9. Architecture Neutral:
   -No implementation dependent features. e.g, the size of primitive data types is fixed.

## Variables

Types:

1. Local variables:
   -Declared inside a method,constructors or blocks.
   -It will be destroyed once it exits the method or block.
   -There is no default values for the local variables.
2. Instance Variables:
   -Instance variables are declared inside a class,but outside any method,constructor or a block.
   -Each object has its own copy of instance variables and they are destroyed when the class is destroyed.
   -Access specifiers can be given to them.
   -They are visible to all the methods and blocks inside the class.
   -They have a default value as 0.
3. Static Variables:
   -Stored in static memory.
   -Declared using _static_ keyword.
   -Visibility similar to instance variables.
   -There would be only one copy of the instance variables regardless of the no. of objects.
   -Default value is 0.
   -Created when program is started and deleted when program is ended.

## Control statements

### Conditional

1. if else

   ```
   if(condition){
       statement(s)
   }
   else{
       statements;
   }
   ```

2. if else if ladder:

   ```
   if(condition)1{
       statement(s)
   }
   else if(condition2){
       statement(s)
   }
   .
   .
   .
   else if(condition n){
       statement(s)
   }
   else{
       statements;
   }
   ```

### Looping Statements

1. While
   ```
   while(condition){
       statements;
   }
   ```
   _Note: instead of while(1), we use while(true)_
2. do while:
   ```
   do{
       statements;
   }while(condition);
   ```
3. for loop:
   ```
   for(initialization,condition,iteration){
       //body
   }
   ```
4. for each loop
   ```
   for(data_type variable:array)
   {
       statements using variable;
   }
   ```

### Jump statements

1. continue //bypass the following statements
2. break: exit from the loop
3. return: control returns to the caller.

## Structure of a JAVA class

```
    access_specifier class class_name{
        instance_variable(s);
        return_type method_name(parameter(s)){
            statements;
        }
        //There can be any number of methods and instance variables in a CLASS

    }
```

The class containing the **main** method is called the main class of the program. JVM will always executes the main method first.
The **main class** and the **main method** should always be **public** for the JVM to be able to access it.

```
\\Simple hello_word program
public class HW{
    public static void main(String[] args){
        System.out.println("Helloworld!!!");
    }
}
```

## Strings and arrays

### Arrays

Arrays are a collection of elements of similar type.

### Declaration of arrays:

```
datatype[] arr_name=new datatype[size]; \\single dimentional arrays
datatype[][] arr_name=new datatype[row_size][column_size]; \\multi dimentional arrays
```

### Initialization of array:

1.  Static initialization
    ```
    int[] arr={1,2,3,4,5,6,7,8,9,10};
    ```
2.  Dynamic initialization
    ```
    int arr=new int[10];
    Scanner in = new Scanner(Sytem.in);
    for(int i=0; i<10; i++){
        System.out.println("Enter element)
        arr[i]=in.nextInt();
    }
    ```

### Accesing array elements

```
    arr_name[index];
```
