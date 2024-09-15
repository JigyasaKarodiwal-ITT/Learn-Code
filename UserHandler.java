package signupapp;

import java.sql.SQLException;

public class UserHandler {
    private final UserDataAccess dataAccess;
    private final UserNotification notification;

    public UserHandler(UserDataAccess dataAccess, UserNotification notification) {
        this.dataAccess = dataAccess;
        this.notification = notification;
    }

    public void createNewUser(String[] userData) {
        try {
            if (dataAccess.addUser(userData)) {
                notification.onSuccess(userData[0]);
            } else {
                notification.onFailure(userData[0]);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public boolean authenticateUser(String username, String password) {
        try {
            return dataAccess.authenticateUser(username, password);
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    public void notifyLoginSuccess(String username) {
        notification.onLoginSuccess(username);
    }

    public void notifyLoginFailure(String username) {
        notification.onLoginFailure(username);
    }
}
