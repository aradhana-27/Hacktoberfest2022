def sameFreq(str,k):
    words=str.split()
    dict={}
    for w in words:
        dict[w]=dict.get(w,0)+1
    for w in dict:
        if dict[w]==k:
            print(w)
  

str="this is a long string which contains a long passage and is used to solve a question of printing words with same frequency so it contains a lot of words"
k=int(input("Enter the frequency you want to check  \n"))
sameFreq(str,k)