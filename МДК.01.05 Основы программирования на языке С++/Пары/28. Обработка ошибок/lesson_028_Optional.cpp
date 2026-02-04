#include <iostream>
#include <stdexcept>
#include <fstream>
#include <optional>
#include <vector>

using namespace std;

optional<int> findPositive(const vector<int>&  v){  
    for(int x : v){
        if(x > 0) return x;
    }
    return nullopt;
}

int main(){                                             
    // std::optional
    vector<int> v = {-1, -1, -1, -1, 1};
    auto result = findPositive(v);
    if(result){
        cout << *result;
    }
}                                                               