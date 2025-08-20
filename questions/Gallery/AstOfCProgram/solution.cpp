#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double DISCOUNT = 1.5e-1;
    double price;
    
    cout << "Enter an item price: $";
    cin >> price;
    cout << fixed << setprecision(2) << price * (1.0 - DISCOUNT) << endl;
    return 0;
}
