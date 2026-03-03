from js import document
import random

word_list = ["python", "hangman", "music", "soccer", "purple", "stitch", "money"]
stages = [
    "",
    "________        ",
    "|               ",
    "|        |      ",
    "|        0      ",
    "|       /|\     ",
    "|       / \     ",
    "|               "
]

word = ""
rletters = []
board = []
wrong = 0

def start_game(event):
    global word, rletters, board, wrong
    word = random.choice(word_list)
    rletters = list(word)
    board = ["_"] * len(word)
    wrong = 0
    document.getElementById("word-display").innerText = "単語: " + " ".join(board)
    document.getElementById("message").innerText = "1文字ずつ当ててみてね！"
    document.getElementById("hangman-stage").innerText = ""

def guess_letter(event):
    global rletters, board, wrong
    char = document.getElementById("guess-input").value.lower()
    document.getElementById("guess-input").value = ""

    if not char or len(char) != 1:
        document.getElementById("message").innerText = "1文字だけ入力してね！"
        return

    if char in rletters:
        indices = [i for i, c in enumerate(rletters) if c == char]
        for i in indices:
            board[i] = char
            rletters[i] = "$"
        document.getElementById("message").innerText = f"{char} は正解！"
    else:
        wrong += 1
        document.getElementById("message").innerText = f"{char} は不正解！"

    document.getElementById("word-display").innerText = "単語: " + " ".join(board)
    document.getElementById("hangman-stage").innerText = "\n".join(stages[:wrong + 1])

    if "_" not in board:
        document.getElementById("message").innerText = "🎉 勝ったよ！おめでとう！"
    elif wrong == len(stages) - 1:
        document.getElementById("message").innerText = f"💀 ゲームオーバー！正解は「{word}」だったよ。"

document.getElementById("start-btn").addEventListener("click", start_game)
document.getElementById("guess-btn").addEventListener("click", guess_letter)
