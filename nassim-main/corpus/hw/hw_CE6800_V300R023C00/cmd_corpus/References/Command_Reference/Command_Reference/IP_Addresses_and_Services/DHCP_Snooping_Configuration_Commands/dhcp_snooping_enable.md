dhcp snooping enable
====================

dhcp snooping enable

Function
--------



The **dhcp snooping enable** command enables DHCP snooping.

The **undo dhcp snooping enable** command disables DHCP snooping.



By default, DHCP snooping is disabled on the device.


Format
------

**dhcp snooping enable**

**undo dhcp snooping enable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Bridge domain view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

DHCP snooping is a security function to protect DHCP.You must enable DHCP snooping globally before enabling DHCP snooping on an interface, in a VLAN, or in a BD.

**Prerequisites**

Before enabling DHCP snooping, ensure that DHCP has been enabled globally using the **dhcp enable** command.

**Follow-up Procedure**

After DHCP snooping is enabled on an interface connected to users, in a VLAN, or in a BD, run the dhcp snooping trusted command to configure the interface connected to the DHCP server as a trusted interface. In this case, the DHCP snooping binding table can be generated.

**Precautions**

After this command is run, both DHCPv4 and DHCPv6 snooping are enabled.The **dhcp snooping enable** command in the system view enables DHCP snooping. If you run the command in the VLAN view, the command takes effect for all the DHCP messages from the specified VLAN. If you run the command in the interface view, the command takes effect for all the DHCP messages received on the specified interface.A DHCP snooping-enabled interface processes both DHCP Request and Reply messages. If the interface that receives DHCP Reply messages is enabled with DHCP snooping but not configured as a trusted interface, DHCP Reply messages are discarded.


Example
-------

# Enable DHCP snooping on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping enable

```

# Enable DHCP snooping in VLAN 100.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan 100
[*HUAWEI-vlan100] dhcp snooping enable

```