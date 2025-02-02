matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
r=len(matrix)
c=len(matrix[0])
mr,mc,mxr,mxc=0,0,r-1,c-1
a=[]
while(len(a)<r*c):
    for j in range(mc,mxc+1):
        a.append(matrix[mr][j])
    mr+=1
    for i in range(mr,mxr+1):
        a.append(matrix[i][mxc])
    mxc-=1
    for j in range(mxc,mc-1,-1):
        a.append(matrix[mxr][j])
    mxr-=1
    for i in range(mxr,mr-1,-1):
        a.append(matrix[i][mc])
    mc+=1
print(a)
