#include <iostream>
#include <cstdlib>
using namespace std;
class Player
{
    int pno, m;
    char name;
    int *goals;

public:
    Player()
    {
        cout << "Player No.:";
        cin >> pno;
        cout << "\nName:";
        cin >> name;
        cout << "No. of Matches: ";
        cin >> m;
        goals = new int[m];
        cout << "\nEnter Goals in Each Match:";
        for (int i = 0; i < m; i++)
        {
            cout << "\nMatch:" << i + 1 << " Goals:";
            cin >> goals[i];
        }
    }

    void display()
    {
        cout << "\n************\nPlayer No.:" << pno << "\nName:" << name << "\nNo. of Matches: " << m
             << "\nGoals in Each Match:";
        for (int i = 0; i < m; i++)
        {
            cout << "\nMatch:" << i + 1 << " Goals:" << goals[i];
        }
    }

    ~Player()
    {
        cout << "\n\nDestruction";
    }
};

int main()
{
    Player P;
    P.display();
    return 0;
}