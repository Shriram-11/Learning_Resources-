#include <iostream>
#include <cstdlib>

using namespace std;

class Box
{
    double l, b, h;

public:
    double volume()
    {
        return (l * b * h);
    }
    double getl(double x = 0)
    {
        l = x;
    }
    double getb(double x = 0)
    {
        b = x;
    }
    double geth(double x = 0)
    {
        h = x;
    }
    Box operator+(const Box &c)
    {
        Box r;
        r.l = l + c.l;
        r.b = b + c.b;
        r.h = h + c.h;
        return r;
    }
};

int main()
{
    Box a, b, c;
    a.getl(10);
    a.getb(10);
    a.geth(10);
    b.getl(10);
    b.getb(10);
    b.geth(10);
    c = a + b;
    cout << "\nVolume of a:" << a.volume() << "\nVoume of b:" << b.volume() << "\nVolume of c:" << c.volume();
    return 0;
}