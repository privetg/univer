import java.util.Scanner;
import java.util.LinkedHashSet;
import java.util.Arrays;

public class UniqueWords {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] words = input.split(" ");
        LinkedHashSet<String> set = new LinkedHashSet<>(Arrays.asList(words));
        System.out.println(String.join(" ", set));
    }
}