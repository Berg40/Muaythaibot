import requests
import json
import os


class TelegramBot:

  def __init__(self):
    token = '7189515285:AAFEH_HZAkulMplyIZsX7ee19C4cxBnMktQ'
    self.url_base = f'https://api.telegram.org/bot{token}/'

  # Iniciar o bot
  def Iniciar(self):
    update_id = None
    while True:
      atualizacao = self.obter_mensagens(update_id)
      mensagens = atualizacao['result']
      if mensagens:
        for mensagem in mensagens:
          update_id = mensagem['update_id']
          chat_id = mensagem['message']['chat']['id']
          eh_primeira_mensagem = mensagem['message']['message_id'] == 1
          resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
          self.responder(resposta, chat_id)

  # Obter mensagens
  def obter_mensagens(self, update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout=100'
    if update_id:
      link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)

  # Criar uma resposta

  def criar_resposta(self, mensagem, eh_primeira_mensagem):
    mensagem_texto = mensagem['message']['text']
    if eh_primeira_mensagem or mensagem_texto.lower() == 'sim':
      return f'''Ola tudo bem digite a opção desejada{os.linesep}1 - Saber sobre o Muay Thai {os.linesep}2 - Valor das Aulas {os.linesep}3 - Saber sobre o Professor {os.linesep}4 - Agendar aula '''
    if mensagem_texto == '1':
      return f'''O Muay Thai, conhecido como a "Arte das Oito Armas", é uma arte marcial tailandesa que engloba golpes de punho, cotovelo, joelho, perna e técnicas de clinch. Além de ser uma forma eficaz de autodefesa, o Muay Thai oferece uma série de benefícios para a saúde física e mental. Fisicamente, melhora a aptidão cardiovascular, promove o fortalecimento muscular, aumenta a flexibilidade e a coordenação. Mentalmente, desenvolve disciplina, concentração, autoconfiança e reduz o estresse. A prática regular do Muay Thai não só aprimora o corpo, mas também fortalece a mente, proporcionando um equilíbrio físico e mental completo.Durante uma aula de Muay Thai intensa, é possível queimar aproximadamente de 600 a 800 calorias, dependendo da duração da aula, da intensidade do treinamento e do peso corporal do praticante. Esta estimativa pode variar de acordo com diversos fatores individuais, mas geralmente o Muay Thai é uma atividade física altamente eficaz para queimar calorias e melhorar a aptidão cardiovascular.'''

    if mensagem_texto == '2':
      variavel1 = 'Valor R$240,00 por mês (com 1 aula por semana)'
      variavel2 = 'Valor R$450,00 por mês (Com 2 aulas por semana)'
      variavel3 = 'Valor R$680,00 por mês (Com 3 aulas por semana)'

      return f'''Os valores das aulas são:{os.linesep} {variavel1}{os.linesep}{variavel2}{os.linesep}{variavel3}'''

    if mensagem_texto == '3':
      return f''' Se deseja conhecer mais sobre mim, permita-me apresentar-me. Sou Berg Andrade, praticante dedicado de Muay Thai há mais de 12 anos. Com 41 anos de idade, esta arte marcial se tornou uma parte fundamental da minha vida.
Desde os primeiros passos na academia, o Muay Thai tem sido mais do que apenas uma prática física; tornou-se um estilo de vida para mim. O tatame se transformou em um espaço onde posso me desafiar e crescer constantemente.
Como professor, tenho a honra de compartilhar minha experiência e conhecimento desde 2020. Observar o progresso dos meus alunos é uma fonte de grande satisfação para mim.
 '''
      # {os.linesep}Confirmar pedido?(s/n)''' se quiser usar esse comando
    if mensagem_texto == '4':
      return f'''"Clique no link do WhatsApp e informe o pacote escolhido, nome e disponibilidade de horário e dias para o treino: [aqui](https://api.whatsapp.com/send?phone=5512997071992&text=Agendamentos%20de%20aulas%20de%20Muay%20Thai)")
 '''

    if mensagem_texto.lower() in ('s', 'sim'):
      return ''' Pedido Confirmado! '''
    else:
      return "Gostaria de saber mais sobre Muay Thai e as aulas? Digite 'sim'"

  # Responder
  def responder(self, resposta, chat_id):
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)


bot = TelegramBot()
bot.Iniciar()



