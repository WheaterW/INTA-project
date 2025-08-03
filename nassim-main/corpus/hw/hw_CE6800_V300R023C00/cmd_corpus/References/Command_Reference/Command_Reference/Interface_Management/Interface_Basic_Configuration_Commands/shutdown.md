shutdown
========

shutdown

Function
--------



The **shutdown** command shuts down an interface.

The **undo shutdown** command starts an interface.



By default, physical interfaces are initialized and started after a device is powered on.


Format
------

**shutdown**

**undo shutdown**


Parameters
----------

None

Views
-----

100GE Layer 2 sub-interface view,Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,200GE Layer 2 sub-interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE Layer 2 sub-interface view,400GE-L2 view,400GE interface view,50GE Layer 2 sub-interface view,Layer 2 50GE interface view,50GE interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 Eth-Trunk interface view,Eth-Trunk interface view,Layer 2 GE interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Layer 2 sub-interface view,Sub-interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the **shutdown** command is run, the interface operating state changes to Down. If the interface is in the disabled state, run the **undo shutdown** command on the interface so that configurations on the interface can take effect, after the **undo shutdown** command is run, the interface operating state is synchronized with the link status.

**Configuration Impact**

Services on the interface are intermittently interrupted after the **shutdown** command is run on the interface.

**Precautions**

* When a physical interface of a device is idle, that is, the interface is not connected to any cable, run the **shutdown** command to disable the interface to prevent interference.
* Run the shutdown and **undo shutdown** commands with caution. The commands are useful in some special cases, for example, an interface needs to be restarted to validate the newly configured parameters.
* Some logical interfaces, such as loopback and null interfaces, do not support the **shutdown** or **undo shutdown** command.

Example
-------

# Shutdown 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] shutdown

```