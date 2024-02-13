<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP NOTES</title>
</head>

<body>
    <?php
    // How to write a function
    function stampaLinguaggio($language){
        echo "Pagina scritta in <strong>$language</strong>.<br>";
    }

    // Function call
    stampaLinguaggio("PHP");
    ?>

    <?php
    //Boolean var
    $vero = true;
    $falso = false;
    $and = 1 && 1;
    $or = 1 || 0;
    $not = !true;
    ?>

    <?php
    // How to define a const
    define("COSTANTE",123);
    echo COSTANTE . "<br>";
    ?>

    <?php
    //If-else
    $a = 5;
    if ($a % 2)
        echo "$a è dispari.";
    else
        echo "$a è pari.";
    echo "<br>";

    //Switch
    $colore = "rosso";

    switch($colore){
        case 'blu':
            echo "Il colore è blu";
            break;
        case 'giallo':
            echo 'Il colore è giallo';
            break;
        default:
            echo "Il colore è $colore";
            break;
    }
    echo "<br>";

    //Another type of if-else
    echo ($colore == "rosso") ? "colore giusto" : "colore sbagliato";
    echo "<br><br><br>";
    ?>

    <?php
    //For cycle
    for ($i = 1; $i <= 10; $i++)
        echo "$i<br>";

    //While cycle
    $i = 0;
    while ($i < 10)
        echo $i++;
    echo "<br>";

    //DoWhile cycle
    do{
        echo --$i;
    } while ($i > 0);
    echo "<br><br><br>";
    ?>

    <?php
    //Array
    $arr = [1, 2, 3, 4];

    foreach ($arr as $valore)
        echo "$valore<br>";
        echo "<br><br>";
    ?>

    <form action="php_notes.php" method="post">
        <input type="text" name="stringa" placeholder="Inserisci stringa" />
        <input type="submit" value="Carica" />
    </form>
    <?php
    error_reporting(E_ERROR | E_PARSE);

    if ($_POST["stringa"])
        echo "Stringa precedentemente caricata -> " . $_POST["stringa"];
    ?>
</body>
</html>