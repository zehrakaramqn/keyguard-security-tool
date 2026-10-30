import re

def analyze_password(password):
    score = 0
    feedback = []

    if not password:
        return 0, ["Lütfen bir parola girin."]

    length = len(password)
    if length >= 12:
        score += 40
    elif length >= 8:
        score += 20
        feedback.append("Parolayı en az 12 karakter yapmak güvenliği artırır.")
    else:
        feedback.append("Parola çok kısa! En az 8 karakter olmalı.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 20
    else:
        feedback.append("Hem büyük hem küçük harf kullanın.")

    if re.search(r"\d", password):
        score += 20
    else:
        feedback.append("En az bir rakam ekleyin.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        feedback.append("En az bir özel karakter (!@#$%^&*) ekleyin.")

    return score, feedback