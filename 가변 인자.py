# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름:{1}\t 나이 : {1}\t".fomat(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)

def profile(name,age,*language):
    print("이름:{0}\t 나이 : {1}\t".format(name,age),end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python","java","c","c++","c#","javaScript")
profile("김태호",25,"kotlin","swift")