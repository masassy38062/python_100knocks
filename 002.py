#02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．


msg1 = "パトカー"
msg2= "タクシー"
msg_add=''

for i in range(0,len(msg1)):
    msg_add += msg1[i]
    msg_add += msg2[i]

print(msg_add)