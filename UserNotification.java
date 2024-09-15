package signupapp;

public interface UserNotification {
    void onSuccess(String username);
    void onFailure(String username);
    void onLoginSuccess(String username);
    void onLoginFailure(String username);
}