package signupapp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {
    private static final String DEFAULT_URL = "jdbc:mysql://localhost:3306/myapp";
    private static final String DEFAULT_USERNAME = "jigyasa";
    private static final String DEFAULT_PASSWORD = "jigyasa";

    private final String url;
    private final String username;
    private final String password;

    public DatabaseConnection() {
        this(DEFAULT_URL, DEFAULT_USERNAME, DEFAULT_PASSWORD);
    }

    public DatabaseConnection(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    public Connection getConnection() throws SQLException {
        return DriverManager.getConnection(url, username, password);
    }
}
