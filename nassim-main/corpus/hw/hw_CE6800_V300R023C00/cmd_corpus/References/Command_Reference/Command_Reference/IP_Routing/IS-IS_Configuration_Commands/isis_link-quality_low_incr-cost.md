isis link-quality low incr-cost
===============================

isis link-quality low incr-cost

Function
--------

The **isis link-quality low incr-cost** command enables an IS-IS interface to adjust the link cost when the link quality is low.

The **undo isis link-quality low incr-cost** command disables an IS-IS interface from adjusting the link cost when the link quality is low.

By default, an IS-IS interface cannot adjust the link cost based on link quality.



Format
------

**isis link-quality low incr-cost** { *cost-value* | **max-reachable** }

**isis process-id** *process-id-value* **link-quality** **low** **incr-cost** { *cost-value* | **max-reachable** }

**undo isis link-quality low incr-cost** [ { *cost-value* | **max-reachable** } ]

**undo isis process-id** *process-id-value* **link-quality** **low** **incr-cost** [ { *cost-value* | **max-reachable** } ]



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
**isis link-quality low incr-cost** command to enable the device to adjust the link cost of an IS-IS interface when its link quality is low. If the IS-IS interface detects that its link quality is low, the device increases the link cost of the interface, so that this link, which has a higher bit error rate, is not selected as the optimal link. After the link quality reverts, the device automatically restores the link cost of the IS-IS interface.

Example
-------

# Set the link cost of an interface to the maximum value when the link quality of the interface is low.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable
[*HUAWEI-100GE1/0/1] isis link-quality low incr-cost max-reachable

```