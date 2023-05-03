import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

# inicialização dos módulos
audio = sr.Recognizer() # módulo para reconhecimento de voz
maquina = pyttsx3.init() # módulo para sintetização de voz

# função para execução de comando de voz
def executa_comando():
    try:
        with sr.Microphone() as source: # utiliza o microfone como entrada
            print('Ouvindo..') # imprime mensagem no console
            voz = audio.listen(source) # aguarda o comando de voz
            comando = audio.recognize_google(voz, language='pt-BR') # reconhece o comando de voz e define a linguagem
            comando = comando.lower() # converte o comando para minúsculo
            if 'Sintia' in comando: # se a palavra "Sintia" for detectada no comando
                comando = comando.replace('Sintia', '') # remove a palavra "Sintia" do comando
                maquina.say(comando) # sintetiza o comando de voz em voz alta
                maquina.runAndWait() # espera a finalização da execução da fala

    except:
        print('Microfone não está ok') # se houver algum erro, imprime mensagem no console

    return comando # retorna o comando de voz

# função para execução de ações baseadas no comando de voz
def comando_voz_usuario():
    comando = executa_comando() # recebe o comando de voz a partir da função "executa_comando"
    if 'horas' in comando: # se o comando de voz contém a palavra "horas"
        hora = datetime.datetime.now().strftime('%H:%M') # obtém a hora atual
        maquina.say('Agora são' + hora) # sintetiza a hora atual em voz alta
        maquina.runAndWait() # espera a finalização da execução da fala
    elif 'procure por' in comando: # se o comando de voz contém a expressão "procure por"
        procurar = comando.replace('procure por', '') # remove a expressão "procure por" do comando
        wikipedia.set_lang('pt') # define a linguagem da pesquisa no wikipedia como português
        resultado = wikipedia.summary(procurar,2) # pesquisa no wikipedia o que foi solicitado e define o número de frases a serem retornadas
        print(resultado) # imprime o resultado no console
        maquina.say(resultado) # sintetiza o resultado em voz alta
        maquina.runAndWait() # espera a finalização da execução da fala
    elif 'toque' in comando: # se o comando de voz contém a palavra "toque"
        musica = comando.replace('toque','') # remove a palavra "toque" do comando
        resultado = pywhatkit.playonyt(musica) # pesquisa a música no YouTube e a reproduz
        maquina.say('Tocando música') # sintetiza mensagem informando que a música está sendo tocada
        maquina.runAndWait() # espera a finalização da execução da fala

comando_voz_usuario() # chama a função "comando_voz_usuario" para execução do código.
