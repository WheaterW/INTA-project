dpfr enable (interface view)
============================

dpfr enable (interface view)

Function
--------



The **dpfr enable** command enables DPFR on an interface for fault detection.

The **undo dpfr enable** command disables DPFR on an interface for fault detection.



By default, DPFR is not enabled on an interface for fault detection.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dpfr enable**

**undo dpfr enable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After DPFR is enabled on an interface for fault detection, the device enables local faulty link detection, local faulty link convergence, remote faulty link notification, remote faulty link relay, and remote faulty link convergence.


Example
-------

# Enable DPFR on an interface.
```
<HUAWEI> system-view
[~HUAWEI] dpfr enable
[~HUAWEI] commit
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] dpfr enable

```