#include <iostream>
using namespace std;

void swap(int &a, int &b)
{
    int t;
    t = a;
    a = b;
    b = t;
}

int main()
{
    int x, y;
    cout << "\nEnter a:";
    cin >> x;
    cout << "\nEnter b:";
    cin >> y;
    swap(x, y);
    cout << "\nAfter swapping\na=" << x << " b=" << y << endl;
    return 0;
}