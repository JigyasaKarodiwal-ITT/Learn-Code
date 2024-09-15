package signupapp;

public class NotificationHandler implements UserNotification {
    @Override
    public void onSuccess(String username) {
        System.out.println("Signup successful for user: " + username);
    }

    @Override
    public void onFailure(String username) {
        System.out.println("Signup failed for user: " + username);
    }

    public void onLoginSuccess(String username) {
        System.out.println("Login successful for user: " + username);
    }

    public void onLoginFailure(String username) {
        System.out.println("Login failed for user: " + username);
    }
}
