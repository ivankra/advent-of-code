#include <bits/stdc++.h>

using LL = long long;

LL pow10(int k) {
  LL res = 1;
  for (int i = 0; i < k; i++) {
    res *= 10;
  }
  return res;
}

int main() {
  std::string line;
  LL ans1 = 0, ans2 = 0;

  while (std::cin >> line) {
    int n = line.size();

    int m = -1;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        m = std::max(m, (line[i] - '0') * 10 + (line[j] - '0'));
      }
    }
    ans1 += m;

    // dp_i[k] = max k-digit number using line[i..n-1] or -1
    LL dp[13];
    memset(dp, 0xff, sizeof(dp));

    dp[0] = 0;

    for (int i = n - 1; i >= 0; i--) {
      for (int k = 12; k >= 1; k--) {
        if (dp[k - 1] != -1) {
          dp[k] = std::max(dp[k], dp[k-1] + (line[i] - '0') * pow10(k - 1));
        }
      }
    }

    if (dp[12] != -1) {
      ans2 += dp[12];
    }
  }

  printf("%lld %lld\n", ans1, ans2);
}
