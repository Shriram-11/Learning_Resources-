#include <iostream>
using namespace std;

class Books
{
public:
    int bno;
    char title[10], author[10], publisher[10];
    float price;
    void read()
    {
        cout << "\nBook No.:";
        cin >> bno;
        cout << "\nBook Name:";
        cin >> title;
        cout << "\n Author Name:";
        cin >> author;
        cout << "\n Book Publisher:";
        cin >> publisher;
        cout << "\nPrice:";
        cin >> price;
    }

    void display()
    {
        cout << "\nBook no.:" << bno << "\nAUthor:" << author << "\nTitle:" << title << "\nPublisher:"
             << publisher << "\nPrice" << price;
    }
};

void search(Books ob[], int n)
{
    int f;
    char t[10], a[10];
    cout << "\nEnter book title:";
    cin >> t;
    cout << "\nEnter author Name:";
    cin >> a;
    for (int i = 0; i < n; i++)
    {
        if (ob[i].author == a && ob[i].title == t)
            cout << "\nFound\n";
        ob[i].display();
        f = 1;
        break;
    }
    if (f == 0)
        cout << "\nNot Found\n";
}

int main()
{
    Books b[100];
    char t[10], a[10];
    int n, ch, f = 0;

    do
    {
        cout << "\nChoose from the follwing:\n1. Enter\n2. Search\n3. Display\n4. Exit\nEnter Choice:";
        cin >> ch;
        switch (ch)
        {
        case 1:
            cout << "\nNo. of books to add:";
            cin >> n;
            for (int i = 0; i < n; i++)
            {
                b[i].read();
            }
            break;
        case 2:
            search(b, n);
            break;
        case 3:
            for (int i = 0; i < n; i++)
                b[i].display();
            break;
        case 4:
            exit(0);
        default:
            cout << "Invalid:";
            break;
        }
    } while (1);
    return 0;
}