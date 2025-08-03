Triggering Multiple Events
==========================

Triggering Multiple Events

#### Application Phase

Subscription phase


#### Function Prototype

result1\_value, result2\_description = \_ops.trigger(occurs=1, period=30, delay=0, suppress=0)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| occurs | Specifies the number of times that an event meets trigger conditions. | The value is an integer ranging from 1 to 2147483647.  The default value is 1. |
| period | Specifies a detection period.  This parameter is valid only when the and/andnot association condition is defined in the API described in [Combining Multiple Conditions](vrp_ops_cfg_0036.html) or the value of **occurs** in \_ops.trigger is greater than 1. | The value is an integer ranging from 1 to 2147483647, in seconds.  The default value is 30. |
| delay | Specifies a delay for triggering an action.  After a Python script meets its subscription conditions, the execution action will be triggered after a specified delay. The script will be executed immediately for the first time without any delay. | The value is an integer ranging from 0 to 2147483647, in seconds.  The default value is 0. |
| suppress | Specifies the number of times execution of the action in the execution phase is suppressed within a detection period.  This parameter is used together with **period**. | The value is an integer ranging from 0 to 2147483647. If the value is n, it indicates that the event is not triggered after n times within the detection period. If the value is 0, suppression is not triggered. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

The **delay** and **suppress** parameters cannot both be set to non-zero values.

After multiple simple events are combined into a complex event through the API described in [Combining Multiple Conditions](vrp_ops_cfg_0036.html), the corresponding action is triggered if the complex event is matched once in 30 seconds.

When you need to trigger the corresponding action after the complex event is matched multiple times, use the \_ops.trigger.


#### Usage Examples

When a user enters the **display device** and **display this** commands on the terminal, the maintenance assistant is triggered only once within 10 seconds, and "Hello world!" will be displayed.

```
test.py 
import ops 
def ops_condition(_ops): 
       ret1, reason1 = _ops.cli.subscribe("con1","display device",True,True,False,20)
       ret2, reason2 = _ops.cli.subscribe("con2","display this",True,True,False,20)
       _ops.correlate("con1 and con2") 
       _ops.trigger(occurs=1, period=10, delay=0, suppress=0)
def ops_execute(_ops): 
       _ops.terminal.write("Hello world!",None) 
       return 0
```