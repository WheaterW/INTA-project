display radius-server max-unresponsive-interval
===============================================

display radius-server max-unresponsive-interval

Function
--------



The **display radius-server max-unresponsive-interval** command displays configuration information about the longest unresponsive interval of a RADIUS server.




Format
------

**display radius-server max-unresponsive-interval**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After the longest unresponsive interval of a RADIUS server is configured using the **radius-server max-unresponsive-interval** command, you can run the **display radius-server max-unresponsive-interval** command to display configuration information about the longest unresponsive interval of the RADIUS server.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configuration information about the longest unresponsive interval of the RADIUS server.
```
<HUAWEI> display radius-server max-unresponsive-interval
Radius server max non-response interval(in seconds) is 400.

```

**Table 1** Description of the **display radius-server max-unresponsive-interval** command output
| Item | Description |
| --- | --- |
| Radius server max non-response interval(in seconds) is | Longest unresponsive interval of the current RADIUS server. |