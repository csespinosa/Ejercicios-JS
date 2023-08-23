def text_wrap(string: str, max_width: int):
    wrap = ""

    for word in string:
        if len(wrap) != 0 and len(wrap.replace("\n", "")) % max_width == 0:
            wrap += "\n"
        wrap += word
        
    return wrap

print(text_wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))