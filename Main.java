package signupapp;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        UserHandler userHandler = new UserHandler();
        Signup signup = new Signup(userHandler);
        Login login = new Login(userHandler);

        while (true) {
            System.out.println("Welcome to Login/Signup Application");
            System.out.println("1. Login");
            System.out.println("2. Signup");
            System.out.println("3. Exit");

            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume newline

            switch (choice) {
                case 1:
                    login.userLogin();
                    break;
                case 2:
                    signup.userSignup();
                    break;
                case 3:
                    System.out.println("Exiting application...");
                    System.exit(0);
                default:
                    System.out.println("Invalid choice, please try again.");
            }
        }
    }
}