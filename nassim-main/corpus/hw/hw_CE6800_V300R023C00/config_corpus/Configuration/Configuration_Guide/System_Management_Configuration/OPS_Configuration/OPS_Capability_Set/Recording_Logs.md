Recording Logs
==============

Recording Logs

#### Application Phase

Subscription and execution phases


#### Function Prototype

result1\_value, result2\_description = \_ops.syslog(content, severity="ops.INFORMATIONAL", logtype="ops.SYSLOG")


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| content | Specifies the log content. | The value is a string of 0 to 512 case-sensitive characters. |
| severity | Specifies a log level. | The value is of the enumerated type:   * CRITICAL: indicates a major error. * ERROR: indicates an error. * WARNING: indicates a potential error. * INFORMATIONAL: indicates an informational message.   The default value is **INFORMATIONAL**. |
| logtype | Specifies a log type. | The value is of the enumerated type:   * SYSLOG: user logs * DIAGNOSE: diagnostic logs   The default value is **SYSLOG**. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

Record user logs. The logs can be existing logs on the device or user-defined logs.


#### Usage Examples

When a script is run on a device, some information is recorded in user logs.

```
test.py
import ops 
opsObj = ops.ops()
opsObj.syslog("Record an informational syslog.",ops.INFORMATIONAL,ops.SYSLOG)
```