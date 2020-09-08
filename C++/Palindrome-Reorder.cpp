#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int main() {
	string input;
	cin >> input;

	int c[26] = {}, c1;
	for(char d : input)
		++c[d - 'A'];
	for(int i = 0; i < 26; i++)
		c1 += c[i] & 1;
	if (c1 > 1) {
		cout << "NO SOLUTION";
		return 0;
	}

	// Solution possible
	string t;
	for(int i = 0; i < 26; i++) {
		if (c[i] % 2 == 0) {
			// Even counts
			for (int j = 0; j < c[i] / 2; j++) {
				t += (char)('A' + i);
	}}}

	cout << t;

	for (int i = 0; i < 26; i++) {
		if (c[i] & 1) {
			// Odd count
			for (int j = 0; j < c[i]; j++) {
				cout << (char)('A' + i);
			}
		}
	}

	reverse(t.begin(), t.end());
	cout << t;

	return 0;
}
