from functools import reduce
import time

def profile(f):
    def fToString(*args, **kwargs):
        ans=f.__name__
        ans=ans+"("
        sep=""
        for a in args:
            ans=ans+sep+str(a)
            sep=","
            pass
        for k in kwargs:
            ans=ans+sep+str(k)+"="+str(kwargs[k])
            sep=","
            pass
        ans=ans+")"
        return ans
    #@wraps(f)
    def wrapper(*args,**kwargs):
        start=time.clock()
        ans=f(*args,**kwargs)
        end=time.clock()
        print(fToString(*args,**kwargs) + " took " + str(end - start) + " seconds")
        return ans
    return wrapper


@profile
def factp(n):
    def fact(n):
        if n<=0:
            return 1;
        else:
            return fact(n-1)*n;
        pass
    print(str(fact(n)))

@profile
def factr(n):
    print(reduce(lambda x,y:x*y , [x for x in range(1,n+1)]))
    pass

factr(5)
factp(6)
