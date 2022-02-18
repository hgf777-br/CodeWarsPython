import sys
sys.setrecursionlimit(20000)
xrange=range
class np:
  @staticmethod
  def argsort(x):
    s, _ = zip(*sorted(enumerate(x),key=lambda x:x[1]))
    return s
  @staticmethod
  def mean(ls):
    return 1.*sum(ls)/len(ls)


def pairs_mapping(prs,num):
    ## Sort ordering of prs by mean node degree for pair
    global d
    d={i:0 for i in xrange(1,num+1)}
    for i,j in prs:
        d[i]+=1
        d[j]+=1
    perm=np.argsort([np.mean([d[i],d[j]]) for i,j in prs])
    
    global dg
    dg=[d[i] for i in xrange(1,num+1)]
     
    satDeg=[0]*num
     
    for i,j in prs:

        satDeg[i-1]+=dg[j-1]
        satDeg[j-1]+=dg[i-1]

     
    return d,satDeg,[prs[i] for i in perm]


def findPairs(num):

    pairs = []
    hi = num+num-1

    psqs = [i for i in xrange(2, hi) if int(i**(0.5)) == i**(0.5)]

    # for each e in psqs create links (e-1,1)....(2,e-2)
    for e in psqs:
        pairs += [(i, e-i) for i in range(1, e-1) if i < e-i and max(i, e-i) <= num]


    return pairs


def Fathom(seqList, prs, dg, num):

     

    r=[dg[x] for x in dg if x not in seqList]
     

    if not all(k>0 for k in r):
        return seqList,False

    if  r.count(1)>1:
         return seqList,False
 
    def filterPairs(prs,lastButOne):# (10,6) dont want((6,10)
        def check(x):
            #deduct 1 from the degree of each adjacent node to arc x
            if lastButOne==x[1]:
                dg[x[0]]-=1
            else:
                dg[x[1]]-=1
             

  
        return list(filter(lambda x: not (x[1]==lastButOne or x[0]==lastButOne  ) ,prs))
        
         
    
    def adjustDegrees(x,dg,num):
        # reduce degree of nodes connected to
        # x
        for i,j in prs:
            if x==i: # j is connected to x
                if j in dg:
                    dg[j]-=1
            elif x==j: # i is connected to x
                if i in dg:
                    dg[i]-=1


        return dg

    assert seqList!=[] , "Depth First has forbidden seqList ==[] "
    if prs==None:
        print(num)
        print(seqList)
    assert prs!=None , "prs is None error"
    
    
    if len(prs)<num-len(seqList):
        return seqList,False
     
    L=len(seqList)

    if len(seqList)==num:
        return seqList,True
    el= seqList[-1]
    #print seqList
    if len(seqList)>1:
        prev=seqList[-2]
        candidates=[c for c in prs if el in c and not(prev in c)]
    else:
        candidates=[c for c in prs if el in c]#c[0]==el or c[1]==el]
    # order candidates by degree
    candidates=sorted(candidates,key=lambda x:dg[x[0]] if x[0]!=el else dg[x[1]])
     
    if candidates==[]:
        return seqList,False

    YN=False
    soln=[]
     
    try:
        del dg[seqList[-2]]
    except:
        gh=34
    for first,second in candidates:
        if first==el:
            f,s=el,second # So adding second
            if s not in seqList:
                fp=filterPairs(prs,seqList[-2]) if len(seqList)>1 else prs
                ap=adjustDegrees(el, dict(dg), num)
                soln,YN=Fathom(seqList+[second], fp, ap, num)


                if YN : return soln,True


        else:#if second==seqList[-1] :#and len(seqList)>1:
            f,s=el,first

            if s not in seqList:

                fp=filterPairs(prs,seqList[-2]) if len(seqList)>1 else prs
                ap=adjustDegrees(el, dict(dg), num)
                soln,YN=Fathom(seqList+[first], fp, ap, num)
                if YN==True:
                    return soln,True


    return soln,False

def collectCounts(prs):
    collect={i:0 for i in xrange(1,num+1)}
    for (i,j) in prs:
        collect[i]+=1
        collect[j]+=1

    print(collect)

    return collect

def DepthFirst(num):
    prs = findPairs(num)
    if len(prs)<num-1:
        print("No soln")
        return False
    d,satDeg,prs=pairs_mapping(prs,num)

    n_ordering=np.argsort(d.values())

    dx=[d[i+1]+satDeg[i] for i in xrange(0,num)]
    dx=np.argsort(dx)
    r=prs#range(num,0,-1)

    Y=range(1,num+1)
    
    global dg
    copy_dg=list(d.items())
    copy_dg=dict(d)

    for i in dx:#n_ordering: # was d

        print(i)


        dg=dict(copy_dg)
        KL=len(prs)
        soln,YN=Fathom([i],prs,dg, num)

        if YN==True: break
    print(YN)
    if not YN: return False
    return soln


def square_sums_row(num):
    soln = DepthFirst(num)
    return soln


n = 1000

print(f"Final ({n}) : {square_sums_row(n)}")
