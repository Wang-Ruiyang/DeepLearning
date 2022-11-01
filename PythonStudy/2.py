def hanoi(n,x,y,z):
    if n==1:    #只有一层了
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)     #将x上n个移到z的问题 转为 将x上面n-1个移到y的问题
        print(x,'-->',z)     #将x中剩下的唯一一个（也是最大的），移到z
        hanoi(n-1,y,x,z)     #将y上的n-1（全部）移到z中，也就是以y为起点，移动到z

n = int(input('请输入汉诺塔的层数:'))
hanoi(n,'A','B','C')
        
           
