#include <bits/stdc++.h>

int main() {
    std::vector<int> sums;
    for (;;) {
        int sum = 0, cnt = 0;
        std::string line;
        while (std::getline(std::cin, line) && !line.empty()) {
            sum += std::stoi(line);
            cnt++;
        }
        if (cnt == 0) {
            break;
        }
        sums.push_back(sum);
    }

    std::sort(sums.begin(), sums.end());
    std::reverse(sums.begin(), sums.end());

    std::cout << sums[0] << "\n" << sums[0] + sums[1] + sums[2] << "\n";
}
