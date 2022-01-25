#include <iostream>

using namespace std;

int main() {
    int depth = 0, position = 0;
    string cmd;
    int x;
    while(cin >> cmd >> x) {
        if(cmd == "forward") {
            position += x;
        } else if(cmd == "down") {
            depth += x;
        } else if(cmd == "up") {
            depth -= x;
        }
    }
    cout << depth * position << endl;
}