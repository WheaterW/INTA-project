tunnel-protocol
===============

tunnel-protocol

Function
--------



The **tunnel-protocol** command configures the tunnel mode on a tunnel interface.

The **undo tunnel-protocol** command restores the default setting.



By default, the tunnel interface is not configured with any tunnel mode.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**tunnel-protocol** { **gre** | **none** }

**undo tunnel-protocol**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **gre** | Indicates the GRE mode. | - |
| **none** | Indicates that a tunnel interface is not configured with any tunnel mode. A tunnel in this mode is not operative. To use the tunnel interface, select another tunnel mode. | - |



Views
-----

Tunnel interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When configuring the GRE tunnel, you need to create a tunnel interface, and then use the **tunnel-protocol** command to configure the tunnel mode on the tunnel interface.



**Precautions**

Configuring, changing, or deleting the tunnel mode of a tunnel interface will delete all tunnel-related configurations on the interface, such as the MTU. Exercise caution when performing this operation.


Example
-------

# Configure the tunnel mode on Tunnel 10 as GRE.
```
<HUAWEI> system-view
[~HUAWEI] interface Tunnel 10
[*HUAWEI-Tunnel10] tunnel-protocol gre

```