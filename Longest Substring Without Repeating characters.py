def longest(s):
  longest=0
  current=""
  for ch in s:
    if ch in current:
      index=current.index(ch)
      current=current[index+1:]
    current+=ch
    longest=max(longest,len(current))
  print("Longest Substring : ",longest)
longest("pwwkew")

