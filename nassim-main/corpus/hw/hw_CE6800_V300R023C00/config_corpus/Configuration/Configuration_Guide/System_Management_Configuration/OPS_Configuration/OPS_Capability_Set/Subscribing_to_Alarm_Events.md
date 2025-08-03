Subscribing to Alarm Events
===========================

Subscribing to Alarm Events

#### Application Phase

Subscription phase


#### Function Prototype

result1\_value, result2\_description = \_ops.alarm.subscribe(tag, feature, event, condition[4]=None, alarm\_state=start, occurs=1, period=30)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| tag | Specifies conditions. | The value is a string of 1 to 8 case-sensitive characters, consists of letters, digits, and underscores (\_), and starts with a letter. The value of **tag** cannot be **and**, **or**, or **not**. If only one condition is subscribed to in the script, the value can be an empty string. If multiple conditions are subscribed to, the value cannot be empty and must be unique in the script. |
| feature | Specifies the name of a feature. | The value is a string of 1 to 225 case-sensitive characters, for example, CMF\_LOG\_LOCK.  You can run the [**display info-center log-server log-dictionary**](cmdqueryname=display+info-center+log-server+log-dictionary) command in the diagnostic view to view all log names based on the **LOGNAME** field. |
| event | Specifies the name of an event. | The value is a string of 2 to 63 case-sensitive characters, for example, VFM\_FLHSYNC\_FAIL. |
| condition[4] | Specifies a condition array. | A maximum of four parameter conditions can be set. For example:  conditions = []  con1 = {'name':'ifIndex', 'op':'eq', 'value':'100'} conditions.append(con1)  con2 = {'name':' vpnInstance', 'op':'eq', 'value': 'abc'} conditions.append(con2)  **name** indicates the parameter name, **op** indicates the judgment type, **eq** indicates equal to, and **value** is the comparison value determined by **op**. For details, see [condition alarm level](vrp_ops_cfg_0009.html#EN-US_TASK_0000001512685906__p171631239115919).  If no parameter condition needs to be set, leave this parameter blank, indicating that the action execution condition is met when an alarm is triggered. |
| alarm\_state | Specifies the alarm status. | The value is of the Boolean type:  start: An alarm is generated.  end: The alarm is cleared.  The default value is **start**. |
| occurs | Specifies the number of occurrences in a period. | The value is an integer ranging from 0 to 4294967295. |
| period | Specifies a period. | The value is an integer ranging from 0 to 4294967295. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

You can subscribe to alarms. When an alarm occurs, the assistant is triggered. (You can run the **display alarm information** command in the diagnostic view to query information about all events that can be subscribed to.)


#### Usage Examples

When the device generates the CMF\_LOG\_LOCKBackwardTransition alarm, the assistant is triggered.

```
test.py
import ops 
def ops_condition(_ops):
   _ops. alarm.subscribe("alm1", "CMF_LOG_LOCK", "CMF_LOG_LOCKBackwardTransition", condition, alarm_state='start')
   _ops.correlate("alm1")
def ops_execute(_ops):
   handle, err_desp  = _ops.cli.open()
   _ops.cli.execute(handle,"display device > ops_test.log")
   ret = _ops.cli.close(handle) 
   return 0 
```