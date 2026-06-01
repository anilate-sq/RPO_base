#include <iostream>     
#include <fstream>      // Файловые потоки
#include <sstream>      // Строковые потоки для удобного парсинга текста
#include <string>       
#include <vector>       
#include <stdexcept>    // Классы исключений
#include <memory>       // Умные указатели (для управления кастомным буфером)
using namespace std;    

// Функция создания тестового лог-файла с разными форматами строк
void create_messy_log(const string& filename) {
    ofstream file(filename);                       
    if (!file) throw runtime_error("Не удалось создать лог-файл"); 
    file << "INFO|2024-05-20|Сервер запущен\n";    
    file << "ERROR|2024-05-21|Отказ диска\n";      
    file << "MALFORMED_LINE_WITHOUT_DELIMITER\n";  
    file << "WARN|2024-05-22|Высокая нагрузка\n";  
    file.close();                                  
}                                                  

// Функция парсинга лога с продвинутой обработкой состояний потока и кастомным буфером
void parse_log_advanced(const string& filename) {
    ifstream file;                                 
    unique_ptr<char[]> buffer = make_unique<char[]>(8192); 
    file.rdbuf()->pubsetbuf(buffer.get(), 8192);   
    if (!file) throw runtime_error("Файл не найден: " + filename); 

    // Включаем автоматическое преобразование ошибок потока в исключения C++
    file.exceptions(ifstream::failbit | ifstream::badbit); 
    try {                                          
        string line;                               
        int line_number = 0;                       
        while (getline(file, line)) {              
            line_number++;                         
            istringstream iss(line);               
            string level, date, message;           
            if (getline(iss, level, '|') &&        
                getline(iss, date, '|') &&         
                getline(iss, message)) {           
                cout << "[" << level << "] "    
                     << date << " -> " << message 
                     << " (строка " << line_number << ")" << endl; 
            } else {                               
                cout << "Пропущена битая строка #" << line_number << ": " << line << endl; 
            }                                     
        }                                         
    } catch (const ios_base::failure& e) {         
        if (file.eof()) {                         
            // Ничего не делаем, EOF ожидается при штатном завершении цикла getline, исключение игнорируется
        } else {                                  
            cerr << "Аппаратная ошибка чтения потока: " << e.what() << endl; 
        }                                          
    }                                              

    file.clear();                                  
    cout << "\nПарсинг завершён. Поток очищен и готов к новым операциям." << endl; 
}                                                 

int main() {                                    
    setlocale(LC_ALL, "Russian");                  
    const string LOG_FILE = "system.log";          
    try {                                          
        create_messy_log(LOG_FILE);                
        cout << "Файл создан. Начинаем анализ...\n" << endl;
        parse_log_advanced(LOG_FILE);              
    } catch (const exception& e) {                 
        cerr << "Непредвиденная ошибка: " << e.what() << endl; 
        return 1;                                  
    }                                              
}                                                 