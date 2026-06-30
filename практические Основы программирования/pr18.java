import java.util.Scanner;

public class pr18 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Программа агрегации данных в матрице");
        System.out.println("------------------------------------");

        int[][] matrix = new int[3][3];

        System.out.println("Введите 9 целых чисел для заполнения матрицы 3x3:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.printf("Элемент [%d][%d]: ", i, j);
                matrix[i][j] = scanner.nextInt();
            }
        }

        System.out.println();
        System.out.println("Введенная матрица:");
        printMatrix(matrix);
        System.out.println();

        int sum = 0;

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                sum += matrix[i][j];
            }
        }

        System.out.println("Сумма всех элементов матрицы: " + sum);

        int elementsCount = matrix.length * matrix[0].length;
        System.out.println("Количество элементов: " + elementsCount);
        System.out.printf("Среднее арифметическое: %.2f%n", (double) sum / elementsCount);

        scanner.close();
    }

    private static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.printf("%5d", matrix[i][j]);
            }
            System.out.println();
        }
    }
}