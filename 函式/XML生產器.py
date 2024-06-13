def myxml(tag, content='', **kwargs):  # **kwargs接收數量不定的關鍵字參數(dict物件)
    attrs_list = []
    for key, value in kwargs.items():
        # 把屬性轉字串放入list
        attrs_list.append(f'{key}="{value}"')
    attrs = ''.join(attrs_list)
    return f'<{tag}{attrs}>{content}</{tag}>'


print(myxml('foo', 'bar', a=1, b=2, c=3))
