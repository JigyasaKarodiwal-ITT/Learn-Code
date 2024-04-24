package signupapp;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DatabaseHandler implements UserDataAccess{
    private Connection getConnection() throws SQLException {
        return new DatabaseConnection().getConnection();
    }

    public boolean addUser(String[] userData) {
        if (userData.length != 4) {
            System.out.println("Invalid user data format.");
            return false;
        }

        String sql = "INSERT INTO users (username, dob, email, password) VALUES (?, ?, ?, ?)";

        try (Connection connection = getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, userData[0]);
            preparedStatement.setString(2, userData[1]);
            preparedStatement.setString(3, userData[2]);
            preparedStatement.setString(4, userData[3]);
            int rowsAffected = preparedStatement.executeUpdate();
            return rowsAffected > 0;
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    public boolean authenticateUser(String username, String password) {
        String sql = "SELECT * FROM users WHERE username = ? AND password = ?";

        try (Connection connection = getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, username);
            preparedStatement.setString(2, password);
            return preparedStatement.executeQuery().next();
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }
}
