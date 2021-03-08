def find_by_text(text: str, articles):
    result = []
    text = text.lower()
    for article in articles:
        if text in article['text'].lower() or text in article['title'].lower():
            result.append(article)
    return result
