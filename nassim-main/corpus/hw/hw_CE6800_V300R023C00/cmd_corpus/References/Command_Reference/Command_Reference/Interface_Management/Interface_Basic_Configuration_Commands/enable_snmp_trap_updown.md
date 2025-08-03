enable snmp trap updown
=======================

enable snmp trap updown

Function
--------



The **enable snmp trap updown** command enables an interface to send a trap message to the NMS when the protocol status of the interface changes.

The **undo enable snmp trap updown** command disables an interface from sending a trap message to the NMS when the protocol status of the interface changes.



By default, an interface sends a trap message to the NMS when the protocol status of the interface changes.


Format
------

**enable snmp trap updown**

**undo enable snmp trap updown**


Parameters
----------

None

Views
-----

100GE Layer 2 sub-interface view,Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,200GE Layer 2 sub-interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE Layer 2 sub-interface view,400GE-L2 view,400GE interface view,50GE Layer 2 sub-interface view,Layer 2 50GE interface view,50GE interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 Eth-Trunk interface view,Eth-Trunk interface view,Layer 2 GE interface view,Tunnel interface view,Layer 2 sub-interface view,Sub-interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable an interface to send a trap message to the NMS when the protocol status of the interface changes, run the enable snmp trap updown command. The command output helps the NMS monitor the interface status.

**Configuration Impact**

The function of sending a trap message to the NMS when the protocol status of the interface changes is enabled by default. If an interface alternates between Up and Down, it will frequently send trap messages to the NMS, causing the NMS to be busy processing these trap messages. In this case, run the undo enable snmp trap updown command to disable the interface from sending trap messages to the NMS.


Example
-------

# Disable an interface from sending a trap message to the NMS when the protocol status of the interface changes.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo enable snmp trap updown

```