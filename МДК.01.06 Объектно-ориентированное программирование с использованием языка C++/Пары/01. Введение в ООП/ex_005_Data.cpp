#include <iostream>
#include <vector>

using namespace std;

struct Author{
    string name;
    int birthday;
    string description; 
};

class Book{

    private:
        string ISBN;
    
    public:
        string name;
        vector<string> jenres;
        Author author;

    void showBook(){
        cout << "Книга: " << name << "\nАвтор: " << author.name << "\nОсновной жанр: " << jenres[0] << endl;
    }
};

int main(){
    //Создаем книжку и автора
    Author Oruell{"Джордж Оруэлл", 1903, "Британский писатель"};
    Book book;
    book.jenres = {"Драма", "Роман"};
    book.author = Oruell;
    book.name = "1984";

    book.showBook();
}
