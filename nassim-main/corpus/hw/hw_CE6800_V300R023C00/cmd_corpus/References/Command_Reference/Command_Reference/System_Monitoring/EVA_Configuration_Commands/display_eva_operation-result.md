display eva operation-result
============================

display eva operation-result

Function
--------



The **display eva operation-result** command displays the query result.




Format
------

**display eva operation-result** *fileName*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *fileName* | Specifies the name of a script. | The value is a string of 4 to 16 case-sensitive characters. It must start with a letter and end with .py. It can contain digits, letters, and underscores(\_). |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run the display eva operation-result command to check the action execution result of a script.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the action execution result of the test.py script.
```
<HUAWEI> display eva operation-result test.py
--------------------------------------------------------------------------------
ActionTime:2022-02-12 15:12:29
StrategyFormula:
ActionName:log
OutputInfo:
ActionResult:
EventName = ops_cpu
DataValue = 3.000
cpu-id = 0
slot-id = 1

```

**Table 1** Description of the **display eva operation-result** command output
| Item | Description |
| --- | --- |
| ActionTime | Time when an action is executed. |
| StrategyFormula | Matching policy. |
| ActionName | Name of an action.   * log: displays diagnostic logs. * scriptNest: enables nested scripts. * uninstall: disables nested scripts. * netconf.Exec: NETCONF RPC operation. * netconf.Get: NETCONF get operation. |
| OutputInfo | Entity of the action. |
| ActionResult | Action execution result. |