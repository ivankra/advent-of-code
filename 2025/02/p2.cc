#include <bits/stdc++.h>

using LL = long long;

bool is_invalid(LL x) {
  char s[30];
  sprintf(s, "%lld", x);

  int n = strlen(s);
  for (int k = 1; k < n; k++) {
    if (n % k == 0) {
      int eq = 0;
      for (int i = 0; i < n; i += k) {
        if (memcmp(s, s + i, k) == 0) {
          eq += k;
        }
      }

      if (eq == n) {
        return true;
      }
    }
  }

  return false;
}

int main() {
  LL a, b, ans = 0;

  while (scanf("%lld-%lld,", &a, &b) >= 2) {
    for (LL x = a; x <= b; x++) {
      if (is_invalid(x)) {
        ans += x;
      }
    }
  }

  printf("%lld\n", ans);
}
