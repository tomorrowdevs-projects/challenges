#include <iostream>
#include <vector>

using namespace std;


void divisorsOfNumber(int number) {
    int count = 0;
    vector<int> divisors;

    if(number == 0){
        cout << "Quitting... " << endl;
        exit(0);
    }

    for(int n=1; n <= number; n++) {

        if(number % n == 0) {
            divisors.push_back(n);
            count++;
        }
    }
    
    cout << number << " have " << count << " divisors:";
    for(int n=0; n <= divisors.size() - 1; n++) {
        cout << " " << divisors.at(n);
    }
    cout << endl;
}


int main () {

    int n, end;

    do {
        cout << "Enter a number (0 to exit): ";
        cin >> n;

        divisorsOfNumber(n);
    }
    while(end!=0);

    return 0;
}
