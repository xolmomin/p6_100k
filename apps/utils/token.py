def token_generator(*args):
    return abs(hash(args))
