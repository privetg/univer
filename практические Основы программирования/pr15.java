import java.util.Arrays;
import java.util.Random;

public class pr15 {
    public static void main(String[] args) {
        System.out.println("=".repeat(60));
        System.out.println("РАБОТА С МАССИВАМИ");
        System.out.println("=".repeat(60));
        System.out.println();

        demonstrateOneDimensionalArray();

        System.out.println();
        System.out.println("=".repeat(60));

        demonstrateTwoDimensionalArray();

    }



    private static void demonstrateOneDimensionalArray() {
        System.out.println("▶ 1. ОДНОМЕРНЫЙ МАССИВ");
        System.out.println("-".repeat(60));

        int size = 10;
        int[] numbers = createRandomArray(size, 1, 100);

        System.out.println("Сгенерированный массив (размер " + size + "):");
        printArray(numbers);
        System.out.println();

        int[] result = findMinMax(numbers);
        int min = result[0];
        int max = result[1];

        System.out.println("Результаты линейного поиска:");
        System.out.println("  Минимальный элемент: " + min + " (индекс: " + findIndex(numbers, min) + ")");
        System.out.println("  Максимальный элемент: " + max + " (индекс: " + findIndex(numbers, max) + ")");

        System.out.println("\nСтатистика массива:");
        System.out.println("  Сумма элементов: " + sumArray(numbers));
        System.out.println("  Среднее значение: " + averageArray(numbers));
        System.out.println("  Отсортированный массив: " + Arrays.toString(sortArray(numbers)));
    }




    private static void demonstrateTwoDimensionalArray() {
        System.out.println("▶ 2. ДВУМЕРНЫЙ МАССИВ (КВАДРАТНАЯ МАТРИЦА)");
        System.out.println("-".repeat(60));

        int size = 5;
        int[][] matrix = createIdentityMatrix(size);

        System.out.println("Квадратная матрица " + size + "x" + size +
                " (единицы на главной диагонали, нули остальные):");
        printMatrix(matrix);


        System.out.println("\nСвойства матрицы:");
        System.out.println("  Размер: " + size + "x" + size);
        System.out.println("  Количество единиц: " + countOnes(matrix));
        System.out.println("  Количество нулей: " + countZeros(matrix));
        System.out.println("  Является ли единичной: " + (isIdentityMatrix(matrix) ? "Да" : "Нет"));


        System.out.println("  Является ли симметричной: " + (isSymmetric(matrix) ? "Да" : "Нет"));
    }




    private static int[] createRandomArray(int size, int min, int max) {
        Random random = new Random();
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(max - min + 1) + min;
        }
        return array;
    }



    private static void printArray(int[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]);
            if (i < array.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }



    private static int[] findMinMax(int[] array) {
        if (array == null || array.length == 0) {
            throw new IllegalArgumentException("Массив не может быть пустым");
        }

        int min = array[0];
        int max = array[0];

        for (int i = 1; i < array.length; i++) {
            if (array[i] < min) {
                min = array[i];
            }
            if (array[i] > max) {
                max = array[i];
            }
        }

        return new int[]{min, max};
    }



    private static int findIndex(int[] array, int value) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == value) {
                return i;
            }
        }
        return -1;
    }



    private static int sumArray(int[] array) {
        int sum = 0;
        for (int num : array) {
            sum += num;
        }
        return sum;
    }



    private static double averageArray(int[] array) {
        return (double) sumArray(array) / array.length;
    }



    private static int[] sortArray(int[] array) {
        int[] sorted = Arrays.copyOf(array, array.length);
        Arrays.sort(sorted);
        return sorted;
    }



    private static int[][] createIdentityMatrix(int size) {
        int[][] matrix = new int[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                matrix[i][j] = (i == j) ? 1 : 0;
            }
        }

        return matrix;
    }



    private static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }


    private static int countOnes(int[][] matrix) {
        int count = 0;
        for (int[] row : matrix) {
            for (int value : row) {
                if (value == 1) count++;
            }
        }
        return count;
    }



    private static int countZeros(int[][] matrix) {
        int count = 0;
        for (int[] row : matrix) {
            for (int value : row) {
                if (value == 0) count++;
            }
        }
        return count;
    }



    private static boolean isIdentityMatrix(int[][] matrix) {
        int size = matrix.length;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (i == j) {
                    if (matrix[i][j] != 1) return false;
                } else {
                    if (matrix[i][j] != 0) return false;
                }
            }
        }
        return true;
    }



    private static boolean isSymmetric(int[][] matrix) {
        int size = matrix.length;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (matrix[i][j] != matrix[j][i]) {
                    return false;
                }
            }
        }
        return true;
    }

    // ============================================
    // МЕТОД ДЛЯ ТРЕУГОЛЬНИКА ПАСКАЛЯ
    // ============================================


    private static int[][] generatePascalTriangle(int rows) {
        int[][] triangle = new int[rows][];

        for (int i = 0; i < rows; i++) {
            triangle[i] = new int[i + 1];

            triangle[i][0] = 1;
            triangle[i][i] = 1;

            for (int j = 1; j < i; j++) {
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
        }

        return triangle;
    }

}