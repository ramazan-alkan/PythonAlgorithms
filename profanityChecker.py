# Profanity checker

def profanityChecker(text):
    # Profanity list
    profanities = ["Hello", "hello", "Bad", "bad"]

    # Check profanity
    if any(a in text for a in profanities):
        # return if there is profanity
        return "I found a bad word in profanities array."
    # return if there is not any profanity
    return "It's perfect. I can't found any bad word."

text = profanityChecker("Hello is really a bad word") # Send a string

print(text) # Print result