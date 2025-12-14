def count_words(book_text: str)->int:
    total_words:int = len(book_text.split())
    return total_words

def count_chars(book_text: str) -> dict[str, int]:
    lower_contents = book_text.lower()
    results: dict[str,int] = {}
    for char in lower_contents:
        results[char] = results.get(char,0) + 1
    return results

def sort_on(items: dict)->int:
    return items["num"]

def sort_chars(char_counts: dict[str,int])->list[dict[str,str|int]]:
    char_list: list[dict[str,str|int]] = []
    for char,num in char_counts.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)
    return char_list