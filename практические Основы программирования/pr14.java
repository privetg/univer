public class pr14 {
    public static void main(String[] args) {
        System.out.println("=== Параллельное выполнение задач ===");
        System.out.println("Главный поток: " + Thread.currentThread().getName());
        System.out.println("Запуск потоков...");
        System.out.println("=".repeat(50));
        System.out.println();

        Thread numberThread = new Thread(new NumberTask(), "NumberThread");
        Thread letterThread = new Thread(new LetterTask(), "LetterThread");

        numberThread.start();
        letterThread.start();

        System.out.println("Статус потоков после запуска:");
        System.out.println("NumberThread: " + numberThread.getState());
        System.out.println("LetterThread: " + letterThread.getState());
        System.out.println();

        try {
            numberThread.join();
            letterThread.join();
        } catch (InterruptedException e) {
            System.err.println("Главный поток был прерван: " + e.getMessage());
        }

        System.out.println();
        System.out.println("=".repeat(50));
        System.out.println("Все задачи завершены!");
    }
}


class NumberTask implements Runnable {
    @Override
    public void run() {
        String threadName = Thread.currentThread().getName();
        System.out.println("[Номерной поток] " + threadName + " - запущен");

        try {
            for (int i = 1; i <= 5; i++) {
                System.out.println("[ЧИСЛО] " + i + " (поток: " + threadName + ")");
                Thread.sleep(500);
            }
        } catch (InterruptedException e) {
            System.err.println("[Номерной поток] Был прерван!");
            Thread.currentThread().interrupt();
        }

        System.out.println("[Номерной поток] " + threadName + " - завершен");
    }
}


class LetterTask implements Runnable {
    @Override
    public void run() {
        String threadName = Thread.currentThread().getName();
        System.out.println("[Буквенный поток] " + threadName + " - запущен");

        try {
            for (char c = 'A'; c <= 'E'; c++) {
                System.out.println("[БУКВА] " + c + " (поток: " + threadName + ")");
                Thread.sleep(700);
            }
        } catch (InterruptedException e) {
            System.err.println("[Буквенный поток] Был прерван!");
            Thread.currentThread().interrupt();
        }

        System.out.println("[Буквенный поток] " + threadName + " - завершен");
    }
}