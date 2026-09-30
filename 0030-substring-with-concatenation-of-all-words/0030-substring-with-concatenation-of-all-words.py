class Solution(object):
    def findSubstring(self, s, words):
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        result = []

        for i in range(word_len):
            left = i
            count = 0
            current = {}

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_freq:
                    current[word] = current.get(word, 0) + 1
                    count += 1

                    while current[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    current = {}
                    count = 0
                    left = right + word_len

        return result