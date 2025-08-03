virtual-channel
===============

virtual-channel

Function
--------



The **virtual-channel** command configures a ring auto protection switching protocol data unit (R-APS PDU) transmission mode for a sub-ring.

The **undo virtual-channel enable** command restores the default configuration.



By default, R-APS PDUs on sub-rings are transmitted in non-virtual channel (NVC) mode.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**virtual-channel** { **disable** | **enable** }

**undo virtual-channel** { **disable** | **enable** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | Disables the VC mode for R-APS PDU transmission on a sub-ring, which means the NVC mode is used. | - |
| **enable** | Enables the VC mode for R-APS PDU transmission on a sub-ring. | - |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

* To specify whether to use VCs or NVCs to transmit R-APS PDUs on sub-rings, run the **virtual-channel** command.
* ERPSv2 supports single and multi-ring topologies.
* In multi-ring topologies, sub-rings either have VCs or NVCs to transmit R-APS PDUs.
* With VCs: R-APS PDUs on sub-rings are transmitted to the major ring through interconnection nodes. The ring protection link (RPL) owner port of a sub-ring blocks both R-APS PDUs and data traffic.
* With NVCs: R-APS PDUs on sub-rings are terminated on the interconnection nodes. The RPL owner port blocks data traffic but not R-APS PDUs on each sub-ring.

Example
-------

# Configure the sub-ring ERPS ring 5 to use VCs to transmit R-APS PDUs.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 5
[*HUAWEI-erps-ring5] version v2
[*HUAWEI-erps-ring5] sub-ring
[*HUAWEI-erps-ring5] virtual-channel enable

```