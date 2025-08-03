max-response-time
=================

max-response-time

Function
--------



The **max-response-time** command sets a global maximum response time of IGMP Query messages.

The **undo max-response-time** command restores the default value.



By default, the maximum response time for IGMP Query messages is 10 seconds.


Format
------

**max-response-time** *interval*

**undo max-response-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the maximum response time of IGMP Query messages. | The value is an integer ranging from 1 to 25, in seconds. |



Views
-----

IGMP view,VPN instance IGMP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The function of this command is the same as the function of the **igmp max-response-time** command in the interface view. The configuration in the IGMP view is globally valid, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.


Example
-------

# In the IGMP view, set the maximum response time of IGMP Query messages to 8 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] igmp
[*HUAWEI-igmp] max-response-time 8

```