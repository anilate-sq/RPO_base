#include <iostream>
#include <string_view>

using namespace std;

void print(string_view sv){
        cout << sv << endl;
}

int main(){
       // String_view
       // string_view - используем для просмотра строк
        
       string text = "Что-то на очень важном";
       print(text);
       
       // find - поиск по первому вхождению
       string s = "abc1231";
       size_t pos = s.find("123");

        if (pos != string::npos){
                cout << "Поиск строки abc: " << pos << endl;
        }

        else{
                cout << "Что-то пошло не так";
        }
       
       // find_first_of и find_last_of
       pos = s.find_first_of("1");
       cout << "Первое вхождение: " << pos << endl;
       pos = s.find_last_of("1");
       cout << "Последнее вхождение вхождение: " << pos << endl;
       
}