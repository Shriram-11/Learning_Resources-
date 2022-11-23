#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    fstream f;
    string filename;
    char ch, c;

    cout << "Enter Filename:";
    cin >> filename;
    filename = filename + ".txt";
    f.open(filename, ios::out);

    if (!f)
    {
        cout << "Error 55!!! we are looking!!";
        return 0;
    }

    cout << "\nFile Created";
    f << "Ciao a tutti";
    f.close();

    f.open(filename, ios::in);
    if (!f)
    {
        cout << "Error 55!!! we are looking!!";
        return 0;
    }
    cout << "\nFile Content";
    while (!f.eof())
    {
        f >> ch;
        cout << ch;
    }
    return 0;
}