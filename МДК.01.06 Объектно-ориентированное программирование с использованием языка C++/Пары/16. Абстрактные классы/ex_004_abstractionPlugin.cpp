#include <iostream>
#include <vector>
#include <memory>

using namespace std;

// Интерфейс плагина
class IPlugin{
    public:
        virtual ~IPlugin() = default;
        virtual string name() const = 0;
        virtual void initialize() = 0;
        virtual void run() = 0;
        virtual void shutdown() = 0;
};

// Реализация конкретных плагинов
class LoggerPlugin : public IPlugin{
    public:
        string name() const override {return "Logger";}
        void initialize() override {cout << "[Logger] Создан" << endl;}
        void run() override {cout << "[Logger] Запись лога" << endl;}
        void shutdown() override {cout << "[Logger] Очищен" << endl;}
};

class CachePlugin : public IPlugin{
    private:
        int hit_count = 0;
    
    public:
        string name() const override {return "Cache";}
        void initialize() override {cout << "[Cache] Выделена память" << endl;}
        void run() override{
            hit_count++;
            cout << "[Cache] Проверка кэша (Хитов: " << hit_count << ")" << endl;
        }
        void shutdown() override {cout << "[Cache] Память освобождена" << endl;}
};

class Application {
    private:
        vector<IPlugin*> plugins;
    
    public:
        void register_plugin(IPlugin* plugin){
            plugins.push_back(plugin);
            cout << "Плагин зарегестрирован: " << plugin->name() << endl;
        }

        void start(){
            cout << "Инициализация плагинов" << endl;
            for (auto* p : plugins) p->initialize();
            cout << "Выполнение логики" << endl;
            for (auto* p : plugins) p->run();
            cout << "Остановка" << endl;
        }
};

int main(){
    setlocale(LC_ALL, "ru");
    Application app;

    app.register_plugin(new LoggerPlugin());
    app.register_plugin(new CachePlugin());

    app.start();
}