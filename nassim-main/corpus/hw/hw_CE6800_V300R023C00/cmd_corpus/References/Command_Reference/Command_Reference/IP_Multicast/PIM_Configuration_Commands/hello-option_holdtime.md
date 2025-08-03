hello-option holdtime
=====================

hello-option holdtime

Function
--------



The **hello-option holdtime** command sets the neighbor timeout period carried in PIM Hello packets to be sent by a router.

The **undo hello-option holdtime** command restores the default configuration.



By default, the neighbor timeout period carried in PIM Hello packets to be sent by a router is 105s.


Format
------

**hello-option holdtime** *holdtimeValue*

**undo hello-option holdtime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *holdtimeValue* | Specifies the neighbor timeout period carried in PIM Hello messages to be sent. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to set the neighbor timeout period carried in PIM Hello packets to be sent by a router. If the receive end does not receive any Hello packet from the local device within the timeout period, the receive end considers that the local neighbor is aged. If routers need to quickly detect PIM neighbor changes, set this parameter to a smaller value, but the value must be greater than the configured interval for sending Hello messages.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the hello-option holdtime command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, set the neighbor timeout period carried in PIM Hello packets to be sent by the router to 120 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] hello-option holdtime 120

```