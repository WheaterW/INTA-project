snmp-agent protocol get-bulk timeout
====================================

snmp-agent protocol get-bulk timeout

Function
--------



The **snmp-agent protocol get-bulk timeout** command configures a get-bulk operation timeout period.

The **undo snmp-agent protocol get-bulk timeout** command restores the default get-bulk operation timeout period.



The default get-bulk operation timeout period is 2 seconds.


Format
------

**snmp-agent protocol get-bulk timeout** *time*

**undo snmp-agent protocol get-bulk timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time* | Specifies a get-bulk operation timeout period. | The value is an integer ranging from 0 to 600, in seconds. The default value is 2.  The value 0 indicates that a get-bulk operation never expires. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

A get-bulk operation allows an NMS to query information about multiple managed devices at a time, equaling multiple get-next operations.If an NMS requests many data through a get-bulk operation, a long time is required to obtain the data. You can run the **snmp-agent protocol get-bulk timeout** command to change the get-bulk operation timeout period.

**Precautions**

You are not advised to change the get-bulk operation timeout period. The default get-bulk operation timeout period is recommended. To reconfigure a get-bulk operation timeout period, you must ensure that the configured period is less than an NMS's timeout period.


Example
-------

# Set the get-bulk operation timeout period to 10 seconds.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent protocol get-bulk timeout 10

```