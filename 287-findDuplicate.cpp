#include <iostream>
#include <vector>
using namespace std;

int findDuplicate(vector<int>& nums);

int main() {
    int n;
    cin >> n;
    vector<int> nums;
    for (int i=0; i<n+1; i++) {
        int val;
        cin >> val;
        nums.push_back(val);
    }
    int ans;
    ans = findDuplicate(nums);
    cout << ans << endl;
    return 0;
}

int findDuplicate(vector<int>& nums) {
    // two pointers tech, slow and fast pointer
    // simulate linked list to find the circle entry
    // each time, slow pointer goes one step, fast goes two
    // until they meet
    int slow = 0, fast = 0;
    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (slow != fast);

    // let slow pointer begin at the first place
    // then two pointer both goes one step until they meet
    // the place they meet is the duplicate number we need
    slow = 0;
    while (slow != fast) {
        slow = nums[slow];
        fast = nums[fast];
    }
    return slow;
}
