package signupapp;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        UserDataAccess dataAccess = new DatabaseHandler(); 
        UserNotification notification = new NotificationHandler(); 
        UserHandler userHandler = new UserHandler(dataAccess, notification);
        Signup signup = new Signup(userHandler);
        Login login = new Login(userHandler);

        runApplication(scanner, signup, login);
    }

    private static void runApplication(Scanner scanner, Signup signup, Login login) {
        while (true) {
            printMenu();
            int choice = getUserChoice(scanner);
            
            switch (choice) {
                case 1:
                    login.userLogin();
                    break;
                case 2:
                    signup.userSignup();
                    break;
                case 3:
                    exitApplication();
                    break;
                default:
                    displayInvalidChoiceMessage();
            }
        }
    }

    private static void printMenu() {
        System.out.println("Welcome to Login/Signup Application");
        System.out.println("1. Login");
        System.out.println("2. Signup");
        System.out.println("3. Exit");
    }

    private static int getUserChoice(Scanner scanner) {
        System.out.print("Enter your choice: ");
        return scanner.nextInt();
    }

    private static void exitApplication() {
        System.out.println("Exiting application");
        System.exit(0);
    }

    private static void displayInvalidChoiceMessage() {
        System.out.println("Invalid choice, please try again.");
    }
}
