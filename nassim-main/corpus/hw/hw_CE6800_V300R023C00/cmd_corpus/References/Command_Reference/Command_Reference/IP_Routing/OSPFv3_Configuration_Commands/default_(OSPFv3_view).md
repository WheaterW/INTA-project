default (OSPFv3 view)
=====================

default (OSPFv3 view)

Function
--------



The **default** command sets the default cost of the external routes that are imported by OSPFv3.

The **undo default** command restores the default value.



By default, the default cost of the external routes is 1; the type of the imported external routes is Type 2; the default tag value is 1.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**default** { **cost** *costvalue* | **tag** *tagvalue* | **type** *typevalue* } \*

**undo default** { **cost** [ *costvalue* ] | **tag** [ *tagvalue* ] | **type** [ *typevalue* ] } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cost** *costvalue* | Specifies the default cost of the external route that is imported by OSPFv3.   * The cost of a Type 1 external route equals the cost of the route from the Router to the related ASBR plus the cost of the route from the ASBR to the destination. * The cost of a Type 2 external route equals the cost of the route from the ASBR to the destination. | The value ranges from 0 to 16777214. |
| **tag** *tagvalue* | Specifies the tag of the imported VPN routes. | The value is an integer ranging from 0 to 4294967295. |
| **type** *typevalue* | Specifies the type of the external routes. | The value is 1 or 2.   * 1: Type 1 external route * 2: Type 2 external route |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Since OSPFv3 can import external routing information and advertise it to the entire AS, it is necessary to specify the default cost of the external route that is imported by the protocol.If multiple OSPFv3 processes are started, the command is valid only for this process.

**Precautions**

You can run the following commands to set the cost of imported routes. The priorities of imported routes are in descending order.

* Run the **apply cost** command to set the route cost.
* Run the import-route (OSPFv3) command to set the cost of the imported route.
* Run the default (OSPFv3) command to set the default cost of imported routes.The **default tag** command takes effect only for the OSPF process on the public network or the OSPFv3 VPN process for which the **vpn-instance-capability simple** command is run. If the **vpn-instance-capability simple** command is not run for an OSPFv3 VPN process, the tag value configured using the **route-tag** command takes effect.

Example
-------

# Specify the default cost of the external routes that are imported by OSPFv3 as 10.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] default cost 10

```