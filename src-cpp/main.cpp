#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// https://www.geeksforgeeks.org/cpp/serialize-and-deserialize-an-object-in-cpp/

class Car {
private:
    string model;
    int year;

public:
    Car() {};
    Car(const string& model, int year): model(model), year(year) {}

    void printData() {
        cout << model << " " << year << endl;
    }

    void serialize(const string& filename) {
        ofstream file(filename, ios::binary);
        if (!file.is_open()) {
            cerr
                << "Error: failed to open file."
                << endl;
            return;
        }
        file.write(reinterpret_cast<const char*>(this), sizeof(*this));
        file.close();
        cout << "Object serialized." << endl;
    }

    static Car deserialize(const string& filename) {
        Car obj("", 0);
        ifstream file(filename, ios::binary);
        if (!file.is_open()) {
            cerr
                << "Error: failed to open file."
                << endl;
            return obj;
        }

        file.read(reinterpret_cast<char*>(&obj), sizeof(obj));
        cout << "Object deserialized." << endl;
        return obj;
    }
};

int main() {
    cout << "Hello World" << endl;

    Car original("Ford F150", 2020);
    original.serialize("data.bin");

    Car restored = Car::deserialize("data.bin");

    original.printData();
    restored.printData();
}