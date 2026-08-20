function criarFormularioVendooMEI() {
  var form = FormApp.create('Vendoo | Pesquisa de Mercado com MEIs');
  form.setDescription('Olá, empreendedor(a)! Esta pesquisa entende as dores e rotinas do MEI para criarmos o Vendoo, uma solução sob medida para o seu negócio.');

  form.addTextItem().setTitle('1. Nome ou Nome da Marca (Opcional)').setRequired(false);
  form.addTextItem().setTitle('2. Em qual segmento seu MEI atua?').setHelpText('Ex: Serviços, Beleza, Tecnologia, Alimentação...').setRequired(true);

  var q3 = form.addMultipleChoiceItem();
  q3.setTitle('3. Há quanto tempo você atua como MEI?')
    .setChoices([
      q3.createChoice('Menos de 6 meses'),
      q3.createChoice('De 6 meses a 1 ano'),
      q3.createChoice('De 1 a 3 anos'),
      q3.createChoice('Mais de 3 anos'),
      q3.createChoice('Ainda estou em processo de formalização')
    ]).setRequired(true);

  var q4 = form.addCheckboxItem();
  q4.setTitle('4. Quais são as suas maiores dificuldades no dia a dia do MEI?')
    .setChoices([
      q4.createChoice('Separar finanças pessoais das da empresa (PF x PJ)'),
      q4.createChoice('Emitir notas fiscais e controlar obrigações (DAS)'),
      q4.createChoice('Controlar fluxo de caixa e pagamentos'),
      q4.createChoice('Atrair novos clientes e divulgar serviços'),
      q4.createChoice('Cobrar clientes e evitar inadimplência')
    ]).setRequired(true);

  var q5 = form.addMultipleChoiceItem();
  q5.setTitle('5. Como você faz a gestão financeira e de vendas hoje?')
    .setChoices([
      q5.createChoice('Caderno / Papel'),
      q5.createChoice('Planilhas (Excel / Google Sheets)'),
      q5.createChoice('Bloco de notas / WhatsApp'),
      q5.createChoice('Sistema/Software pago'),
      q5.createChoice('Não faço controle estruturado')
    ]).setRequired(true);

  var q6 = form.addScaleItem();
  q6.setTitle('6. O quanto uma plataforma unificada (Vitrine + Gestão + Pagamentos) facilitaria seu dia a day?')
    .setBounds(1, 5)
    .setLabels('Pouco útil', 'Indispensável')
    .setRequired(true);

  var q7 = form.addCheckboxItem();
  q7.setTitle('7. Qais recursos do Vendoo seriam mais valiosos para você?')
    .setChoices([
      q7.createChoice('Vitrine/Catálogo digital com link para WhatsApp'),
      q7.createChoice('Checkout de pagamento integrado (PIX e Cartão)'),
      q7.createChoice('Separação automática de caixa PF e PJ'),
      q7.createChoice('Lembretes e alertas de obrigações do MEI (DAS)'),
      q7.createChoice('Cobranças e lembretes automáticos para clientes')
    ]).setRequired(true);

  var q8 = form.addMultipleChoiceItem();
  q8.setTitle('8. Quanto aceitaria investir por mês no Vendoo?')
    .setChoices([
      q8.createChoice('Apenas versão 100% gratuita'),
      q8.createChoice('Até R$ 29,90 / mês'),
      q8.createChoice('De R$ 30,00 a R$ 59,90 / mês'),
      q8.createChoice('Porcentagem por venda realizada')
    ]).setRequired(true);

  var q9 = form.addMultipleChoiceItem();
  q9.setTitle('9. Quer testar a versão Beta do Vendoo em primeira mão?')
    .setChoices([
      q9.createChoice('Sim! Quero ser um dos primeiros.'),
      q9.createChoice('Talvez mais para frente.'),
      q9.createChoice('Não no momento.')
    ]).setRequired(true);

  form.addTextItem().setTitle('10. WhatsApp ou E-mail para contato:').setRequired(false);
}