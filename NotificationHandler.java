package signupapp;

public class NotificationHandler {
    public void onSuccess(String username) {
        System.out.println("Signup successful for user: " + username);
    }

    public void onFailure(String username) {
        System.out.println("Signup failed for user: " + username);
    }
}
