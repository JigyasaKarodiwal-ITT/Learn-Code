package signupapp;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Signup {
    private final UserHandler userHandler;

    public Signup(UserHandler userHandler) {
        this.userHandler = userHandler;
    }

    public void userSignup() {
        Scanner scanner = new Scanner(System.in);
        try {
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
            System.out.println("User created successfully!");
        } catch (InputMismatchException e) {
            System.out.println("Invalid input format. Please enter valid data.");
        } catch (NoSuchElementException e) {
            System.out.println("Input not found. Please try again.");
        } catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
            e.printStackTrace();
        } finally {
            scanner.close();
            System.exit(1);
        }
    }
}
