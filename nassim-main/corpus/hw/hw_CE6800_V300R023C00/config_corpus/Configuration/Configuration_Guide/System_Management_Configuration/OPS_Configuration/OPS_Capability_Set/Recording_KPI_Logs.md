Recording KPI Logs
==================

Recording KPI Logs

#### Application Phase

Execution phase


#### Function Prototype

result1\_value, result2\_description = ops.kpi.log(action, reason)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| action | User-defined character string, which is used to record events. | The value is a string of 1 to 49 case-insensitive characters, excluding the end character **\0**. |
| reason | User-defined character string, which records the fault cause. | The value is a string of 1 to 1023 case-insensitive characters, excluding the end character **\0**. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value, indicating the failure cause. It is returned only when the first return value is 1.


#### Usage Description

The event execution result is recorded and stored in the action\_data (action, reason, action\_time, script\_name) table in the GMDB.

When the KPI event log recording interface (ops.kpi.log) is used:

* The system automatically obtains the script name. Ensure that the script name ends with .py. Otherwise, the operation fails.
* The system automatically records the event time specified by action\_time.

#### Usage Examples

Create a script named test\_log.py to record the execution result of the cpu\_usage event.

```
def ops_condition(_ops)
    e1 = _ops.kpi.event("cpu")
    e1.add_inner(10167, 0)
    e1. set_threshold(">", 90)
    e1. set_compute_rule("avg", 5)
    _ops.kpi.subscribe(e1)
def ops_execute(_ops)
    _ops.kpi.log("cpu usage alarm", "the temperature is too high")
```