package signupapp;

import java.util.Scanner;

public class Login {
    private UserHandler userHandler;

    public Login(UserHandler userHandler) {
        this.userHandler = userHandler;
    }

    public void userLogin() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your username:");
        String username = scanner.nextLine();
        System.out.println("Enter your password:");
        String password = scanner.nextLine();

        if (userHandler.authenticateUser(username, password)) {
            System.out.println("Login successful for user: " + username);
        } else {
            System.out.println("Login failed. Invalid username or password.");
        }
    }
}
