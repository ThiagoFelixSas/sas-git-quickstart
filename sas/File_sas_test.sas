/* Teste de conectividade e validação de ambiente */
data work.teste_git;
    attrib ds_mensagem length=$50;
    ds_mensagem = "Integracao SAS Studio e Git com sucesso!";
    dt_processamento = datetime();
    format dt_processamento datetime20.;
run;

title "Validacao de Ambiente - Time CA";
proc print data=work.teste_git;
run;