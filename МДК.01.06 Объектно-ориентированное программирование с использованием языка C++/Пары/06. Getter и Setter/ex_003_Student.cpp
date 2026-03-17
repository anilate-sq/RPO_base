#include <iostream>

using namespace std;

enum Groups{
        g2113,
        g2114,
        g2013,
        g2014
};

class Student{
        private:
                Groups group;
                int age;
                string name;

        public:  
                // Обработка работа с группой
                string getTextGroup(Groups group){
                        switch (group){
                                case Groups::g2114: return "Г2114"; 
                                case Groups::g2113: return "Г2113"; 
                                case Groups::g2013: return "Г2013"; 
                                case Groups::g2014: return "Г2014"; 
                                default: return "Без группы";
                        }
                }
        
                string getGroup(){
                        return getTextGroup(this->group);
                }

                void setGroup(string group){
                        if(group == "Г2114" || group == "Г2113" || group == "Г2013" || group == "Г2014"){
                                if (group == "Г2114") this->group = Groups::g2114;
                                else if(group == "Г2113") this->group = Groups::g2113;
                                else if(group == "Г2013") this->group = Groups::g2013;
                                else this->group = Groups::g2014;
                        }

                        else{
                                cout << "Не подходящее значение" << endl;
                        }
                }

                int getAge(){
                        return this->age;
                }

                void setAge(int age){
                        this->age = age;
                }

                string getName(){
                        return this->name;
                }

                void setName(string name){
                        if(name != "")
                                this->name = name;
                        
                        else cout << "Поле не должно быть пустым" << endl;
                }

};

int main(){
        Student boby;
        boby.setAge(15);
        boby.setName("Бобик");
        boby.setGroup("Г2013");

        cout << "Студент:\n\nВозраст " << boby.getAge() << "\nИмя: " << boby.getName() << "\nГруппа: " << boby.getGroup() << endl;
}