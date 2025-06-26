class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length;

        // Add 1 padding at the beginning and end
        int[] newNums = new int[n + 2];
        newNums[0] = 1;
        newNums[n + 1] = 1;
        for (int i = 0; i < n; i++) {
            newNums[i + 1] = nums[i];
        }

        // DP table: dp[i][j] = max coins we can collect from i to j (exclusive)
        int[][] dp = new int[n + 2][n + 2];

        // We build the table bottom-up
        // length is the size of the interval
        for (int length = 2; length <= n + 1; length++) {
            for (int left = 0; left <= n + 1 - length; left++) {
                int right = left + length;
                for (int i = left + 1; i < right; i++) {
                    int coins = newNums[left] * newNums[i] * newNums[right];
                    coins += dp[left][i] + dp[i][right]; // coins from subproblems
                    dp[left][right] = Math.max(dp[left][right], coins);
                }
            }
        }

        // The final answer is the max coins between 0 and n+1 (exclusive)
        return dp[0][n + 1];

    }
}