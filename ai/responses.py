import random

START_RESPONSES = [
    "Halo Ryan 😎 Mau dibukain apa?",
    "Siap bos. Mau ngoding, data science, atau main game?",
    "Desktop Assistant online 🫡",
    "Lagi siap jaga laptop. Ada yang mau dibuka?"
]

UNKNOWN_RESPONSES = [
    "Gua belum ngerti maksudnya 😭",
    "Coba ngomong yang lebih jelas dikit 🗿",
    "Perintah itu belum masuk kamus gua.",
    "Hmm... gua bingung harus buka apa."
]

ACCESS_DENIED_RESPONSES = [
    "Siapa lu 🗿",
    "Akses ditolak.",
    "Laptop ini bukan punya lu 😭",
]

PLANNING_RESPONSES = [
    "Oke bentar gua pikir dulu...",
    "Nyusun workspace dulu 🧠",
    "Liat dulu yang harus dibuka...",
    "Siap, lagi direncanain."
]

SUCCESS_RESPONSES = [
    "Siap 🫡",
    "Beres 😎",
    "Sudah gua kerjain.",
    "Sip, jalan.",
    "Oke, lagi dibukain.",
    "Beres boss 😎",
    "Workspace siap 🔥",
    "Semua udah kebuka 🫡",
    "Siap digunakan.",
]

def pick(pool):
    return random.choice(pool)