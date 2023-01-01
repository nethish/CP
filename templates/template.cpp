#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define endl "\n"
#define dd(x) cout << #x << " = " << (x) << endl;

#define all(x) (x).begin(), (x).end()
#define YES cout << "YES" << endl;
#define NO cout << "NO" << endl; return;

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

template <typename V>
ostream& operator<<(ostream& os, set<V> s) {
  cout << "{";
  for (auto i: s) cout << i << ", " << endl;
  cout << "}";
  return os;
}

template <typename V>
ostream& operator<<(ostream& os, multiset<V> s) {
  cout << "{";
  for (auto i: s) cout << i << ", " << endl;
  cout << "}";
  return os;
}

int dx[] = {-1, 0, 0, 1}, dy[] = {0, 1, -1, 0};

int INF = INT_MAX;
const ll MOD = 1000000007;
// const ll MOD = 998244353;

ll power(ll a, ll p, ll mod=MOD) {
  ll res = 1;
  while (p) {
    if (p & 1) res = (res * a) % mod;
      p >>= 1;
      a = (a * a) % mod;
  }
  return res;
}


void solve() {
  start_here
}
 
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int t = 1;
  cin >> t;
  while (t--) {
    solve();
  }
}
