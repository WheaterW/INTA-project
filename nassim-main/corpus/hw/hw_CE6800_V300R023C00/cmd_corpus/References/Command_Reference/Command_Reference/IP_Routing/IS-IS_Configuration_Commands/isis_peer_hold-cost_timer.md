isis peer hold-cost timer
=========================

isis peer hold-cost timer

Function
--------



The **isis peer hold-cost timer** command sets the period during which IS-IS keeps the specified cost in local LSPs.

The **undo isis peer hold-cost** command restores the default setting.



By default, after a neighbor relationship is established, IS-IS does not retain the specified cost and hold time in local LSPs.


Format
------

**isis peer hold-cost** *cost-val* **timer** *timer-val*

**undo isis peer hold-cost** [ *cost-val* **timer** *timer-val* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **timer** *timer-val* | Specifies the interval for holding the cost. | The value is an integer ranging from 100 to 1000000, in milliseconds. |
| **hold-cost** *cost-val* | Specifies the hold cost. | The value is an integer ranging from 1 to 16777214. |



Views
-----

100ge sub-interface view,100GE interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When an IS-IS interface changes from down to up, the IS-IS neighbor relationship is re-established. After IGP route convergence is completed, traffic is switched back to the recovered link. As IGP routes converge fast, many services that depend on IGP routes may require a delayed switchback. After the **isis peer hold-cost** command is run, the IS-IS LSP on the local device retains the specified cost for a period of time. In this manner, traffic is forwarded along the original path. After the hold-cost timer expires, the cost is restored to the normal value, and traffic is switched back normally.For P2P neighbors and broadcast neighbors, the time for starting the hold-cost timer is as follows:

* For a P2P neighbor, the hold-cost timer is started after the neighbor goes Up.
* After a broadcast neighbor goes Up, a DIS is elected. After the DIS is elected successfully, the hold-cost timer is started.

Example
-------

# Set the period during which IS-IS keeps the cost value 22 in local LSPs to 100000 ms.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] isis enable
[*HUAWEI-100GE1/0/1] isis peer hold-cost 22 timer 100000

```