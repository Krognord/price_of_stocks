import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Ваш ключ API
API_KEY = 'cm2rlo1r01qoj4je82egcm2rlo1r01qoj4je82f0'

def get_last_price(symbol):
    """ Получение последней цены акции. """
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data['c']  # c - текущая цена

def animate(i):
    """ Функция для обновления графика. """
    price = get_last_price('TSLA')  # Используем символ тикера Tesla
    prices.append(price)
    times.append(i)

    plt.cla()
    plt.plot(times, prices)
    plt.xlabel('Время (обновления)')
    plt.ylabel('Цена в долларах')
    plt.title('Цена акций Tesla в реальном времени')

prices = []
times = []

# Создание анимации с отключенным кэшированием данных кадров
ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show()