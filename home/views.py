from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class Small_covers(View):
    def get(self, request):
        return (render(request,'home/s_cover.html'))

class Small_covers2(View):
    def get(self, request):
        return (render(request,'home/s_cover2.html',{'result1':'', 'result2':'','result3':'','result4':'','result5':'','nthcf':'','dg':'','DN':''}))
        
    def post(self, request):
        FP=request.POST['FP']
        J=request.POST['J']
        dim=Dim(FP)
        FP1=FPcon(FP,dim)
        for i in range(0,len(FP1)):
            quick_sort(FP1[i],0,len(FP1[i])-1)
        FP1=FP2(FP1)
        J=Z(J)
        result1=FP1
        CFs=f(FP1)      
        result2=CFs
        result4=len(CFs) #number of CFs
        result3=FP
        WG=Wedges(FP1,J)
        result1=WG[0]
        quick_sortlen(result1,0,len(result1)-1)
        result5=WG[1] #same vertices before Wedges
        dg=DG(CFs)
        return (render(request,'home/s_cover2.html',{'result1':result1,'result2':result2, 'result3':result3,'result4':result4,'result5':result5,'nthcf':'','dg':dg,'DN':''} ) )

class Small_covers3(View):
    def get(self, request):
        return (render(request,'home/s_cover2.html',{'result1':'', 'result2':'','result3':'','result4':'','result5':'','nthcf':'','dg':'','DN':''}))
    
    def post(self, request):
        result1=request.POST['result1']
        result2=request.POST['result2']
        FP=request.POST['result3']
        dim=Dim(FP)
        FP1=FPcon(FP,dim)
        for i in range(0,len(FP1)):
            quick_sort(FP1[i],0,len(FP1[i])-1)
        FP1=FP2(FP1)
        CFs=f(FP1)
        dg=DG(CFs)
        result4=request.POST['result4']
        result5=request.POST['result5']
        n=int(result4)
        nth=request.POST['nth']
        nth=int(nth)
        nth2=request.POST['nth2']
        nth2=int(nth2)
        if nth>n:
            nthcf=''
        else:
            nthcf=nthcff(result2,nth)
        DN=FDG(nth,dg,nth2)
        
        return (render(request,'home/s_cover2.html',{'result1':result1,'result2':result2, 'result3':FP,'result4':result4,'result5':result5,'nthcf':nthcf,'dg':dg,'DN':DN} ) )

from itertools import combinations
import sympy as sy

def FPcon(FP,dim):
    FP1=[]
    i=2
    j=1
    while i<len(FP)-1:
            if j==1:
                FP1=FP1+[[int(FP[i])]]
                i=i+2
                j=j+1
            elif j==dim:
                FP1[-1]=FP1[-1]+[int(FP[i])]
                i=i+4
                j=1
            else:
                FP1[-1]=FP1[-1]+[int(FP[i])]
                i=i+2
                j=j+1
    return FP1

def Z(a):
    b=1
    c=[]
    while b<len(a):
        c=c+[int(a[b])]
        b=b+2
    return c

def Dim(FP):
    for i in range(0,len(FP)):
        if FP[i]==']':
            break
    i=i-3
    i=i//2+1
    return (i)

def S0(n): #Z2n 모든 벡터(차원)
	a=[]
	for i in range(0,n):
		a=a+[i]
	S0=[]
	for i in range(1,n+1):
		S0=S0+list ( combinations(a,i) )
	S=[]
	for i in range(0,len(S0)):
		s=[0]*n
		for j in S0[i]:
			s[j]=1
		S=S+[s]
	return S

def L0(S,n): #n항등행렬(Z2n,차원)
	L=[]
	for i in range(0,n):
		L=L+[S[i]]
	return L


def VS(a,b): #리스트 벡터 합
    s=[]
    for i in range(0,len(a)):
        s=s+[a[i]+b[i]]
    return s



