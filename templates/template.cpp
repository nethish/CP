#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define endl "\n"
#define debug(x) cout << #x << " = " << (x) << endl;
int INF = INT_MAX;
const ll MOD = 1000000007;
 
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
  for (auto &i: map) {
    cout << "[" << i.first << ": " << i.second << "]";
  }
  cout << "}";
  return os;
}
 
void solve() {
}
 
 
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);
 
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}
/* Check long long
 * Facts and data representation
 * Constructive? Top bottom up down
 */
 
