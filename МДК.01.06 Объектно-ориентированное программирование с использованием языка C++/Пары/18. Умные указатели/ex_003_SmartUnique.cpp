#include <iostream>
#include <memory>

using namespace std;

class HeavyObject{
    public:
        HeavyObject(const string& name) : name(name){
            cout << "Объект " << name << " создан" << endl; 
        }

        ~HeavyObject(){
            cout << "Объект " << name << " был уничтожен" << endl;
        }

        void process() {
            cout << "Процесс работы над " << name << " начат" << endl;
        }

    private:
        string name;
};

void test_unique_ownership(){
    auto obj = make_unique<HeavyObject>("Молочный коктейль");
    obj->process();

    auto obj2 = move(obj);
    obj2->process();
}

int main(){
    setlocale(LC_ALL, "ru");
    test_unique_ownership();
}