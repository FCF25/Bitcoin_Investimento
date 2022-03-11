import contas
import input_moeda
from login_senha import senha_gmail, email_gmail
import smtplib
import email.message
import time



# Vai enviar o e-mail com todas as informações que coloquei , porém poderá ser alteradas abaixo
def enviar_email(self):
    vinvestimento = contas.inv((input_moeda.lista[self]))
    vlucro = float(contas.valor_ganho(input_moeda.lista[self]))
    vatual = float(vinvestimento + vlucro)
    nmoeda = contas.nameinv(input_moeda.lista[self])
    corpo_email = (f'''  <h1>Você ja pode retirar o dinheiro !!!</h1                                     
                                                                                                        
                        <p>A nossa criptomoeda ultrapassou o nosso valor estipulado de lucro de R$ {vlucro:,.2f} que foi programado.</p>    
                                                                                                                            
                        <table  border=1 cellpadding=5>                                                                   
                        <tr>                                                                                              
                        <th align="center"> {nmoeda}</th>                                                      
                        <th align="center">Valores</th>                                                                   
                        </tr>                                                                                             
                                                                                                                            
                        <tr>                                                                                              
                        <td> Valores Investido</td>                                                                       
                        <td> R$ {vinvestimento:,.2f}</td>                                                                     
                        </tr>                                                                                             
                                                                                                                            
                        <tr>                                                                                              
                        <td> Valor atual</td>                                                                             
                        <td> R$ {vatual:,.2f}</td>                                                          
                        </tr>                                                                                             
                                                                                                                            
                        <td> Lucro  </td>                                                                                 
                        <td> R$ {vlucro:.2f}</td>                                                                       
                        </tr>                                                                                             
                        </table>                                                                                          
                                                                                                                            
                        <p> <font size=+2><b><font color="#000099">Vai logo!!!!</font></b></p>                            
                            ''')

    msg = email.message.Message()
    msg['Subject'] = f'Assunto - Sua cripto {"bitcoin"} já deu lucro!!'
    msg['From'] = email_gmail() 
    msg['To'] = 'e-mail@gmail.com' # Você deverá colocar o e-mail que você quer receber o valor
    password = senha_gmail()
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
    

# Vai verificar se o total de nosso investimento for maior ou igual nosso valor que colocamos em sacar.
# Nesse caso abaixo ele vai pegar a ultima linha de nossa lista que é o total de nossa carteira e verificar se sim envia, se não não envia. 
def ganhando_envia_email(self):
    # c = contas.lucro_unitario()
    envia = contas.valor_ganho(self)
    if envia >= self.sacar:
        time.sleep(60)
        return enviar_email(-1)
