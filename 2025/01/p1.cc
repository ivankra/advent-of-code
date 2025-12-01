#include <bits/stdc++.h>

int main() {
  char dir;
  int n, cur = 50, ans = 0;

  while (scanf(" %c%d", &dir, &n) == 2) {
    for (int i = 0; i < n; i++) {
      if (dir == 'L') cur--; else cur++;
      cur = (cur + 100) % 100;
    }
    if (cur == 0) ans++;
  }

  printf("%d\n", ans);
}
