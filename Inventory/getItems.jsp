<%@ page import="java.sql.*, org.json.*, java.util.*" %>
<%
	response.setContentType("application/json");
	response.setCharacterEncoding("UTF-8");

	String url = "jdbc:mysql://138.68.140.83:3306/db_supermarket";
	String user = "Sanjana";
	String pass = "Sanjana@123";

	Connection con = null;
	PreparedStatement pst = null;
	ResultSet rs = null;

	try {
		Class.forName("com.mysql.cj.jdbc.Driver");
		con = DriverManager.getConnection(url, user, pass);

		String sql = "SELECT ItemID, Description, UnitPrice, StockQty FROM Item";
		pst = con.prepareStatement(sql);
		rs = pst.executeQuery();

		JSONArray arr = new JSONArray();

		while (rs.next()) {
			JSONObject obj = new JSONObject();
			obj.put("ItemID", rs.getString("ItemID"));
			obj.put("Description", rs.getString("Description"));
			obj.put("UnitPrice", rs.getDouble("UnitPrice"));
			obj.put("StockQty", rs.getInt("StockQty"));
			arr.put(obj);
		}

		out.print(arr.toString());

	} catch (Exception e) {
		out.print("{\"error\":\"" + e.toString() + "\"}");
	}
%>
