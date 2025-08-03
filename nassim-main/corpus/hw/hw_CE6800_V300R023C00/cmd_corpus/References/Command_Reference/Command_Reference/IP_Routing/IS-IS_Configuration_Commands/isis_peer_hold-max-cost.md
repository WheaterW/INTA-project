isis peer hold-max-cost
=======================

isis peer hold-max-cost

Function
--------



The **isis peer hold-max-cost** command sets the maximum holdtime for the largest IS-IS route cost in local Link State PDUs (LSPs).

The **undo isis peer hold-max-cost** command restores the default configuration.



By default, no maximum holdtime is set for the largest IS-IS route cost in local LSPs.


Format
------

**isis peer hold-max-cost timer** *timer-val*

**isis process-id** *process-id* **peer** **hold-max-cost** **timer** *timer-val*

**undo isis peer hold-max-cost timer** [ *timer-val* ]

**undo isis process-id** *process-id* **peer** **hold-max-cost** **timer** [ *timer-val* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **process-id** *process-id* | Specifies the ID of an IS-IS process, which is used in multi-instance process scenarios. | The value is an integer ranging from 1 to 4294967295. |
| **timer** *timer-val* | Sets the maximum holdtime for the largest IS-IS route cost in local LSPs. | The value is an integer ranging from 100 to 1000000, in milliseconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a Down IS-IS interface goes Up, IS-IS neighbor relationships are re-established on the interface, and traffic is switched back to this Up interface after IGP route convergence. IGP route convergence is fast, but many services that depend on IGP routes may not expect such fast traffic switchback. To delay traffic switchback after IGP route convergence, run the **isis peer hold-max-cost** command to set the maximum holdtime for the largest IS-IS route cost (16777214 in wide mode and 63 in narrow mode) in local LSPs. In this manner, before the specified maximum holdtime expires, traffic is not switched back to this route due to its large cost. After the specified maximum holdtime expires, the route cost reverts to the original value, and then traffic is switched back to this route.The effective time of the specified maximum holdtime is different for P2P and broadcast neighbors.

* For a P2P neighbor, the maximum holdtime takes effect after the neighbor relationship goes Up.
* For a broadcast neighbor, the maximum holdtime takes effect after the neighbor relationship goes Up and then a DIS is elected successfully.

Example
-------

# Set the maximum holdtime to 1000 ms for the largest IS-IS route cost in local LSPs on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis peer hold-max-cost timer 1000

```