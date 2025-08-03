Subscribing to Timer Events
===========================

Subscribing to Timer Events

#### Application Phase

Subscription phase


#### Function Prototype

result1\_value, result2\_description = \_ops.timer.cron(tag, crontime)

result1\_value, result2\_description = \_ops.timer.relative(tag, timelength)

result1\_value, result2\_description = \_ops.timer.absolute(tag, timelength)

result1\_value, result2\_description = \_ops.timer.countdown(tag, timelength)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| tag | Specifies conditions. | The value is a string of 1 to 8 case-sensitive characters, consists of letters, digits, and underscores (\_), and starts with a letter. The value of **tag** cannot be **and**, **or**, or **not**. If only one condition is subscribed to in the script, the value can be an empty string. If multiple conditions are subscribed to, the value cannot be empty and must be unique in the script. |
| crontime | Specifies a cron timer description. | The value is a character string in the *m h d M D Y* format.   * *m*: specifies the minute. The value is an integer ranging from 0 to 59. * *h*: specifies the hour. The value is an integer ranging from 0 to 23. * *d*: specifies the day in a month. The value is an integer ranging from 1 to 31. * *M*: specifies the month. The value is an integer ranging from 1 to 12. * *D*: specifies the day in a week. The value is an integer ranging from 0 to 7. The values 0 and 7 indicate Sunday, and the values 1 to 6 indicate Monday to Saturday. * *Y*: specifies the year. The value is an integer ranging from 2000 to 2099. *Y* is optional. If *Y* is not specified, it indicates the current year. |
| timelength | Specifies the timer duration. | The value is an integer ranging from 0 to 4294967295, in seconds. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

If multiple simple events are defined using a timer in the subscription phase but the simple events are not combined using the interface described in [Combining Multiple Conditions](vrp_ops_cfg_0036.html), the Python script assistant cannot be configured successfully.

The timer event subscription API provides four timers:

* cron is a timer defined based on CRON standards of the UNIX operating system and the cron timer time is in the *m h d M D Y* format.
  + If *m* is \*, the action in the execution phase is executed every minute. If *h* is \*, the action in the execution phase is executed every hour. The same rule applies to *d*, *M*, *D*, and *Y*. If *Y* is \* or is not specified, the action in the execution phase is executed every year.
  + If *m* is a-b, the action in the execution phase is executed from the ath minute to the bth minute. If *h* is a-b, the action in the execution phase is executed from the ath hour to bth hour. The same rule applies to *d*, *M*, *D*, and *Y*.
  + If *m* is \*/n, the action in the execution phase is executed every n minutes. If *h* is \*/n, the action in the execution phase is executed every n hours. The same rule applies to *d*, *M*, *D*, and *Y*.
  + If *m* is "a, b, c,... ", the action in the execution phase is executed in the ath, bth, cth minute and so on. If *h* is "a, b, c,... ", the action in the execution phase is executed in the ath, bth, cth hours and so on. The same rule applies to *d*, *M*, *D*, and *Y*.
  
  For example, "15 16 1 \* \*" indicates that the action in the execution phase is executed at 16:15 on the first day of each month, and "0 12 \* \* 1-5" indicates that the action in the execution phase is executed at 12:00 from Monday to Friday in each week.
* relative indicates a cyclic timer, and the action in the execution phase is executed every **timelength** value seconds.
* absolute indicates an absolute timer, **timelength** indicates the number of seconds calculated since 00:00 on January 1, 1970, and the action in the execution phase is executed when the timer expires.
* countdown indicates a one-time triggering timer. After the script initialization is complete and the **timelength** value is counted down, the action in the execution phase is triggered only once.

#### Usage Examples

A timer event is triggered every 5s after the timer event is subscribed.

```
test.py 
def ops_condition(_ops):
       _ops.timer.relative("timer1",5)                   # Create a timer named timer1 with a countdown of 5s.
       _ops.correlate("timer1")                            # Associate timer1 with the OPS instance. When the timer condition is met, the _execute operation is performed.
def ops_execute(_ops): 
       _ops.syslog("Record an informational syslog.") 
       return 0
```