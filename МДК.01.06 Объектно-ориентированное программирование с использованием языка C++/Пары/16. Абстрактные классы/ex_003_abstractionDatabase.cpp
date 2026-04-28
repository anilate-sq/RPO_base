#include <iostream>
#include <vector>
#include <memory>

using namespace std;

// Интерфейс БД
class IDatabase {
    public:
        virtual bool connect(const string& host) = 0;
        virtual string query(const string& sql) = 0;
        virtual void disconnect() = 0;
        virtual string get_driver_name() const = 0;
        virtual ~IDatabase() = default;
};

// Реализация MySQL
class MySQLDriver : public IDatabase{
    private:
        bool connected = false;
        string current_host;
    public:
        bool connect (const string& host) override {
            cout << "[MySQL] Подключен к " << host << endl;
            current_host = host;
            connected = true;
            return true;
        }

        string query(const string& sql) override {
            if (!connected) return "Ошибка! Отсутсвует подключение";
            cout << "[MySQL] Выполняем: " << sql << endl;
            return "Запрос выполнен успешно";
        }

        void disconnect() override{
            cout << "[MySQL] Отключение от " << current_host << endl;
            connected = false;
        }

        string get_driver_name() const override {return "MySQL 8.0";}
};

// Реализация PostgreSQL
class PostgresDriver : public IDatabase{
    private:
        bool connected = false;
    public:
        bool connect(const string & host) override {
            cout << "[PG] Подключение к " << host << endl;
            connected = true;
            return true;
        }

        string query(const string& sql) override {
            if(!connected) return "Ошибка! Отсутствует подключение";
            cout << "[PG] Выполняем: " << sql << endl;
            return "Запрос выполнен успешно";
        }

        void disconnect() override{
            cout << "[PG] Отключение" << endl;
            connected = false;
        }

        string get_driver_name() const override {return "PostgreSQL 14";}
};

// Симуляция бизнес-логики, работаящая с абстракцией
class UserRepository{
    private:
        IDatabase& db; // Ссылка на интерфейс

    public:
        // explicit - модификатор запрещающий неявные преобразования в конструкторе
        explicit UserRepository(IDatabase& database) : db(database){}
    
        void load_users(){
            string result = db.query("SELECT * from users");
            cout << "Ответ БД: " << result << endl;
        }

};

int main(){
    setlocale(LC_ALL, "ru");
    MySQLDriver mysql;
    mysql.connect("localhost:3306");

    UserRepository repo_mysql(mysql);
    repo_mysql.load_users();
    mysql.disconnect();

    PostgresDriver pg;
    pg.connect("localhost:5432");

    UserRepository repo_pg(pg);
    repo_pg.load_users();
    pg.disconnect();
}