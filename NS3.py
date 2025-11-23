
#http://10.72.101.72/Portal/Portal.mwsl?PriNav=Varstate&MultiUseToken=fC3hFSe7FrB6lLotisYgq7Ul5M4%3D&
# v1=DB3.DBX0.0&t1=1&DB3.DBX0.0=
# &v2=DB3.DBX0.1
# &t2=1&DB3.DBX0.1=&v3=DB3.DBX0.2&t3=5&DB3.DBX0.2=&v4=Nueva+variable&t4=+

s=''

for j in range(1):
    s=''
    for i in range(80):
        s+= f"&v{i+1}=DB3.DBB{i+40}"

    print(f"http://10.72.101.72/Portal/Portal.mwsl?PriNav=Varstate&MultiUseToken=fC3hFSe7FrB6lLotisYgq7Ul5M4%3D{s}&DoVars=Aplicar")