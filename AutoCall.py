import os
import time

path=input("输入号码的路径:")
f=open(path,mode="r")
phone_number=[]
for each_line in f:
    if each_line[-1]=="\n":
        phone_number.append(each_line[:-1])
    else :
        phone_number.append(each_line)
print("测试号码为：")
print(phone_number)
i=0
handup="adb shell input keyevent 6"
log_file=open(path[:-4]+"_log.txt",mode='a')
for i in range(len(phone_number)):
    cmd = 'adb shell am start -a android.intent.action.CALL tel:'+ phone_number[i]
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"拨打电话"+str(phone_number[i]))
    log_file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"拨打电话"+str(phone_number[i]+";"))
    os.system(cmd)
    time.sleep(20)
    print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"挂断电话"+str(phone_number[i])))
    log_file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"挂断电话"+str(phone_number[i])+"\n")
    os.system(handup)
    time.sleep(10)
    log_file=open(path[:-4]+"_log.txt",mode='a')
    log_file.close
end=input("输入任意字符结束")
