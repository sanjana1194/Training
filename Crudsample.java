import java.sql.*;

public class Crudsample {
	String url;
	String user;
	String pass;

	Crudsample() {
		url = "jdbc:mysql://138.68.140.83:3306/db_supermarket";
		user = "Sanjana";
		pass = "Sanjana@123";
	}

	void createRecord(String cashierID, String cashierName) {
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection conn = DriverManager.getConnection(url, user, pass);

			String query = "INSERT INTO Cashier (CashierID, CashierName) VALUES (?, ?)";
			PreparedStatement ps = conn.prepareStatement(query);
			ps.setString(1, cashierID);
			ps.setString(2, cashierName);

			int rows = ps.executeUpdate();
			if (rows > 0)
				System.out.println("Cashier added successfully!");
			else
				System.out.println("Insertion failed!");

			ps.close();
			conn.close();
		} 
		catch (Exception e) {
			e.printStackTrace();
		}
	}

	void readRecords() {
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection conn = DriverManager.getConnection(url, user, pass);

			String query = "SELECT * FROM Cashier";
			Statement stmt = conn.createStatement();
			ResultSet rs = stmt.executeQuery(query);

			while (rs.next()) {
				String id = rs.getString("CashierID");
				String name = rs.getString("CashierName");
				System.out.println(id + " | " + name);
			}

			rs.close();
			stmt.close();
			conn.close();
		} 
		catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		Crudsample cs = new Crudsample();

		cs.createRecord("C013", "Sai");
		cs.createRecord("C014", "Reena");

		cs.readRecords();
	}
}
