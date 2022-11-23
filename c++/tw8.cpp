#include <iostream>
#include <cstdlib>
using namespace std;

class Std
{
    int roll;
    char Name[30], gender, usn[10];

public:
    void getinfo()
    {
        cout << "\nName:";
        cin >> Name;
        cout << "\nGender:";
        cin >> gender;
        cout << "\nUsn:";
        cin >> usn;
        cout << "\nRoll:";
        cin >> roll;
    }
    void putinfo()
    {
        cout << "\nName:" << Name << "\nRoll:" << roll << "\nUSN:" << usn << "\nGender:" << gender;
    }
};

class result : public Std
{
    int marks;
    char grade;

public:
    void getresult()
    {
        cout << "\nMarks:";
        cin >> marks;
        cout << "\nGrade";
        cin >> grade;
    }

    void putresult()
    {
        cout << "\nMarks:" << marks << "\nGrade" << grade;
    }
};

int main()
{
    result r;
    r.getinfo();
    r.getresult();
    r.putinfo();
    r.putresult();
    return 0;
}