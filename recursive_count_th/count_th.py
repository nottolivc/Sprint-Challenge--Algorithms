'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
  def occur(word, start):
    count = 0
    if start >= len(word) - 1:
      return 0
    if word[start] + word[start + 1] == 'th':
      count += 1
    return occur(word, start + 1) + count
  return occur(word, 0)
