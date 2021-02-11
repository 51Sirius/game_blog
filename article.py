articles = [
    {'title': 'Lost ark',
     'text': 'Благодарим вас за интерес и вопросы, которые вы оставляли к публикациям с анонсом плана обновлений и презентации LOA ON. Команда локализации передала разработчикам комментарии русскоязычного сообщества, и мы вместе продолжим радовать вас подробной информацией об игре и ее перспективах. Если вы хотите узнать больше о будущем LOST ARK, оставляйте свои вопросы в специальной форме. Мы выберем самые интересные и часто встречающиеся, а ответит на них в видеоформате директор разработки Smilegate RPG — Geum Kang-seon.',
     'date': '08.02.2021',
     'big': True,
     'id': 1,
     'img': True,
     'img_id': 'https://im0-tub-ru.yandex.net/i?id=83291a42738314f71c7455101901b2ac&n=13',
     'categories': [1]
     },
    {'title': 'Gaming IT',
     'text': 'В следующем месяце Disco Elysium дебютирует на консолях и получит расширенную версию — The Final Cut. Среди нововведений — политические квесты, о которых во время анонса нового издания разработчики почти ничего не говорили. Зато поговорили в интервью Push Square.',
     'date': '09.02.2021',
     'big': False,
     'id': 2,
     'img': False,
     'img_id': '',
     'categories': [5]
     },
]


def find_by_text(text: str):
    result = []
    text = text.lower()
    for article in articles:
        if text in article['text'] or text in article['title']:
            result.append(article)
    return result
