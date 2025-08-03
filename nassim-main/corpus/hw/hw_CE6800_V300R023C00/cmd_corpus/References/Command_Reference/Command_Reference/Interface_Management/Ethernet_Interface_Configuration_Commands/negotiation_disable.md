negotiation disable
===================

negotiation disable

Function
--------



The **negotiation disable** command configures an interface to work in non-auto-negotiation mode.

The **undo negotiation disable** command configures an interface to work in auto-negotiation mode.



By default, the interface works in auto-negotiation mode.


Format
------

**negotiation disable**

**undo negotiation disable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The earliest Ethernet interfaces worked in 10M half-duplex mode and required mechanisms such as Carrier Sense Multiple Access (CSMA)/Collision Detection (CD) to ensure system stability. As Ethernet technology develops, Ethernet interfaces can work in 100M and 1000M full-duplex mode. This greatly improves Ethernet performance. Auto-negotiation technology allows new Ethernet to be compatible with earlier Ethernet. In auto-negotiation mode, interfaces on both ends of a link negotiate their operating parameters, including the duplex mode and rate. If the negotiation succeeds, the two interfaces work at the same operating parameters.

**Precautions**



If the **negotiation disable** command is run on an interface in Up state, the interface status changes from Up to Down and then to Up. Use this command with caution.After a copper cable is installed on an interface, the **negotiation disable** command can be run on the interface.




Example
-------

# Configure 100GE 1/0/1 to work in non-auto-negotiation mode.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] negotiation disable

```