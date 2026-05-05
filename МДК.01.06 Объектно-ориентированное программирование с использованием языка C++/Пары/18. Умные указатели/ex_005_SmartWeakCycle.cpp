#include <iostream>
#include <memory>
using namespace std;

struct NodeB;

struct NodeA{
    shared_ptr<NodeB> partner;
    ~NodeA() {
        cout << "NodeA удалена" << endl; 
    }
};

struct NodeB{
    weak_ptr<NodeA> partner;
    ~NodeB(){
        cout << "NodeB удалена" << endl;
    }

        void check_parther(){
        if(auto loacked = partner.lock()){
            cout << "NodeA существует" << endl;         
        }
        else{
            cout << "NodeA удалена" << endl;
        }
    }
};

int main(){
    setlocale(LC_ALL, "ru");
    {
        auto a = make_shared<NodeA>();
        auto b = make_shared<NodeB>();
        a->partner = b;
        b->partner = a; // weak_ptr
        cout << "Количество ссылок: " << a.use_count() << endl;
    }
}