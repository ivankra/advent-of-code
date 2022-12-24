#include <bits/stdc++.h>
using namespace std;
using LL = long long;
using State = array<int, 3>;  // (y,x,c)

vector<string> A;
int H, W, CL;

int main() {
  string line;
  H = 0;
  while (getline(cin, line)) {
    A.push_back(line);
    H++;
  }
  W = A[0].size();
  CL = (W-2)*(H-2);

  int xS=-1, xE=-1;
  for (int i = 0; i < W; i++) {
    if (A[0][i] == '.') xS = i;
    if (A[H-1][i] == '.') xE = i;
  }

  State st = {0, xS, 0};

  map<State, int> dist;
  dist[st] = 0;

  queue<State> Q;
  Q.push(st);

  while (!Q.empty()) {
    st = Q.front(); Q.pop();
    if (st[0] == H-1 && st[1] == xE) {
      printf("%d\n", dist[st]);
      break;
    }

    for (int d = 0; d < 5; d++) {
      static int DY[] = {0,1,-1,0,0};
      static int DX[] = {0,0,0,1,-1};
      int y = st[0] + DY[d];
      int x = st[1] + DX[d];
      int c = (st[2] + 1) % CL;
      if (y < 0 || y >= H || x < 0 || x >= W || A[y][x] == '#') continue;

      bool good = true;
      for (int i = 1; i <= H-1 && good; i++) {
        int p = H-2;
        if (A[i][x] == 'v') {
          int ii = 1 + (i-1 + c) % p;
          if (ii == y) good = false;
        }
        if (A[i][x] == '^') {
          int ii = 1 + (i-1 - c%p + p*100) % p;
          if (ii == y) good = false;
        }
      }
      for (int j = 1; j <= W-1 && good; j++) {
        int p = W-2;
        if (A[y][j] == '>') {
          int jj = 1 + (j-1 + c) % p;
          if (jj == x) good = false;
        }
        if (A[y][j] == '<') {
          int jj = 1 + (j-1 - c%p + p*100) % p;
          if (jj == x) good = false;
        }
      }
      if (!good) continue;

      State st1 = {y,x,c};
      if (dist.count(st1) != 0) continue;

      dist[st1] = dist[st] + 1;
      Q.push(st1);
    }
  }



}
