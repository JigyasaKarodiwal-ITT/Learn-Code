import java.util.Scanner;

public class Input {
    public static int takeNumber() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a 4-digit number: ");
        int num = scanner.nextInt();
        scanner.close();
        return num;
    }
}
