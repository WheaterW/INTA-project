loopback internal(Interface group view)
=======================================

loopback internal(Interface group view)

Function
--------



The **loopback internal** command configures the internal loopback detection mode on an interface.

The **undo loopback internal** command disables the internal loopback detection mode on an interface.



By default, internal loopback detection is not configured on an interface.


Format
------

**loopback internal**

**undo loopback** [ **internal** ]


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before testing some special functions such as locating an Ethernet fault, enable loopback detection on the desired Ethernet interface to check whether the interface is working properly. If no fault occurs on the Ethernet interface, the physical and protocol statuses of the interface are always up after loopback detection is enabled. If a fault occurs, the statuses remain down. After the internal loopback is configured, the test packets sent from the interface are sent back to the interface through the system.

**Follow-up Procedure**

Run the **display interface** command to check whether the current state of the interface configured with the internal loopback mode is Up. If the current state is Up, the internal forwarding function is normal. Otherwise, the internal forwarding function is faulty.

**Precautions**

* Loopback detection may cause Ethernet interfaces or links to fail to work properly. After loopback detection is complete, run the undo loopback command to disable loopback detection immediately.
* After loopback is configured on an interface, the interface needs to be removed from VLAN 1 to prevent traffic loops. You can run the undo port default vlan, undo port hybrid vlan, or **undo port trunk allow-pass vlan** command to delete the interface from VLAN 1 based on the link type of the interface.
* The loopback internal and **fec mode** commands are mutually exclusive.
* The loopback internal and **single-fiber** commands are mutually exclusive.

Example
-------

# Configure internal loopback detection on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] loopback internal

```