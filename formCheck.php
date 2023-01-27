<?php
  
  echo "<pre>";
  print_r($_GET); //サーバで$_GET['キー']があるかないかを表示
  echo "</pre>";
  

  //投稿日のチェック
  if($_GET['dateSelect'] != ""){
    echo "投稿日：{$_GET['dateSelect']}<br>\n";
  }
  else{
    echo "投稿日を入力してください。<br>\n";
  }

  //登校時間のチェック
  if($_GET['timeSelect'] != ""){
    echo "投稿時間：{$_GET['timeSelect']}<br>\n";
  }
  else{
    echo "投稿時間を入力してください。<br>\n";
  }

  //氏名のチェック
  if($_GET['namae'] != ""){
    echo "氏名：{$_GET['namae']}<br>\n";
  }
  else{
    echo "氏名を入力してください。<br>\n";
  }

  //メールのチェック
  if($_GET['eMail'] != ""){
    echo "メールアドレス：{$_GET['eMail']}<br>\n";
  }
  else{
    echo "メールアドレスを入力してください。<br>\n";
  }
  
  //性別のチェック
  if(isset($_GET['gender'])){
    echo "性別：{$_GET['gender']}<br>\n";
  }
  else{
    echo "性別を選択してください。<br>\n";
  }

  //趣味のチェック
  if(isset($_GET['hobby'])){
    $hobby = "";
    for($i = 0 ; $i < count($_GET['hobby']) ; $i++){
        $hobby .= $_GET['hobby'][$i]."、";
    }
    $hobby = mb_substr($hobby,0,-1);
    //$hobby = mb_substr($hobby,0,mb_strlen($hobby)-1);
    echo "趣味:{$hobby}<br>\n";
  }
  else{
    echo "趣味がチェックされていません。<br>\n";
  }

  //出身地のチェック
  if($_GET['birthplace'] != ""){
    echo "出身地：{$_GET['birthplace']}<br>\n";
  }
  else{
    echo "出身地を選択したください。<br>\n";
  }

  //好きな地域のチェック
  if(isset($_GET['favoriteArea'])){
    $favoriteArea = "";
    for($i = 0 ; $i < count($_GET['favoriteArea']) ; $i++){
      $favoriteArea .= $_GET['favoriteArea'][$i]."、";
    }
    $favoriteArea = mb_substr($favoriteArea,0,-1);
    echo "好きな地域：{$favoriteArea}<br>\n";
  }
  else{
    echo "好きな地域を選択してください。<br>\n";
  }

  //問い合わせのチェック
  if($_GET['inquiry'] != ""){
    echo "問合せ内容：{$_GET['inquiry']}<br>\n";
  }
  else{
    echo "問合せ内容は、必須ではありません。<br>\n";
  }

  //好きな場所のチェック
  if(isset($_GET['like'])){
    echo "どこが好きですか？：{$_GET['like']}<br>\n";
  }
  else{
    echo "どこが好きですか？をチェックしてください。<br>\n";
  }

  //ペットのチェック飼って
  if(isset($_GET['pet'])){
    echo "ペットは飼っていますか：{$_GET['pet']}<br>\n";
  }
  else{
    echo "ペットは飼っていますか？をチェックしてください。<br>\n";
  }
?>