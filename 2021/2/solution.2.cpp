#include <iostream>

using namespace std;

int main() {
    int depth = 0, position = 0, aim = 0;
    string cmd;
    int x;
    while(cin >> cmd >> x) {
        if(cmd == "forward") {
            position += x;
            depth += aim * x;
        } else if(cmd == "down") {
            aim += x;
        } else if(cmd == "up") {
            aim -= x;
        }
    }
    cout << depth * position << endl;
}