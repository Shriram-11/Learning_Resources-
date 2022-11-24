![plot](D:\Learning_Resources-\Java\1.png)

## How does a java code works

Java makes use of Java Virtual Machine which cotains different libraries for the code to work. The strps involved are:

1. Type your code
2. An interpretor converts the source code into BYTECODE
3. The byte code is futher compoled by JAVA compiler to make it machine readable

## Structure of a JAVA class

**Class**: A class is a User-defined datatype, which contains a collection of similar objects.

**Object**: An object is an instance of a class.

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
