def order(sentence):
  # code here
  result = []
  if sentence:
      words = sentence.split()
      for i in range(1, 10):
          for w in words:
              if (str(i) in w):
                  result.append(w)
      sentence = " ".join(result)
      return sentence
  return sentence
