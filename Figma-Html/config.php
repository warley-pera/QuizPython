<?php

$dbHost = 'localhost'
$dbUsername = 'root'
$dbPassword = ''
$dbName = 'formulario-figma'

$conexao = new mysqli($dbHost,$dbUsername, $dbPassword, $dbName)


if($conexao->connect_erro)
{
    echo "Erro"
}
else
{
    echo "Conexão efetuada com sucesso"
}
?>