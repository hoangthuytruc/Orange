vowels = "AEOYIU"
directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
start = True


def count_vowels(word):
    res = 0
    for w in word:
        if w in vowels:
            res += 1
    return res


def find_words(board, x, y, cur_word, visited, found_words):
    if len(cur_word) == 4:
        if count_vowels(cur_word) == 2:
            found_words.add(cur_word)
        return

    visited[x][y] = True
    for d in directions:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
            new_word = cur_word + board[nx][ny]
            find_words(board, nx, ny, new_word, visited, found_words)
    visited[x][y] = False

def solve():
    global start

    board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(2)]
    if not start:
        input()
    for i in range(4):
        line = list(input().split())
        if line[0] == '#':
            exit()
        for j in range(8):
            board[j >> 2][i][j & 3] = line[j]

    if not start:
        print()
    start = False
    visited = [[False for _ in range(4)] for _ in range(4)]
    words = [set() for _ in range(2)]
    for board_id in range(2):
        for i in range(4):
            for j in range(4):
                cur_word = ""
                cur_word += board[board_id][i][j]
                find_words(board[board_id], i, j, cur_word, visited, words[board_id])

    common_words = list()
    for word in words[0]:
        if word in words[1]:
            common_words.append(word)
    common_words.sort()
    if len(common_words) == 0:
        print("There are no common words for this pair of boggle boards.")
    else:
        for w in common_words:
            print(w)


if __name__ == '__main__':
    while True:
        solve()