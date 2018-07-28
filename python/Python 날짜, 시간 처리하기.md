# Python 날짜, 시간 처리하기 

파이썬에서 날짜와 시간을 다루는 방법을 알아보자. > 새로운 걸 발견하는데로 업데이트 할 것이다. 

- `시간`을 `문자열`로 출력하려면 `strftime` 메서드를 사용하면 된다.

```python
import datetime
 
now = datetime.datetime.now()
print(now)          # 2018-07-28 12:11:32.669083

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)      # 2018-07-28
 
nowTime = now.strftime('%H:%M:%S')
print(nowTime)      # 12:11:32
 
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)  # 2018-07-28 12:11:32
```

날짜, 시간형식의 `문자열`을 `datetime`으로 만들 때도 `strptime`을 사용하면 된다. 

```python
import datetime
 
timeStr = '2018-07-28 12:11:32'
Thistime = datetime.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')

print(type(Thistime)) # [class 'datetime.datetime']
print(myDatetime)       # 2018-07-28 12:11:32
```

**날짜나 시간을 변경**하기 위해서는 `replace` 메서드를 사용하면 된다.

```python
import datetime
 
myDatetime = datetime.datetime.strptime('2018-07-28 12:11:32', '%Y-%m-%d %H:%M:%S')
print(myDatetime)   # 2018-07-28 12:11:32
 
yourDatetime = myDatetime.replace(day=27)
print(myDatetime)   # 2018-07-28 12:11:32
print(yourDatetime) # 2018-07-27 12:11:32
```

**날짜**만을 관리하기 위해서는 `datetime.date`를, **시간**만을 관리하기 위해서는 `datetime.time`을 이용하면 된다. `datetime.date`와 `datetime.time`을 **합치기** 위해서는 `datetime.datetime.combine`을 이용하자.

```python
import datetime
 
d = datetime.date(2018, 7, 28)
t = datetime.time(12, 23, 38)
 
dt = datetime.datetime.combine(d, t)
print(dt) # 2018-07-28 12:23:38
```

`datetime`의 **각 날짜와 시간에 관련된 항목값에 접근**하려면 `timetuple` 메서드를 사용하면 된다.

```python
import datetime
 
now = datetime.datetime.now()
nowTuple = now.timetuple()
print(nowTuple)         
# time.struct_time(tm_year=2018, tm_mon=7, tm_mday=28, tm_hour=13, tm_min=21, tm_sec=40, tm_wday=6, tm_yday=109, tm_isdst=-1)
print(nowTuple.tm_year) # 2018

```

**날짜, 시간 연산**을 해보자. datetime에 하루(1day)를 더하고 싶다면 `datetime.timedelta`를 이용하자.

```python
import datetime
 
now = datetime.datetime.now()
print(now)      # 2018-07-28 12:40:00.320686
 
tomorrow = now + datetime.timedelta(days=1)
print(tomorrow) # 2018-07-29 12:40:00.320686
```

- **`timedelta`**에 들어갈 수 있는 인자값은 아래와 같다.

| 단위  | Method  |
|---|---|
| 1주 | datetime.timedelta(weeks=1)|
| 1일 | datetime.timedelta(days=1) |
|  1시간 | datetime.timedelta(hours=1)|
| 1분 | datetime.timedelta(minutes=1)|
| 1초 | datetime.timedelta(seconds=1)|
| 1밀리초 | datetime.timedelta(milliseconds=1)|
|1마이크로초|datetime.timedelta(microseconds=1)|

>  `timedelta`로 ex> **5시간 30분** 을 표현하면
>
> *  datetime.timedelta(hours=5, minutes=30)
> *  이것을 초(second) 단위로 변경하려면 total_seconds() 메서드를 호출하면 초단위로 쉽게 변경할 수 있다.



`datetime`에서 `datetime`을 빼면 **`timedelta`** 값을 얻을 수 있다.

```python
import datetime
 
a_Datetime = datetime.datetime.strptime('2018-07-28 00:00:00', '%Y-%m-%d %H:%M:%S')
b_Datetime = datetime.datetime.strptime('2018-07-27 00:00:10', '%Y-%m-%d %H:%M:%S')
result = a_Datetime - b_Datetime
print(result)         # 1 day, 0:00:10
print(result.days)    # 1
print(result.seconds) # 10
```

