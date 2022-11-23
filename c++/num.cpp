#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(int argc, char **argv)
{
    int a, b, i;
    string ar[10] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    cin >> a >> b;
    for (i = a; i <= b; i++)
    {
        if (i >= 0 && i < 10)
        {
            cout << ar[i] << "\n";
        }
        else
        {
            if (i % 2 == 0)
            {
                cout << "even\n";
            }
            else
            {
                cout << "odd\n";
            }
        }
    }
    return 0;
}