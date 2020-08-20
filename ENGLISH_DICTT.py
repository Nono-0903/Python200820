d = {}
print("######################")
print("**歡迎來到英文高手系統**")
print("######################")
      
while True:
    print("1.建立字彙表")
    print("2.列出全部單字")
    print("3.英文翻譯成中文")
    print("4.中文翻譯成英文")
    print("5.測驗學習成果")
    print("6.離開系統")
    
    option = input("請輸入你想要的功能(代號):")
    
    if option == "6":
        break
    elif option == "1":
        while True:
            voc = input("請輸入新英文單字(按0離開):")
            if voc == '0':
                break
            if voc not in d:
                voc_ch = input("中文解釋:")
                d[voc] = voc_ch
            else:
                print("已經有了!")
    elif option == '2':
            s = sorted(d)
            print(s)
            for i in s:
                print(i,":",d[i])
    elif option == '3':
        while True:
            voc = input("請輸入英文單字(按0離開):")
            if voc == '0':
                break
            if voc in d:
                print(voc,'的中文是',d[voc])
            else:
                print("沒有這個單字")
    elif option == '4':      
        while True:
            got = False
            ch = input('請輸入中文:(按0離開):')
            if ch == '0':
                break
            for k,v in d.items():
                if ch == v:
                    print (ch,"的英文是",k)
                    got = True
            if got == False:
                print("沒有這個單子")
    elif option == '5':
        score = 0
        for k,v in d.items():
            print(v,':')
            ans = input()
            if ans == k:
                score +=1
                print('答對!!')
            else:
                print("答錯!!!")
        print('總共拿到',score,'分')
                