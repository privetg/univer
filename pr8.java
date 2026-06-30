import java.util.ArrayList;
import java.util.Collections;

public class pr8 {
    public static void main(String[] args) {
        ArrayList<String> tasks = new ArrayList<>();

        tasks.add("покушать");
        tasks.add("погулять с собакой");
        tasks.add("покормить кошку");

        System.out.println("Список задач:");
        for (String task : tasks) {
            System.out.println(task);
        }

        tasks.remove(1);
        System.out.println("\nПосле удаления второй задачи:");
        for (String task : tasks) {
            System.out.println(task);
        }

        String searchTask = "покушать";
        if (tasks.contains(searchTask)) {
            System.out.println("\nЗадача \"" + searchTask + "\" найдена в списке.");
        } else {
            System.out.println("\nЗадача \"" + searchTask + "\" отсутствует в списке.");
        }

        Collections.sort(tasks);
        System.out.println("\nОтсортированный список:");
        for (String task : tasks) {
            System.out.println(task);
        }
    }
}