def f(FP):  #small cover 전부 구하기
    m=0
    n=len(FP[-1])
    for i in range(0,len(FP)):
        m=max(m,max(FP[i]))
    i=n+1
    S1=S0(n)
    L1=L0(S1,n)+[0]*(m-n)
    G=[]
    S=[0]*m
    ls0=[0]*n
    c=1
    d=1
    while 1:
        if c==1 and d==1:
            S[i-1]=S1
            for j in FP:
                if max(j)==i:
                    ls=ls0[:]
                    for k in range(0,len(j)-1):
                        ls=VS(ls,L1[j[k]-1])
                    for k in range(0,len(ls)):
                        if ls[k]%2==0:
                            ls[k]=0
                        else:
                            ls[k]=1
                    for p in range(0,len(S[i-1])):
                        if S[i-1][p]==ls:
                            if len(S[i-1])==p:
                                S[i-1]=S[i-1][:p]
                            else:
                                S[i-1]=S[i-1][:p]+S[i-1][p+1:]
                            break
        if d==1 and i==n:
            break
        if S[i-1]==[]:
            i=i-1
            c=0
            d=1
        else:
            c=1
        if c==1:
            L1[i-1]=S[i-1][0]
            if len(S[i-1])>1:
                S[i-1]=S[i-1][1:]
            else:
                S[i-1]=[]
            if i==m:
                G=G+[L1[:]]
                d=0
            if i<m:
                i=i+1
                d=1
    return G


def partition(c, start, end):
	pos = start
	for i in range(start+1, end+1):
		if c[i] < c[start]:
			c[pos+1], c[i] = c[i], c[pos+1]
			pos += 1
	c[pos], c[start] = c[start], c[pos]
	return pos

def quick_sort(c, start, end):
	if start < end:
		pos = partition(c, start, end)
		quick_sort(c, start, pos-1)
		quick_sort(c, pos+1, end)

def partitionlen(c, start, end):
	pos = start
	for i in range(start+1, end+1):
		if len(c[i]) < len(c[start]):
			c[pos+1], c[i] = c[i], c[pos+1]
			pos += 1
	c[pos], c[start] = c[start], c[pos]
	return pos

def quick_sortlen(c, start, end):
	if start < end:
		pos = partitionlen(c, start, end)
		quick_sortlen(c, start, pos-1)
		quick_sortlen(c, pos+1, end)
 
 
def FP2(FP):  #making simplicial cpx from facets
    FP1=[]
    for i in FP:
        for j in range(1,len(i)+1):
            FP1=FP1+list(combinations(i,j))
    FP1=list(set(FP1))
    for i in range(0,len(FP1)):
        FP1[i]=list(FP1[i])
    return FP1

def MSM(A): #똑같은 행렬 만들기
    B=sy.Matrix(A.row(0))
    for i in range(1,len(A.col(0))):
        B=sy.Matrix((B,A.row(i)))
    return B

def MM(a):   #making matrices from lists
    A=[]
    for i in a:
        A=A+[sy.Matrix(i).T]
    return A

