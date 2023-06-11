#include <iostream>
#include <cstdlib>

using namespace std;
class Student
{
protected:
    char name[30], usn[30];

public:
    virtual void show() = 0;
};

class Std_Adm : Student
{
protected:
    int fees;

public:
    virtual void insert()
    {
        cout << "\nName:";
        cin >> name;
        cout << "\nUSN:";
        cin >> usn;
        cout << "\nFees:";
        cin >> fees;
    }

    void show()
    {
        cout << "\nName:" << name << "\nUSN:" << usn << "\nFees:" << fees;
    }
};

int main()
{
    Std_Adm s[10];
    int n, i;
    cout << "\nEnter no. of students:";
    cin >> n;
    for (i = 0; i < n; i++)
    {
        s[i].insert();
    }
    for (i = 0; i < n; i++)
    {
        s[i].show();
    }
    return 0;
}