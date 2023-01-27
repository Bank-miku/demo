<?php
    if ($_POST['sub']) {
        echo $_POST['name'].'<br>';
        echo '<a href="./formCheck.html">go back to page.html</a>';
    }else{
        echo 'please input your name'.'<br>';
        echo '<a href="./page.html">go back to page.html</a>';
    }
?>