def nthcff(a,n):
    s=0
    s1=0
    s2=0
    c=0
    c2=0
    b=[]
    for i in range(1,len(a)):
        if (s2==0 and a[i]==']'):
            if s==0:
                s1=s1+1
            if a[i+1]==']':
                s=s+1
            if s==n:
                p=i
                s2=1
        if (c2==0 and a[i]=='[') and a[i+1]=='[':
            c=c+1
            if c==n:
                j=i
                c2=1
        if c2==1 and s2==1:
            break
    for k in range(j+2,p):
        if (a[k] != '[' and a[k] != ']') and (a[k] != ',' and a[k] != ' '):
            b=b+[int(a[k])]
    f=[]
    for i in range(1,s1+1):
        k=i*len(b)//s1
        e=[]
        for j in range(k-len(b)//s1,k):
            e=e+[b[j]]
        f=f+[e]
    return f

def Z2S(a,b):  #mod2에서의 합
    c=a+b
    for i in range(0,len(c)):
        if c[i]%2==1:
            c[i]=1
        else:
            c[i]=0
    return c

def ro(A,i,k):  #행렬의 한 원소와 같은 col에 있는 다른 원소들이 1이면 그 원소를 포함하는 row에 처음의 원소를 포함하는 row를 더함
    for j in range(0,len(A.col(0))):
        if A[j,k]%2==1 and j != i:
            a=Z2S(A.row(j),A.row(i))
            A.row_del(j)
            A=A.row_insert(j,a)
    return A


def rref(A1):  #mod2에서 rref만들기
    A=MSM(A1)
    n=min(len(A.col(0)),len(A.row(0)))
    i=0
    p=0
    while i<n and p<len(A.row(0)):
        if A[i,p]==1:
            A=ro(A,i,p)
            i=i+1
            p=p+1
            continue
        for j in range(i,len(A.col(0))):
            if A[j,p]==1:
                a=A.row(j)
                b=A.row(i)
                A.row_del(j)
                A=A.row_insert(j,b)
                A.row_del(i)
                A=A.row_insert(i,a)
                break
        if A[i,p]==0:
            p=p+1
            continue
        A=ro(A,i,p)
        if A[i,p-1]==0:
            ro(A,i,p)
    return(A)


def CC(A,c):  #c번째 col을 맨 앞으로 보내기
    a=A.col(c)
    B=MSM(A)
    B.col_del(c)
    B=B.col_insert(0,a)
    return(B)

def ind(A,a):  #list의 index
    for i in range(0,len(a)):
        if a[i]==A:
            return(i)

def g(A,B,c):  #두 행렬의 projectied 연결? (행렬,행렬,col)
    d=0
    e=0
    A1=CC(A,c)
    B1=CC(B,c)
    for i in range(0,len(A1.col(0))):
        if A1[i,0]==1 and d==0:
            d=1
            i1=i
        if B1[i,0]==1 and e==0:
            e=1
            i2=i
        if d==1 and e==1:
            break
    A1=ro(A1,i1,0)
    B1=ro(B1,i2,0)
    A1.row_del(i1)
    A1.col_del(0)
    B1.row_del(i2)
    B1.col_del(0)
    A1=rref(A1)
    B1=rref(B1)
    if A1==B1:
        return [[A,B],c]

def PJ(A,c): #c번째 col에서 PJ
    A1=CC(A,c)
    for i in range(0,len(A1.col(0))):
       if A1[i,0]==1:
            break
    A1=ro(A1,i,0)
    A1.row_del(i)
    A1.col_del(0)
    A1=rref(A1)
    return A1

def DG(a):
    a=MM(a)
    dg=[]
    for k in range(0,len(a[0].row(0))):
        for i in range(0,len(a)):
            a1=a[i]
            A1=PJ(a1,k)
            for j in range(i+1,len(a)):
                a2=a[j]
                B1=PJ(a2,k)
                if A1==B1:
                    dg=dg+[[[ind(a1,a),ind(a2,a)],k]]
    for i in range(0,len(dg)):
        dg[i][1]=dg[i][1]+1
        for j in range(0,2):
            dg[i][0][j]=dg[i][0][j]+1
    return dg

def FDG(nth,DG,j):
    s=[]
    for i in range(0,len(DG)):
        if (intersect(DG[i][0],[nth]) != []) and (DG[i][1]==j):
            s=s+[DG[i]]
    return(s)
    

def union(A,B):
    C=A+B
    C=list(set(C))
    return C
    
def intersect(A,B):
    C=[]
    for i in A:
        for j in B:
            if i==j:
                C=C+[i]
                break
    return C
    
    
    
def Check(A,B):
    for i in range(0,len(B)):
        if A==B[i]:
            return 1
    return 0
    
    
def LK(x,FP):
    LK=[]
    for i in FP:
        a=union([x],i)
        quick_sort(a,0,len(union([x],i))-1)
        if intersect([x],i)==[] and Check(a,FP)==1:
            LK=LK+[i]
    return LK
    
def Join(FP1,FP2):
    J=[]
    for i in FP1:
        for j in FP2:
            J=J+[union(i,j)]
    return J
    
def Subt(A,B):
    C=B
    c=[]
    for i in range(0,len(B)): 
        if B[i]==A or Check(A[0],B[i])==1:
            c=c+[i]
    for i in range(0,len(c)):
        C=C[:c[i]]+C[c[i]+1:]
        for j in range(0,len(c)):
            c[j]=c[j]-1
    return C


def Wedges(FP,J):
    A=FP
    u=0
    for i in range(0,len(J)):
        for j in range(0,J[i]-1):
            A=Wedge(i+u+1,A)
            u=u+1
    VN=[]
    p=1
    for j in range(0,len(J)):
        VN=VN+[[]]
        for k in range(0,J[j]):
            VN[j]=VN[j]+[p]
            p=p+1        
    return [A,VN]

def maxv(FP):
    m=0
    for i in FP:
       m2=max(i) 
       m=max(m,m2)
    return(m)                
    


def Wedge(i,FP):
    for p in range(0,len(FP)):
        for q in range(0,len(FP[p])):
            if FP[p][q]>i:
                FP[p][q]=FP[p][q]+1
    a=Join([[],[i],[i+1],[i,i+1]],LK(i,FP))
    b=Join([[],[i],[i+1]],Subt([i],FP))
    A=union2(a,b)
    for p in range(0,len(A)):
        quick_sort(A[p],0,len(A[p])-1)
    c=[A[0]]
    for p in range(1,len(A)):
        k=0
        q=0
        for q in range(0,len(c)):
            if A[p]==c[q]:
                k=1
                break
        if k==0:
            c=c+[A[p]]
    return c
    
    
def union2(A,B):
    U=A+B
    return U