<html>
<head>
    <title>Electricity Bill</title>
</head>
<body>
    <h2>Electricity Bill Calculation</h2>
    
    <form action="" method="POST">
        <input type="text" name="customerName" placeholder="Customer Name" required><br><br>
        <input type="number" name="units" placeholder="Units Consumed (kWh)" min="0" required><br><br>
        <input type="number" name="rate" placeholder="Rate per Unit (₹)" min="1" step="any" required><br><br>
        <input type="number" name="additionalCharges" placeholder="Additional Charges (₹)" step="any"><br><br>
        <input type="number" name="discount" placeholder="Discount (%)" min="0" max="100" step="any"><br><br>
        <button type="submit">Generate Bill</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $customerName = htmlspecialchars($_POST['customerName']);
        $unitsConsumed = $_POST['units'];
        $ratePerUnit = $_POST['rate'];
        $additionalCharges = isset($_POST['additionalCharges']) ? $_POST['additionalCharges'] : 0;
        $discount = isset($_POST['discount']) ? $_POST['discount'] : 0;

        $baseAmount = $unitsConsumed * $ratePerUnit;
        $discountAmount = ($baseAmount + $additionalCharges) * ($discount / 100);
        $totalBill = $baseAmount + $additionalCharges - $discountAmount;

        echo "<h3>Bill Details</h3>";
        echo "<table border='1'>
                <tr><th>Customer Name</th><td>$customerName</td></tr>
                <tr><th>Units Consumed</th><td>$unitsConsumed kWh</td></tr>
                <tr><th>Rate per Unit</th><td>₹$ratePerUnit</td></tr>
                <tr><th>Base Amount</th><td>₹" . number_format($baseAmount, 2) . "</td></tr>
                <tr><th>Additional Charges</th><td>₹" . number_format($additionalCharges, 2) . "</td></tr>
                <tr><th>Discount</th><td>" . number_format($discount, 2) . "%</td></tr>
                <tr><th>Total Bill</th><td>₹" . number_format($totalBill, 2) . "</td></tr>
              </table>";
    }
    ?>
</body>
</html>
