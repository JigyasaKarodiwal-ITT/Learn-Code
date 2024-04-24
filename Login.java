package signupapp;

import java.util.Scanner;

public class Login implements UserInteraction {
    private final UserHandler userHandler;

    public Login(UserHandler userHandler) {
        this.userHandler = userHandler;
    }

    @Override
    public void userLogin() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your username:");
        String username = scanner.nextLine();
        System.out.println("Enter your password:");
        String password = scanner.nextLine();

        if (userHandler.authenticateUser(username, password)) {
            userHandler.notifyLoginSuccess(username);
        } else {
            userHandler.notifyLoginFailure(username);
        }
    }
    	
    @Override
    public void userSignup() {
     
    }
}
