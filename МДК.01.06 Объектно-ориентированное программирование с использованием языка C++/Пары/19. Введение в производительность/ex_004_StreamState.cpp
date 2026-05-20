#include <iostream>  
#include <vector>       
#include <chrono>       
#include <algorithm>    
#include <numeric>     
#include <random>       
using namespace std;    

constexpr size_t SIZE = 10000000; 
constexpr size_t SEARCHES = 100000; 

int linear_search(const vector<int>& arr, int target) { 
    for (size_t i = 0; i < arr.size(); ++i) 
        if (arr[i] == target) return i; 
    return -1; 
}

int binary_search_manual(const vector<int>& arr, int target) {
    int l = 0, r = arr.size() - 1; 
    while (l <= r) { 
        int m = l + (r - l) / 2; 
        if (arr[m] == target) return m; 
        else if (arr[m] < target) l = m + 1;
        else r = m - 1;
    }
    return -1;
}

template <typename Func> 
double benchmark(Func&& func) {     
    for (int i = 0; i < 2; ++i) func();
    auto start = chrono::high_resolution_clock::now();
    func();
    auto end = chrono::high_resolution_clock::now();
    return chrono::duration_cast<chrono::milliseconds>(end - start).count();
}

int main(){
    setlocale(LC_ALL, "Russian");
    
    vector<int> arr(SIZE);          
    iota(arr.begin(), arr.end(), 0); 
    
    vector<int> targets(SEARCHES);  
    for (size_t i = 0; i < SEARCHES; ++i) 
        targets[i] = (i % 2 == 0) ? (rand() % SIZE) : (SIZE + rand() % 1000); 
    
    auto test_func = [&](auto search_fn, const string& name) { 
        volatile int dummy = 0;     
        auto fn = [&]{             
            for (int t : targets) dummy += search_fn(arr, t); 
        };
        double time = benchmark(fn); 
        cout << name << ": " << time << " мс" << endl;
    };

    test_func(linear_search, "Linear Search O(N)"); 
    test_func(binary_search_manual, "Manual Binary O(log N)"); 
    test_func([](const vector<int>& a, int t){ return binary_search(a.begin(), a.end(), t) ? 1 : 0; },
              "std::binary_search O(log N)");
    return 0;                      
}