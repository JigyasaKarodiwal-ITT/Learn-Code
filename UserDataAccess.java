package signupapp;

import java.sql.SQLException;

public interface UserDataAccess {
    boolean addUser(String[] userData) throws SQLException;
    boolean authenticateUser(String username, String password) throws SQLException;
}