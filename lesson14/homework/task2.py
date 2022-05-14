# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

# use replace

def stop_words(words):
    def decorator(func):
        def wrap(*args):
            phrase = func(*args)
            new_phrase = phrase
            for i in words:
                if i in phrase:
                    new_phrase = new_phrase.replace(i, "*")
            return new_phrase
        return wrap

    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan("Steve")
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
