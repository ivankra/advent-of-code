#include <bits/stdc++.h>

using LL = long long;

bool is_invalid(LL x) {
  char s[30];
  sprintf(s, "%lld", x);

  int n = strlen(s);
  return n % 2 == 0 && memcmp(s, s + n / 2, n / 2) == 0;
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
