<html>
<head>
    <title>Indian Cricket Players</title>
</head>
<body>
    <h2>List of Indian Cricket Players</h2>

    <?php
    $players = [
        "RISHAL",
        "RAHIBA",
        "NIVED RAAJ",
        "ASWIN A.C",
        "ANAS SHAWARMA",
        "ZALZU",
        "SHANID",
        "SHEIKH",
        "Rishabh Pant",
        "Mohammad Shami"
    ];

    echo "<table border='1'>
            <tr>
                <th>Sr. No.</th>
                <th>Player Name</th>
            </tr>";

    $srNo = 1;
    foreach ($players as $player) {
        echo "<tr>
                <td>$srNo</td>
                <td>$player</td>
              </tr>";
        $srNo++;
    }

    echo "</table>";
    ?>

</body>
</html>
