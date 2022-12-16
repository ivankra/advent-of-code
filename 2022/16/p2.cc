#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace std;

struct CHash {
  static inline size_t seed = chrono::high_resolution_clock::now().time_since_epoch().count() * (size_t)&errno;
  static size_t mix(size_t x) { x *= 0xff51afd7ed558ccdull; return x + (x >> 32); }

  template<typename T>
  decltype(hash<T>()(declval<T>())) operator()(const T& x) const { return mix(hash<T>()(x) + seed); }

  template<typename... T>
  size_t operator()(const tuple<T...>& x) const {
    return apply([this](const auto&... v) {
      size_t h = 0;
      return ((h = h * 31 + (*this)(v)), ...);
    }, x);
  }
};
template<class K, class V> using hash_map = __gnu_pbds::gp_hash_table<K, V, CHash>;

vector<string> SplitString(string s, string sep) {
    vector<string> res;
    size_t i = 0;
    while (i < s.size()) {
        size_t j = s.find(sep, i);
        if (j == string::npos) break;
        res.push_back(s.substr(i, j - i));
        i = j + sep.size();
    }
    res.push_back(s.substr(i));
    return res;
}

int main() {
    int N = 0;
    map<string, int> name2id;
    vector<int> adj[64], rate(64);

    auto get_index = [&](string name) {
        if (name2id.count(name) == 0) name2id[name] = N++;
        return name2id[name];
    };
    get_index("AA");

    regex re("Valve ([A-Z]+) has flow rate=(\\d+); tunnels? leads? to valves? ([A-Z, ]+)");
    string line;
    while (getline(cin, line)) {
        smatch m;
        assert(regex_search(line, m, re));
        string u = m[1];
        rate[get_index(u)] = stoi(m[2]);
        for (string v : SplitString(m[3], ", ")) {
            adj[get_index(u)].push_back(get_index(v));
        }
    }
    printf("N=%d\n", N);

    using State = tuple<int, int, uint64_t>;  // pos1, pos2, bitmask of open valves
    hash_map<State, int> states;  // state => sum of flow until t=26
    states[State(0, 0, 0)] = 0;

    int ans2 = 0;

    for (int t = 0; t < 26; t++) {
        printf("t=%d states=%d\n", t, int(states.size()));

        hash_map<State, int> next = states;
        for (const auto& it : states) {
            auto [u1, u2, open0] = it.first;
            int res0 = it.second;

            // brute force action for both player
            // 0=stay, 1=open valve, 2+i=move to adj[u][i]
            for (int a1 = 0; a1 < 2 + adj[u1].size(); a1++)
            for (int a2 = 0; a2 < 2 + adj[u2].size(); a2++) {
                int v1 = u1, v2 = u2, res = res0;
                uint64_t open = open0;

                // player 1
                if (a1 == 1 && rate[u1] > 0 && (open & (1ULL << u1)) == 0) {
                    // open valve
                    open |= 1ULL << u1;
                    res += (26 - t - 1) * rate[u1];
                }
                if (a1 >= 2) {
                    // move
                    v1 = adj[u1][a1-2];
                }

                // player 2
                if (a2 == 1 && rate[u2] > 0 && (open & (1ULL << u2)) == 0) {
                    // open valve
                    open |= 1ULL << u2;
                    res += (26 - t - 1) * rate[u2];
                }
                if (a2 >= 2) {
                    // move
                    v2 = adj[u2][a2-2];
                }

                State st(v1, v2, open);
                next[st] = max(next[st], res);
                ans2 = max(ans2, res);
            }
        }

        states = next;
    }

    printf("%d\n", ans2);
}
