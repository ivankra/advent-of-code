#include <bits/stdc++.h>
using namespace std;

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

    // state = (pos << N) | (open bitmask) => sum of flow until t=30
    map<uint64_t, int> states;
    states[0] = 0;

    int ans1 = 0;

    for (int t = 0; t < 30; t++) {
        printf("t=%d states=%d\n", t, int(states.size()));

        map<uint64_t, int> next = states;
        for (const auto& it : states) {
            uint64_t st = it.first;
            int u = int(st >> N);
            int res = it.second;

            if (((st & (1ULL << u)) == 0) && rate[u] > 0) {
                // open valve
                uint64_t st1 = st | (1ULL << u);
                int res1 = res + (30-t-1) * rate[u];
                next[st1] = max(next[st1], res1);
                ans1 = max(ans1, res1);
            }

            for (int v : adj[u]) {
                // move u -> v
                uint64_t st1 = (st & ((1ULL << N) - 1)) | (uint64_t(v) << N);
                next[st1] = max(next[st1], res);
            }
        }

        states = next;
    }

    printf("%d\n", ans1);
}
