#include <iostream>
#include <vector>
using namespace std;

// Алгоритм разделения строки 1:
vector<string> split(const string&s, char delim){
	vector<string> res;
	string cur;

	for(char c : s){
		if (c == delim){
			res.push_back(cur);
			cur.clear();
		} else{
			cur += c;
		}
	}
	res.push_back(cur);
	return res;
}

// Алгоритм разделения строки 2:
vector<string_view> split_sv(string_view s, char delim){
	vector<string_view> res;
	size_t start = 0;

	while(true){
		size_t pos = s.find(delim, start);
		if (pos == string_view::npos){
			res.push_back(s.substr(start));
			break;
		}
		res.push_back(s.substr(start, pos-start));
		start = pos + 1;
	}
	return res;
}

int main(){
	// Подстроки и разделение строки(sbstr и split)
	
	// Подстроки
	string s = "hello world";
	string sub = s.substr(6, 5); // с 6 позиции выделяем 5 символов

	// Способ разделения 1:
	for(auto i : split(s, ' ')){
		cout << i << endl;
	};

	// Способ разделения 2:
	string_view sv = "Текстовая надпись";
	for(auto i : split_sv(sv, ' ')){
		cout << i << endl;
	};
	

}