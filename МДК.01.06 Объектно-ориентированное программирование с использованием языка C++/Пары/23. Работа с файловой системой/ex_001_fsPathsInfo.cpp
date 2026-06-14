#include <iostream>
#include <filesystem> // Стандартная библиотека файловой системы C++17
#include <chrono>
#include <iomanip>

using namespace std; 
namespace fs = std::filesystem;

int main(){
        setlocale(LC_ALL,  "ru");
        fs::path current_dir = fs::current_path();
        cout << "Текущая директория: " << current_dir << endl;
        fs::path demo_file = current_dir / "demo_data.txt";
        cout << "Целевой путь:  " << demo_file << endl;
        if (fs::exists(demo_file)){
                cout << "Файл существует";
        } else{
                cout << "Файл не найден";
        }
        fs::path parent = demo_file.parent_path();
        fs::path filename = demo_file.filename();
        fs::path stem = demo_file.stem();
        fs::path ext = demo_file.extension();
        cout << "Родитель: " << parent << endl;
        cout << "Полное имя: " << filename << endl;
        cout << "Корень: " << stem << endl;
        std::error_code ec;
        auto file_size = fs::file_size(demo_file, ec);
        if(ec){
                cerr << "Ошибка чтения: " << ec.message() << endl;
        }
        else {
                cout << "Размер файла" << file_size << endl;
        }
        auto write_time = fs::last_write_time(demo_file, ec);
        if(!ec){
                auto sctp = chrono::time_point_cast<chrono::system_clock::duration>(write_time);
                auto tt = chrono::system_clock::to_time_t(sctp);
                cout << "Последнее изменение: " << put_time(std::localtime(&tt), "%Y-%m-%d %H:%M:%S") << endl;
        }
        if(fs::is_regular_file(demo_file)) cout << "Обычный файл" << endl;
        else if(fs::is_directory(demo_file))  cout << "Директория" << endl;
        else if (fs::is_symlink(demo_file)) cout << "Символисческая ссылка" << endl;
        else cout << "Неизвестный тип" << endl;
}
 