#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
    int l, i, max, min;
    cout << "\nEnter length of the array:";
    cin >> l;
    int *a = new int[l];
    cout << "\nEnter array elements:";
    for (i = 0; i < l; i++)
        cin >> a[i];
    min = *a + 0;
    max = *a + 0;
    for (i = 0; i < l; i++)
    {
        if (a[i] < min)
            min = a[i];
        else if (a[i] > max)
            max = a[i];
    }
    cout << "\nSmallest Element: " << min << "\nLargest element: " << max << endl;
    return 0;
}