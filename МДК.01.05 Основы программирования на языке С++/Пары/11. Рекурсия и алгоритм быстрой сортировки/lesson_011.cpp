#include <iostream>
#include <vector>

using namespace std;

template <typename ... Args> // Шаблом перечня аргументов
void printMessage(Args... args) {
	(cout << ... << args) << endl;
}

/// <summary>
/// Подсчет суммы элементов массива, используя рекурсию
/// </summary>
/// <param name="arr"></param>
/// <param name="count"></param>
/// <returns></returns>
int sum(int arr[], int count) {
	if (count == 0) {
		return 0; // Условия выхода/Базовый случай
	}
	return arr[count - 1] + sum(arr, count - 1);
}

void quickSort(vector<int> &arr, int left, int right) {
	int i = left, j = right;
	int pivot = arr[(left + right) / 2];
	while (i <= j) {
		while (arr[i] < pivot) i++;
		while (arr[j] > pivot) j++;
		if (i <= j) swap(arr[i++], arr[j--]);
	}

	if (left < j) quickSort(arr, left, j);
	if (i < right) quickSort(arr, i, right);
}


int binarySearch(const vector<int>& arr, int left, int right, int target) {
	if (left > right) return -1; // Базовый случай

	int mid = (left + right) / 2;

	if (arr[mid] == target) {
		return mid;
	}

	else if (arr[mid] > target) {
		return binarySearch(arr, left, mid - 1, target);
	}
	else {
		return binarySearch(arr, mid + 1, right, target);
	}
}

int main()
{
	int testArr[] = { 1, 2, 3, 4, 5 };
	cout << sum(testArr, 5);

	vector<int> data = { 10, 7, 2, 8, 6, 1, 5 };
	quickSort(data, 0, data.size() - 1);
	for (int item : data) {
		cout << item;
	}

	printMessage("Сообщение: ", 1, "- что-то на важном");
}

