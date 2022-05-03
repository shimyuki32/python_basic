#previous method
tweet_limit = 200
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))
    
#new method using walrus operator
tweet_limit = 200
tweet_string = "Blah" * 50
if (diff := tweet_limit - len(tweet_string)):
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))