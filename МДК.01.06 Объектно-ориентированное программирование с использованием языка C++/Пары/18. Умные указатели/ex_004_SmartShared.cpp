#include <iostream>
#include <memory>
#include <vector>

using namespace std;

void show_ref_count(const string& msg, const shared_ptr<string>& ptr){
    cout << msg << " количество: " << ptr.use_count() << endl;
}

void test_shared_ownership(){
    auto data = make_shared<string>("Выделили новый блок памяти");
    show_ref_count("Создана", data);

    vector<shared_ptr<string>> copies;
    for(int i = 0; i < 3; i++){
        copies.push_back(data);
        show_ref_count("Добавлена копия: " + to_string(i+1), data);
    }

    copies.clear();
    show_ref_count("Произведена очистка", data);
}

// По окончанию выполения функции data удалится

int main(){
    setlocale(LC_ALL, "ru");
    test_shared_ownership();
    
}