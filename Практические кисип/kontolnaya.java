import java.util.Scanner;

public class kontolnaya {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (isPrime(n)) {
            System.out.println(n + " - ïðîñòîå ÷èñëî");
        } else {
            System.out.println(n + " - ñîñòàâíîå ÷èñëî");
        }
    }

    public static boolean isPrime(int n) {
        if (n < 1) return false;
        if (n == 1) return true;
        if (n % 2 == 0) return n == 2;
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
