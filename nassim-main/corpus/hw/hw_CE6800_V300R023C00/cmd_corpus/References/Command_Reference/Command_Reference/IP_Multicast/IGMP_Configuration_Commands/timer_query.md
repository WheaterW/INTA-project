timer query
===========

timer query

Function
--------



The **timer query** command sets a global interval for sending IGMP general query messages.

The **undo timer query** command restores the default value.



By default, the interval for sending IGMP general query messages is 60 seconds.


Format
------

**timer query** *interval*

**undo timer query**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval for sending IGMP general query messages. | The value is an integer ranging from 1 to 18000, in seconds. |



Views
-----

IGMP view,VPN instance IGMP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The function of this command is the same as the function of the **igmp timer query** command used in the interface view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.


Example
-------

# In the IGMP view, set the interval for sending IGMP general query messages to 125 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] igmp
[*HUAWEI-igmp] timer query 125

```