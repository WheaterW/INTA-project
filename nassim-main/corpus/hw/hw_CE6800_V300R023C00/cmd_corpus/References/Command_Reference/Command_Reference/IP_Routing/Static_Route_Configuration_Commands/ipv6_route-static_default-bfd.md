ipv6 route-static default-bfd
=============================

ipv6 route-static default-bfd

Function
--------



The **ipv6 route-static default-bfd** command configures global default BFD parameters for IPv6 static routes.

The **undo ipv6 route-static default-bfd** command cancels the global default BFD parameters configured for IPv6 static routes.



By default, the minimum interval at which BFD control packets are received and sent is 1000 ms, and the detection time multiplier is 3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 route-static default-bfd** { **min-rx-interval** *min-rx-interval* | **min-tx-interval** *min-tx-interval* | **detect-multiplier** *multiplier* } \*

**undo ipv6 route-static default-bfd**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-rx-interval** *min-rx-interval* | Specifies the minimum interval at which BFD control packets are received. | The value is an integer ranging from 3 to 1000, in milliseconds. |
| **min-tx-interval** *min-tx-interval* | Specifies the minimum interval at which BFD control packets are sent. | The value is an integer ranging from 3 to 1000, in milliseconds. |
| **detect-multiplier** *multiplier* | Specifies the detection time multiplier. | The value is an integer ranging from 3 to 50. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure global default BFD parameters for IPv6 static routes, run the **ipv6 route-static default-bfd** command.

**Configuration Impact**

detect-multiplier, min-rx-interval, and min-tx-interval are independent of each other. Specifically, if the **ipv6 route-static bfd** command is used to change only one of the three BFD parameters, the other two parameters continue to use their default values.

**Precautions**

After the **ipv6 route-static default-bfd** command is run on a device, the global default BFD parameters of all IPv6 static routes bound to the BFD session on the device are modified.


Example
-------

# Set the global minimum interval at which BFD packets are received to 300 ms for IPv6 static routes.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 route-static default-bfd min-rx-interval 300

```