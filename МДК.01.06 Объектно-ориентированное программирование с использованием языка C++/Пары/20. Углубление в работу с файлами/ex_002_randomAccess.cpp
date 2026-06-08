#include <iostream>     
#include <fstream>      // Библиотека для файлового потока fstream (поддерживает чтение и запись)
#include <vector>       
#include <iomanip>      // Манипуляторы для точного форматирования чисел
using namespace std;  

#pragma pack(push, 1)   // Отключаем выравнивание полей структуры для гарантии точных байтовых смещений
struct Product {        
    char name[20];      
    double price;       
    int quantity;      
};                      
#pragma pack(pop)       // Восстанавливаем стандартное выравнивание структур для остального кода

// Функция создания начального файла с товарами
void create_initial_file(const string& filename) {
    ofstream file(filename, ios::binary | ios::trunc); // Открываем файл для бинарной записи, режим trunc гарантирует очистку старого содержимого
    if (!file) throw runtime_error("Не удалось создать или очистить файл"); 
    vector<Product> products = {                       
        {"Laptop", 1200.50, 10},                       
        {"Mouse", 25.00, 150},                         
        {"Keyboard", 75.99, 50}                        
    };                                                 
    for (const auto& p : products) {                  
        file.write(reinterpret_cast<const char*>(&p), sizeof(Product)); 
    }                                                 
    if (!file) throw runtime_error("Ошибка при записи начальных данных на диск"); 
    file.close();                                     
}                                                      

// Функция обновления цены товара по индексу записи в файле (без перезаписи всего файла)
void update_product_price(const string& filename, int index, double new_price) {
    fstream file(filename, ios::in | ios::out | ios::binary); 
    if (!file) throw runtime_error("Не удалось открыть файл для обновления"); 
    streampos offset = index * sizeof(Product);       
    file.seekp(offset, ios::beg);                      
    if (!file) throw runtime_error("Ошибка позиционирования указателя записи за пределы файла"); 
    Product current;                                   
    file.read(reinterpret_cast<char*>(&current), sizeof(Product)); 
    if (!file) throw runtime_error("Ошибка чтения записи перед обновлением цены"); 
    current.price = new_price;                        
    file.seekp(offset, ios::beg);                      
    file.write(reinterpret_cast<const char*>(&current), sizeof(Product)); 
    if (!file) throw runtime_error("Ошибка записи обновлённой записи на диск"); 
    file.flush();                                     
    file.close();                                  
}                                                 

// Функция чтения и вывода всех товаров из файла с демонстрацией tellg
void print_all_products(const string& filename) {
    ifstream file(filename, ios::binary);             
    if (!file) throw runtime_error("Файл не найден для чтения"); 
    int index = 0;                                     
    Product p;                                         
    while (file.read(reinterpret_cast<char*>(&p), sizeof(Product))) { 
        streampos current_pos = file.tellg();          
        cout << "[" << index << "] "                   
             << "Имя: " << p.name                      
             << " | Цена: $" << fixed << setprecision(2) << p.price 
             << " | Остаток: " << p.quantity           
             << " | Позиция в файле: " << current_pos  
             << endl;                                  
        index++;                                       
    }                                                  
    if (!file.eof()) cout << "Встречена ошибка чтения данных перед концом файла!" << endl;
}                                                      

int main() {                                           
    setlocale(LC_ALL, "Russian");                      
    const string FILE_NAME = "inventory.dat";          
    try {                                              
        create_initial_file(FILE_NAME);                
        print_all_products(FILE_NAME);                 
        update_product_price(FILE_NAME, 1, 29.99);     
        cout << "Цена обновлена" << endl; 
        print_all_products(FILE_NAME);                 
    } catch (const exception& e) {                     
        cerr << "Критическая ошибка: " << e.what() << endl; 
        return 1;                                     
    }                                                  
                                    
}                                                      