isis ipv6 link-quality low incr-cost
====================================

isis ipv6 link-quality low incr-cost

Function
--------

The **isis ipv6 link-quality low incr-cost** command enables an IS-IS interface to adjust the link cost when the link quality is low.

The **undo isis ipv6 link-quality low incr-cost** command disables an IS-IS interface from adjusting the link cost when the link quality is low.

By default, an IS-IS interface adjusts the link cost when the link quality is low.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**isis ipv6 link-quality low incr-cost** { *cost-value* | **max-reachable** }

**isis process-id** *process-id-value* **ipv6** **link-quality** **low** **incr-cost** { *cost-value* | **max-reachable** }

**undo isis ipv6 link-quality low incr-cost** [ { *cost-value* | **max-reachable** } ]

**undo isis process-id** *process-id-value* **ipv6** **link-quality** **low** **incr-cost** [ { *cost-value* | **max-reachable** } ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cost-value* | Specifies a link cost adjustment value.  After this parameter is specified:     * When the link quality becomes low, the actual link cost of the interface equals the original link cost plus the specified adjustment value. * When the link quality reverts, the actual link cost of the interface equals the original link cost. | The value is an integer ranging from 1 to 16777213. |
| **max-reachable** | Adjusts the link cost to the maximum link cost.   * The maximum link cost is 63 if the cost type is narrow, narrow-compatible, or compatible. * The maximum link cost is 16777214 if the cost type is wide or wide-compatible. | - |
| **process-id** *process-id-value* | Specifies the IS-IS multi-instance process ID when multi-instance is enabled under the relevant process. | The value is an integer ranging from 1 to 4294967295. |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

A bit error indicates the deviation between a bit that is sent and the bit that is received. Bit errors caused by optical fiber aging or optical signal jitter are inevitable on carrier networks. During data transmission, a high bit error rate will degrade or even interrupt services in extreme cases.

To ensure network reliability, run the
**isis ipv6 link-quality low incr-cost** command to enable the device to adjust the link cost of an IS-IS interface when its link quality is low. If the IS-IS interface detects that its link quality is low, the device increases the link cost of the interface, so that this link, which has a higher bit error rate, is not selected as the optimal link. After the link quality reverts, the device automatically restores the link cost of the IS-IS interface.

**Prerequisites**

Before running this command, run the **ipv6 enable topology ipv6** command in the IS-IS process to enable the IPv6 function for the process. In the interface view, run the ipv6 enable command to enable the IPv6 function on the interface. Then, run the **isis ipv6 enable** command to enable the IS-IS function on the interface.

**Configuration Impact**

If the isis link-quality low incr-cost command is run more than once in the same view, the latest configuration overrides the previous one.



Example
-------

# Set the link cost of an interface to the maximum value when the link quality of the interface is low.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable topology ipv6
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] isis ipv6 enable 1
[*HUAWEI-100GE1/0/1] isis ipv6 link-quality low incr-cost max-reachable

```