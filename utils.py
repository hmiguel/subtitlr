import hashlib, os

LANGUAGE_PREFERENCES = ['en', 'pt']

def get_prefered_language(available_languages):
    for lang in LANGUAGE_PREFERENCES:
        if lang in available_languages:
            return lang
    return None

def get_hash(name):
    # http://thesubdb.com/api/
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()