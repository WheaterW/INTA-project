ospf peer hold-max-cost timer
=============================

ospf peer hold-max-cost timer

Function
--------



The **ospf peer hold-max-cost timer** command sets a period during which OSPF keeps the maximum cost in local LSAs.

The **undo ospf peer hold-max-cost timer** command restores the default configuration.



By default, no such a period is set after an OSPF neighbor relationship is established.


Format
------

**ospf peer hold-max-cost timer** *timer*

**undo ospf peer hold-max-cost timer** [ *timer* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **timer** *timer* | Specifies a period during which OSPFv3 keeps the maximum cost in local LSAs. | The value is an integer ranging from 100 to 1000000, in milliseconds. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When an OSPF interface changes from Down to Up, the OSPF neighbor relationship is re-established. When IGP route convergence ends, traffic is switched back. IGP routes converge fast. Many services that depend on IGP routes may require a delayed switchback. In this case, you can run the **ospf peer hold-max-cost** command so that OSPF keeps the maximum cost in local LSAs for a specified period after the OSPF neighbor relationship reaches Full state. During this period, the traffic forwarding path remains unchanged. After this period elapses, the original cost is restored, and traffic is switched back.


Example
-------

# Set the period during which OSPF keeps the maximum cost in local LSAs on an interface to 1000 ms.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf peer hold-max-cost timer 1000

```