#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define endl "\n"
#define debug(x) cout << #x << " = " << (x) << endl;

// UTIL
 
template<class T>
ostream& operator<<(ostream& os, vector<T> v) {
  cout << "[";
  for(auto &i: v) cout << i << ", ";
  cout << "]" << endl;
  return os;
}
 
template <typename K, typename V>
ostream& operator<<(ostream& os, pair<K, V> p) {
  os << "{" << p.first << ", " << p.second << "} ";
  return os;
}

template <typename K, typename V>
ostream& operator<<(ostream& os, map<K, V> m) {
  cout << "{";
  for (auto i = m.begin(); i != m.end(); ++i) {
    cout << "[" << i.first << ": " << i.second << "]";
  }
  cout << "}";
  return os;
}

// ALGOS

int dx[] = {-1, 0, 0, 1}, dy[] = {0, 1, -1, 0};

// -1 if prime, 0 if a^2 divides n, (-1)^k if k distinct primes
vector<int> mobius(int n) { vector<int> mob(n + 1, 0); mob[1] = 1; for (int i = 1; i <= n; ++i) for (int j = i + i; j <= n; j += i) mob[j] -= mob[i]; return mob; }


// Go 
int INF = INT_MAX;
const ll MOD = 1000000007;

void solve() {
}
 
 
int main() {
  ios::sync_with_stdio(false);
  // cin.tie(0); cout.tie(0);
 
  int t = 1;
  cin >> t;
  while (t--) {
    solve();
  }
}
/* Check long long
 * Facts and data representation
 * Constructive? Top bottom up down
 */
 
