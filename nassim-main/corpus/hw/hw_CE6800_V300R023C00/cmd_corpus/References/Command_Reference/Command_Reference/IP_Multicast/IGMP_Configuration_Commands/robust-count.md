robust-count
============

robust-count

Function
--------



The **robust-count** command sets a global robustness variable for IGMP queriers.

The **undo robust-count** command restores the default value.



By default, the global robustness variable of IGMP queriers is 2.


Format
------

**robust-count** *robust-value*

**undo robust-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *robust-value* | Specifies the robustness variable of IGMP queriers. It is the number of times for retransmitting messages to compensate for packet loss. | The value is an integer ranging from 2 to 5. |



Views
-----

IGMP view,VPN instance IGMP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A robustness variable is used to define the following values:

* Number of times for sending general query messages when the IGMP querier starts
* Number of times for sending group-specific query messages when the IGMP querier receives a Leave messageThe function of this command is the same as the function of the **igmp robust-count** command used in the interface view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.

Example
-------

# Set the robustness variable of IGMP queriers to 3 in the IGMP view.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] igmp
[*HUAWEI-igmp] robust-count 3

```