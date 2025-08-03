local-preference least active-linknumber
========================================

local-preference least active-linknumber

Function
--------



The **local-preference least active-linknumber** command configures the minimum number of active links for enabling preferential forwarding of local traffic on an Eth-Trunk interface.

The **undo local-preference least active-linknumber** command cancels the configuration of the minimum number of active links for enabling preferential forwarding of local traffic on an Eth-Trunk interface.



By default, the minimum number of active links for enabling preferential forwarding of local traffic is not configured for an Eth-Trunk interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K.



Format
------

**local-preference least active-linknumber** *link-number*

**undo local-preference least active-linknumber** [ *link-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *link-number* | Specifies the minimum number of active links. | The value is an integer that ranges from 1 to 64. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a device has multiple forwarding chips, you can run the **local-preference enhanced** command to enable an Eth-Trunk interface to preferentially forward traffic on the local chip. This configuration saves bandwidth between chips and improves traffic forwarding efficiency. However, if member links go Down, the bandwidth of the outbound interface is insufficient for traffic forwarding, causing traffic loss.To resolve this problem, run the **local-preference least active-linknumber linknumber** command to configure the minimum number of active links for the chip to preferentially forward traffic on the Eth-Trunk interface. When the number of active links on an Eth-Trunk interface is smaller than the value of linknumber, the system automatically disables preferential forwarding of traffic on the local chip of the Eth-Trunk interface. This ensures that bandwidth resources are fully used and bandwidth is sufficient to forward traffic on the local chip, preventing packet loss.


Example
-------

# Set the minimum number of active links for enabling preferential forwarding of traffic on an Eth-Trunk interface to 5.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 10
[~HUAWEI-Eth-Trunk10] local-preference least active-linknumber 5

```