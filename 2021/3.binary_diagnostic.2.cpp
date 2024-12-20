#include <stdio.h>
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
    int k = reports.size();
    bool skip_most_common[k];
    bool skip_least_common[k];
    for(int j = 0; j < k; ++j) {
        skip_most_common[j] = false;
        skip_least_common[j] = false;
    }
    string oxygen_generator_rating = "";
    string co2_scrubber_rating = "";
    for(int i = 0; i < l; ++i) {
        int most_common = 0;
        int least_common = 1;
        for(int j = 0; j < k; ++j) {
            if(skip_most_common[j]) continue;
            string report = reports[j];
            int bit = report[i];
            if(bit == '0') {
                most_common -= 1;
            } else {
                most_common += 1;
            }
        }
        for(int j = 0; j < k; ++j) {
            if(skip_least_common[j]) continue;
            string report = reports[j];
            int bit = report[i];
            if(bit == '0') {
                least_common -= 1;
            } else {
                least_common += 1;
            }
        }
        char most_common_bit = most_common >= 0 ? '1' : '0';
        char least_common_bit = least_common <= 0 ? '1' : '0';
        int c1 = 0, c2 = 0;
        string last_report;
        if(oxygen_generator_rating == "")
        for(int j = 0; j < k; ++j) {
            if(skip_most_common[j]) continue;
            string report = reports[j];
            if(report[i] != most_common_bit)
                skip_most_common[j] = true;
            else {
                last_report = report;
                c1 += 1;
            }
        }
        if(c1 == 1) {
            oxygen_generator_rating = last_report;
        }
        if(co2_scrubber_rating == "")
        for(int j = 0; j < k; ++j) {
            if(skip_least_common[j])
                continue;
            string report = reports[j];
            if(report[i] != least_common_bit)
                skip_least_common[j] = true;
            else {
                last_report = report;
                c2 += 1;
            }
        }
        if(c2 == 1) {
            co2_scrubber_rating = last_report;
        }
    }
    cout << stoi(oxygen_generator_rating, 0, 2) * stoi(co2_scrubber_rating, 0, 2) << endl;
}

