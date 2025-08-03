isis ipv6 prefix-attributes node-disable
========================================

isis ipv6 prefix-attributes node-disable

Function
--------



The **isis ipv6 prefix-attributes node-disable** command sets the N flag in the extended prefix attribute of the loopback interface in an IPv6 IS-IS process to 0.

The **undo isis ipv6 prefix-attributes node-disable** command restores the N flag of the extended prefix attribute of the loopback interface in an IPv6 IS-IS process to 1.



By default, the N flag in the extended prefix attribute of the loopback interface in an IPv6 IS-IS process is set to 1.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 prefix-attributes node-disable**

**isis process-id** *process-id-value* **ipv6** **prefix-attributes** **node-disable**

**undo isis ipv6 prefix-attributes node-disable**

**undo isis process-id** *process-id-value* **ipv6** **prefix-attributes** **node-disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **process-id** *process-id-value* | Specifies the ID of an IS-IS multi-instance process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

Loopback interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the 128-bit route of a loopback interface is a host route, you can run this command to control whether to set the N flag in the extended prefix attribute of the loopback interface in an IPv6 IS-IS process.

**Prerequisites**

IPv6 IS-IS has been enabled on the interface using the **isis ipv6 enable** command in the interface view.


Example
-------

# Set the N flag of the extended prefix attribute of the loopback interface in the IPv6 IS-IS process to 0.
```
<HUAWEI> system-view
[~HUAWEI] isis 100
[*HUAWEI-isis-100] ipv6 enable
[*HUAWEI-isis-100] quit
[*HUAWEI] interface LoopBack 0
[*HUAWEI-LoopBack0] ipv6 enable
[*HUAWEI-LoopBack0] isis ipv6 enable 100
[*HUAWEI-LoopBack0] isis ipv6 prefix-attributes node-disable

```