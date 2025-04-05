<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Final Exam - Wataru Okada</title>
</head>

<body>
    <h1>Final Exam - Wataru Okada</h1>
    <h2>Choose Party Items</h2>
    <div>
        <h3>Party Items List</h3>
        <ul style="list-style-type: none;">
            <li value="0" name="cake" id="cake">0: Cake</li>
            <li value="1" name="balloons" id="balloons">1: Balloons</li>
            <li value="2" name="musicSystem" id="musicSystem">2: Music System</li>
            <li value="3" name="lights" id="lights">3: Lights</li>
            <li value="4" name="cateringService" id="cateringService">4: Catering Service</li>
            <li value="5" name="dj" id="dj">5: DJ</li>
            <li value="6" name="photoBooth" id="photoBooth">6: Photo Booth</li>
            <li value="7" name="tables" id="tables">7: Tables</li>
            <li value="8" name="chairs" id="chairs">8: Chairs</li>
            <li value="9" name="drinks" id="drinks">9: Drinks</li>
            <li value="10" name="partyHats" id="partyHats">10: Party Hats</li>
            <li value="11" name="streamers" id="streamers">11: Streamers</li>
            <li value="12" name="invitationCards" id="invitationCards">12: Invitation Cards</li>
            <li value="13" name="partyGames" id="partyGames">13: Party Games</li>
            <li value="14" name="cleaningService" id="cleaningService">14: Cleaning Service</li>
        </ul>
    </div>
    <form action="" method="get">
        <label for="items">Enter item indices separated by commas (e.g. 0,2):</label><br>
        <input type="text" name="items" id="items" size="30" required><br><br>
        <input type="submit" value="Order the Items">
    </form>

    <?php
    if (isset($_GET['items']) && !empty($_GET['items'])) {
        $items = escapeshellarg($_GET['items']);
        $output = shell_exec("python3 party_planner.py items=$items");
        echo "<hr><h2>Order Summary</h2>";
        echo $output;
    }
    ?>
</body>

</html>
