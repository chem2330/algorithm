#include<iostream>
#include<queue>
#include<tuple>

using namespace std;
int costs[16] = {0};
priority_queue<tuple<int, int, int>> pq;

int main() {

	int N;
	cin >> N;
	for (int i = 0; i < N ; i++) {
		int T, P;
		cin >> T >> P;
		if (i + T > N) continue;
		if (costs[i] + P > costs[i + T]) {
			 costs[i + T] = costs[i] + P;
			 for (int j = i + T + 1; j < N + 1; j++) {
				 if (costs[j] < costs[i + T])
					 costs[j] = costs[i + T];
			 }
		}
	}

	cout << costs[N];

	return 0;
}