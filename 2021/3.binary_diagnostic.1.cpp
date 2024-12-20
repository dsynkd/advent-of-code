#include <iostream>
#include <vector>

using namespace std;

int main() {
    int common_bit = 0;
    string report;
    vector<string> reports;
    while(cin >> report) {
        reports.push_back(report);
    }
    int l = reports[0].size();
    int common_bits[l];
    for(int i = 0; i < l; ++i) {
        common_bits[i] = 0;
    }
    for(auto report: reports) {
        for(int i = 0; i < l; ++i) {
            char ch = report[i];
            if(ch == '0') {
                common_bits[i] -= 1;
            } else {
                common_bits[i] += 1;
            }
        }
    }
    char gamma_rate[l];
    char epsilon_rate[l];
    for(int i = 0; i < l; ++i) {
        int bit = common_bits[i];
        if(bit > 0) {
            gamma_rate[i] = '1';
            epsilon_rate[i] = '0';
        } else {
            gamma_rate[i] = '0';
            epsilon_rate[i] = '1';
        }
    }
    cout << stoi(gamma_rate, 0, 2) * stoi(epsilon_rate, 0, 2) << endl;
}