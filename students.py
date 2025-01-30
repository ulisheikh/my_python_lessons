def get_info(**kwargs):
    while 1:
        kalit = input("Qanday ma'lumot kiritmoqchisiz?>>>\n")
        if kalit == "exit":
            break
        qiymat = input(f"{kalit}ni kiriting>>>\n")
        kwargs[kalit] = qiymat
    print(kwargs)
    return kwargs

def i_print(data):
    for k,v in data.items():
        print(f"Kalit {k}ning qiymati {v}")
    return data