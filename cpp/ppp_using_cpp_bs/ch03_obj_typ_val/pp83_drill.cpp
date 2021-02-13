#include "../std_lib_facilities.h"

int main() {
    cout << "Enter the name of the person you want to write to (followed by 'enter'):\n";
    string first_name = "???";
    cin >> first_name;

    cout << "Enter friend's age:\n";
    int age_years = 0;
    cin >> age_years;

    if (age_years <= 0 || age_years >= 110) {
        simple_error("you're kidding!");
    }

    string age_message = "";
    if (age_years < 12) {
        age_message = "Next year you will be " + to_string(age_years + 1) + ".";
    } else if (age_years == 17) {
        age_message = "Next year you will be able to vote.";
    } else if (age_years > 70) {
        age_message = "I hope you are enjoying retirement.";
    }

    cout << "Enter mutual friend's name:\n";
    string friend_name = "???";
    cin >> friend_name;

    char friend_sex = 0;
    cout << "Please enter 'm' if mutual friend is a male and an 'f' if the friend is female:\n";
    cin >> friend_sex;

    cout << "Dear " << first_name << "," << endl;
    cout << "How are you? I am fine. I miss you. I hear you just had a birthday and you are " << age_years << " years old.";
    if (!age_message.empty()) {
        cout << " " << age_message;
    }

    cout << endl;

    cout << "Have you seen " << friend_name << " lately? ";

    string pronoun = friend_sex == 'm' ? "him" : "her";

    cout << "If you see " << friend_name << " please ask " << pronoun << " to call me." << endl;

    cout << "Yours sincerely," << endl << endl;
    cout << "Tanvir" << endl;
}