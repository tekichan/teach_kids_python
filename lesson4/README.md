# 第四課：for循環
本課是介紹循環概念。循環的意思是指令電腦不斷重覆某項工作。例如，體育課老師命令同學來回跑二十次，就是把來回跑這個動作重覆二十次。

本課所用的循環指令是for。特點是先給予一系列的數字，於每次循環中，從該系列中順序抽出一數字出來。例如：
```python
for odd_number in [1, 3, 5, 7, 9]:
  # next action
```
於每次循環中，Python順序地分別把1、3、5、7和9放入odd_number這個變量中，並執行以下的指令（即是 #next actio或以下的部分）。換言之，完成所有循環後，#next actio或以下的部分會總共執行了五次。留意！for循環以下的重覆指令會先開首留四格空格，這是Python的語法。

Python的for循環語法是 **for** *每次循環變更的變量* **in** *變量列* **:**，此句以下每次循環執行的指令都開首留空四格，直至有指令不再留空兩格為止，才離開循環。

本課的例子便使用`for`來幫助用家重覆不同大小的正方形繪畫有趣的圖案。