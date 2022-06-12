# 线程与进程
# 进程： 资源单位
# 线程：执行单位
# 启动每一个程序默认都会有一个主线程

# 单线程
# def func():
#   for i in range(1000):
#     print('func', i)

# if __name__ == '__main__':
#   func()
#   print('你好啊')

# 多线程
from threading import Thread # 线程类

# 方式一
# def func():
#   for i in range(1000):
#     print('func', i)

# if __name__ == '__main__':
#   t = Thread(target=func) # 创建线程并给线程任务
#   t.start() # 多线程状态为开始工作状态，具体执行时间由 CPU 决定
#   for i in range(1000):
#     print('main', i)

# 方法二  继承类
# class MyThread(Thread):
#   def run(sef): # 固定的， 当线程被执行的时候，被执行的就是run()
#     for i in range(10000):
#       print('子线程', i)

# if __name__ == '__main__':
#   t = MyThread()
#   # t.run() # 方法的调用了 -> 单线程
#   t.start() # 开启线程
#   for i in range(10000):
#     print('主线程', i)

# 传参
def func(name):
  for i in range(1000):
    print(name, i)

if __name__ == '__main__':
  t = Thread(target=func, args=('周杰伦',)) # 传递的参数必须是元组
  t.start() # 
  t2 = Thread(target=func, args=('成龙',)) # 
  t2.start() # 
  # for i in range(1000):
  #   print('main', i)
