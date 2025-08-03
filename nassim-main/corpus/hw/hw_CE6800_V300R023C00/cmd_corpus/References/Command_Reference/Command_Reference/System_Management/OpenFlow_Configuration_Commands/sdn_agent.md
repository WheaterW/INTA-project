sdn agent
=========

sdn agent

Function
--------



The **sdn agent** command configures the device as an OpenFlow-compatible device.

The **undo sdn agent** command restores the default configuration.



By default, a device is not an OpenFlow-compatible device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**sdn agent**

**undo sdn agent**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

OpenFlow-compatible devices support OpenFlow forwarding as well as Layer 2/3 forwarding. On an SDN network, a device must be configured as an OpenFlow-compatible device before other SDN configurations are performed on the device.


Example
-------

# Configure the device as an OpenFlow-compatible device.
```
<HUAWEI> system-view
[~HUAWEI] sdn agent

```