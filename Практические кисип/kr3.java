import java.util.*;

public class kr3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] tokens = sc.nextLine().split(" ");
        int n = tokens.length;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = Integer.parseInt(tokens[i]);

        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;

        Arrays.sort(idx, (a, b) -> {
            int sa = digitSum(nums[a]);
            int sb = digitSum(nums[b]);
            return sa != sb ? Integer.compare(sa, sb) : Integer.compare(a, b);
        });

        for (int i = 0; i < n; i++) {
            System.out.print(nums[idx[i]] + (i == n - 1 ? "" : " "));
        }
    }

    private static int digitSum(int x) {
        int s = 0;
        while (x > 0) {
            s += x % 10;
            x /= 10;
        }
        return s;
    }
}