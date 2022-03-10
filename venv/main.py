from textblob import TextBlob

def get_polarity(text):
  sentiment = TextBlob(text)
  return sentiment.sentiment.polarity

entry = input("What's going on today? ")
polarity = get_polarity(entry)

if polarity < -0.2:
  print("Maybe it's the weather?")
elif polarity < 0.5:
  print("Hey, sounds like you're getting through it alright!")
else:
  print("Nice! Bring the sunshine!")
quit()
