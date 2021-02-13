#include "../std_lib_facilities.h"

int main() {
    cout << "Please enter your name and age (followed by 'enter'):\n";
    string first_name = "???";
    double age_years = 0;

    cin >> first_name;
    cin >> age_years;

    cout << "Hello, " << first_name << " (age " << (age_years * 12) << " months)\n" ;
}