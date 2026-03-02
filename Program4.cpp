#include <iostream>

using namespace std;

int main() {
    float celsius;

    cin >> celsius;

    float fahrenheit = (celsius * 9 / 5) + 32;

    cout << fahrenheit << endl;

    return 0;
}