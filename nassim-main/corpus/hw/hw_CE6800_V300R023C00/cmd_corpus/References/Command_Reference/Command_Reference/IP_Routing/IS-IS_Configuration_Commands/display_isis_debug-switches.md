display isis debug-switches
===========================

display isis debug-switches

Function
--------



The **display isis debug-switches** command displays IS-IS debugging status.




Format
------

**display isis debug-switches** [ *process-id* ]

**display isis** *process-id* **debug-switches**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Displays IS-IS debugging status of in a specified IS-IS process.  By default, IS-IS debugging status of all IS-IS processes is displayed. | The value is an integer that ranges from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view IS-IS debugging status, run the display isis debug-switches command.If no IS-IS process is enabled or IS-IS debugging is not enabled, the output of the display isis debug-switches command is null.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IS-IS debugging status.
```
<HUAWEI> display isis debug-switches 1
ISIS-1 SPF-EVENTS related debugging switch is on
ISIS-1 SPF-PRC debugging switch is on

```

**Table 1** Description of the **display isis debug-switches** command output
| Item | Description |
| --- | --- |
| ISIS-1 SPF-EVENTS related debugging switch is on | SPF-EVENTS debugging of IS-IS 1 is enabled. |
| ISIS-1 SPF-PRC debugging switch is on | SPF-PRC debugging of IS-IS 1 is enabled. |