for  x  in  range(0,20):
        for  y  in  range(0,33):
                z  =  100  -  x  -  y
                if  5*x  +  3*y  +  z/3  ==  100:
                        print('鸡翁  %d  只，鸡母  %d  只，鸡雏  %d  只'  %  (x,  y,  z))