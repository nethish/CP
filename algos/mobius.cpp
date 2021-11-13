vector<int> mobius(int n) {
  /**
   * -1 if prime, 0 if a^2 divides n, (-1)^k if k distinct primes
   */
  vector<int> mob(n + 1, 0);
  mob[1] = 1;
  for (int i = 1; i <= n; ++i) for (int j = i + i; j <= n; j += i) {
    mob[j] -= mob[i];
  }
  return mob;
}
