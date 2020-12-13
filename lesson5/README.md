# 第五課：while循環
本課是介紹另一個循環方法 - while。特點是先給予執行循環的判斷條件，如果條件符合，就會執行循環內的部份。例如：
```python
i = 0
while i < 10:
    # next action
```
當Python執行 `while i < 10:`的時候，會先判斷變量`i`是否少於`10`。如果是的話，便執行下列循環內的代碼。當循環內的代碼執行完成，便會再次執行 `while i < 10:`的時候，並判斷變量`i`是否少於`10`。周而復始，直至`while i < 10:`的判斷為`False`「非」，便會離關循環。

Python的`while`循環語法是 **while** *每次循環的判斷式* **:**，此句以下每次循環執行的指令都開首留空四格，直至有指令不再留空兩格為止，才離開循環。

跟`for`循環比較，`for`循環依照提供的數據列而執行，所以循環次數較為固定。`while`循環則依照判斷式的結果而執行，而被判斷的變量可以在循環內有各式的變化，所以循環次數也較為彈性。以下雨段代碼結果相同，你可以比較`for`與`while`的方別：
```python
# Example 1: print out first 5 even numbers
for i in [2, 4, 6, 8, 10]:
    print(i)
```

```python
# Example 2: print out first 5 even numbers
i = 2
while i <= 10:
    print(i)
    i = i + 2   # i is increased by 2 every time
```

本課的例子代碼 [**circle_pattern.py**](/lesson5/circle_pattern.py) 便使用`while`來幫助用家每隔某固定角度重覆繪畫圓形，從而組成有趣的圖案。