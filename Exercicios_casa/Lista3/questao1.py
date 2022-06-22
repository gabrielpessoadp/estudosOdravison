import requests
# link do open_weather: https://openweathermap.org/
i = 0
while i != 1:
    API_KEY = "1de3390a307a4154696455764302fa3b"
    cidade = input("Digite o nome da cidade que você deseja saber a temperatura:\n")
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
    if cidade == 'exit':
        print('Programa encerrado.')
        break
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    print(f'\nDescrição do tempo: {descricao} e está fazendo {temperatura} ºC')
    print('-----'*10, "\nSe deseja encerrar o programa, digite exit\n", '-----'*10)
        