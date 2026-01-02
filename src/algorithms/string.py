from __future__ import annotations

import re


def string_concat(n):
    s = ""
    for i in range(n):
        s += str(i)
    return s


def regex_match(strings: list[str], pattern: str) -> list[str]:
    matched = []
    for s in strings:
        if re.match(pattern, s):
            matched.append(s)
    return matched


def is_palindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1
    while left < right:
        c_left = text[left]
        if not c_left.isalnum():
            left += 1
            continue
        c_right = text[right]
        if not c_right.isalnum():
            right -= 1
            continue
        if c_left.lower() != c_right.lower():
            return False
        left += 1
        right -= 1
    return True


def word_frequency(text: str) -> dict[str, int]:
    words = text.lower().split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def find_common_tags(articles: list[dict[str, list[str]]]) -> set[str]:
    if not articles:
        return set()

    common_tags = set(articles[0].get("tags", []))
    for article in articles[1:]:
        common_tags.intersection_update(article.get("tags", []))
        if not common_tags:
            break
    return common_tags
