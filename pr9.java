import java.util.InputMismatchException;
import java.util.Scanner;

public class pr9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.print("Введите первое целое число: ");
            int num1 = scanner.nextInt();
            System.out.print("Введите второе целое число: ");
            int num2 = scanner.nextInt();
            int result = num1 / num2;
            System.out.println("Результат деления: " + result);
        } catch (InputMismatchException e) {
            System.out.println("Ошибка: введено не число.");
        } catch (ArithmeticException e) {
            System.out.println("Ошибка: деление на ноль.");
        } finally {
            System.out.println("Завершение программы.");
            scanner.close();
        }
    }
}