package signupapp;
import java.util.Scanner;

public class Signup {
    private UserHandler userHandler;

    public Signup(UserHandler userHandler) {
        this.userHandler = userHandler;
    }

    public void userSignup() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your username:");
        String username = scanner.nextLine();
        System.out.println("Enter your date of birth (DOB) in YYYY-MM-DD format:");
        String dob = scanner.nextLine();
        System.out.println("Enter your email:");
        String email = scanner.nextLine();
        System.out.println("Enter your password:");
        String password = scanner.nextLine();

        String[] userData = {username, dob, email, password};
        userHandler.createNewUser(userData);
    }
}