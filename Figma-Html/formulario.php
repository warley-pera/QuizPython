<?php

if(isset($_POST['submit']))
{
    print_r($_POST['nome']);
    print_r($_POST['email']);
    print_r($_POST['telefone']);
    print_r($_POST['senha']);


include_once('config.php');

$nome = $_POST['nome'];
$email = $_POST['email'];
$telefone = $_POST['telefone'];
$senha = $_POST['senha'];

$result = mysqli_query($conexao, "INSERT INTO usuarios(nome, email, telefone, senha) VALUES ($nome, $email, $telefone, $senha");

}


?>