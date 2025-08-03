set flow-stat interval (interface view)
=======================================

set flow-stat interval (interface view)

Function
--------



The **set flow-stat interval** command sets the interval at which traffic statistics are collected on an interface.

The **undo set flow-stat interval** command restores the default interval.



By default, the interval for collecting traffic statistics on an interface is 300 seconds.


Format
------

**set flow-stat interval** *interval*

**undo set flow-stat interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which traffic statistics are collected on an interface. | The value is an integer ranging from 10 to 600 and must be a multiple of 10, in seconds. |



Views
-----

100GE Layer 2 sub-interface view,Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,200GE Layer 2 sub-interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE Layer 2 sub-interface view,400GE-L2 view,400GE interface view,50GE Layer 2 sub-interface view,Layer 2 50GE interface view,50GE interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 Eth-Trunk interface view,Eth-Trunk interface view,Layer 2 GE interface view,Loopback interface view,NULL interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Layer 2 sub-interface view,Sub-interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The interval configured in the interface view takes effect on the current interface but not on other interfaces.

**Precautions**

* The new interval takes effect after the original interval expires. Traffic statistics are updated in the second cycle after the new interval takes effect.
* The interval at which interface traffic statistics are collected cannot be configured on the management interface.
* The interval set in the interface view takes precedence over the interval set in the system view.


Example
-------

# Set the interval at which traffic statistics are collected on 100GE 1/0/1 to 120 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] set flow-stat interval 120

```