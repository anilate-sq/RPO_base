#include <iostream>
#include <vector>
#include <chrono>
#include <numeric>
using namespace std;

const int ROWS = 4000;
const int COLS = 4000;
const int ITERATIONS = 10;

template <typename Func>
double benchmark(Func&& func){
        for(int i = 0; i < 3; i++) func();
        vector<long long> times;
        for(int i = 0; i < ITERATIONS; i++){
                auto start = chrono::high_resolution_clock::now();
                func();
                auto end = chrono::high_resolution_clock::now();
                times.push_back(chrono::duration_cast<chrono::microseconds>(end-start).count());
        }
        long long sum = accumulate(times.begin(), times.end(), 0LL);
        return static_cast<double>(sum)/ times.size();
}

void row_major_traversal(const vector<vector<int>>& mat){
        volatile long long sum = 0;
        for (size_t r = 0; r < ROWS; r++){
                for(size_t c = 0; c < COLS; c++){
                        sum += mat[r][c];
                }
        }
}

void col_major_traversal(const vector<vector<int>>& mat){
        volatile long long sum = 0;
        for (size_t c = 0; c < COLS; c++){
                for(size_t r = 0; r < ROWS; r++){
                        sum += mat[r][c];
                }
        }
}

int main(){
        setlocale(LC_ALL, "ru");
        cout << "Матрица: " << ROWS << "x" << COLS << endl;
        vector<vector<int>> mat(ROWS, vector<int>(COLS));
        for(auto& row : mat){
                for (auto& val : row) val = 1;
        }

        double t_row = benchmark([&]{ row_major_traversal(mat);});
        cout << "\n Обход со строками: " << t_row << " мс" << endl;
        
        double t_col = benchmark([&]{ col_major_traversal(mat);});
        cout << "\n Обход со строками: " << t_col << " мс" << endl;

        cout << "\n Сравнение: " << (t_col / t_row) << "x" << endl;
}