ip anti-attack source-ip equals destination-ip drop
===================================================

ip anti-attack source-ip equals destination-ip drop

Function
--------



The **ip anti-attack source-ip equals destination-ip drop** command enables the device to discard IP packets with the same source and destination IP addresses.

The **undo ip anti-attack source-ip equals destination-ip drop** command disables the device from discarding IP packets with the same source and destination IP addresses.



By default, the device does not discard IP packets with the same source and destination IP addresses.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**undo ip anti-attack source-ip equals destination-ip drop** { **all** | **slot** *slot-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Specifies all boards, including MPUs and LPUs. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Generally, IP packets with the same source and destination IP addresses can be forwarded. If you determine that the IP packets are attack packets (for example, because of heavy traffic), you can run this command to enable the device to discard the IP packets of this type.


Example
-------

# Enable the function of discarding IP packets with the same source and destination IP addresses on all boards.
```
<HUAWEI> system-view
[~HUAWEI] ip anti-attack source-ip equals destination-ip drop all

```