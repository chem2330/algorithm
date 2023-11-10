#include<iostream>
#include<algorithm>


using namespace std;
int arr[10] = { 0 };

int main() {
    int N;
    cin >> N;

    while (N != 0) {
        int tmp = N % 10;
        if (tmp == 9) {
            tmp = 6;
        }
        arr[tmp]++;
        N /= 10;
    }
    
    if (arr[6] % 2 == 0) {
        arr[6] = arr[6] / 2;
    }
    else {
        arr[6] = (arr[6] / 2 + 1);
    }
    
    int max = *max_element(begin(arr), end(arr));    

	cout << max;
}