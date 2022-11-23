
#include <iomanip>
#include <iostream>
using namespace std;
#include <cstdlib>
class employee
{

    int emp_num;
    char emp_name[20];
    char emp_dept[5];
    float emp_basic;
    float sal;
    float emp_da;
    float emp_hra;
    float net_sal;
    float grs_sal;
    float emp_it;

public:
    void get_details();
    void find_net_sal();
    void show_emp_details();
};

void employee ::get_details()
{

    cout << "\nEnter employee number:\n";
    cin >> emp_num;
    cout << "\nEnter employee name:\n";
    cin >> emp_name;
    cout << "\nEnter employee dept:\n";
    cin >> emp_dept;
    cout << "\nEnter employee basic:\n";
    cin >> emp_basic;
}

void employee ::find_net_sal()
{

    emp_da = 0.7 * emp_basic;
    emp_it = 0.05 * emp_basic;
    emp_hra = 0.2 * emp_basic;
    grs_sal = emp_basic + emp_da + emp_hra;
    net_sal = grs_sal - emp_it;
}

void employee ::show_emp_details()
{

    cout << "\n***********Details of " << emp_name << "*************"
         << setw(05) << "\nEmployee Number :" << setw(05) << emp_num
         << setw(05) << "\nDepartment     :" << setw(05) << emp_dept
         << setw(05) << "\nBasic Salary   :" << setw(05) << emp_basic
         << setw(05) << "\nEmployee DA    :" << setw(05) << emp_da
         << setw(05) << "\nEmployee_HRA   :" << setw(05) << emp_hra
         << setw(05) << "\nIncome_Tax     :" << setw(05) << emp_it
         << setw(05) << "\nGross_Salary   :" << setw(05) << grs_sal
         << setw(05) << "\nNet Salary     :" << setw(05) << net_sal << endl;
}

int main(int argc, char *argv[])
{
    employee emp1;
    emp1.get_details();
    emp1.find_net_sal();
    emp1.show_emp_details();

    // system("PAUSE");
    return EXIT_SUCCESS;
}