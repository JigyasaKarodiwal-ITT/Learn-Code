package signupapp;


public class UserHandler {
    private DataBaseHandler dataBaseHandler;
    private NotificationHandler notificationHandler;

    public UserHandler() {
        this.dataBaseHandler = new DataBaseHandler();
        this.notificationHandler = new NotificationHandler();
    }

    public void createNewUser(String[] userData) {
        if (dataBaseHandler.addUser(userData)) {
            notificationHandler.onSuccess(userData[0]);
        } else {
            notificationHandler.onFailure(userData[0]);
        }
    }

    public boolean authenticateUser(String username, String password) {
        return dataBaseHandler.authenticateUser(username, password);
    }
}
