dhcp snooping user-bind max-number
==================================

dhcp snooping user-bind max-number

Function
--------



The **dhcp snooping user-bind max-number** command sets the maximum number of DHCP snooping binding entries to be learned on an interface.

The **undo dhcp snooping user-bind max-number** command restores the default maximum number of DHCP snooping binding entries to be learned on an interface.



By default, an interface can learn a maximum of 9216 DHCP snooping binding entries.


Format
------

**dhcp snooping user-bind max-number** *max-number*

**undo dhcp snooping user-bind max-number**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-number* | Specifies the maximum number of DHCP snooping binding entries that can be learned on an interface. | The value is an integer ranging from 1 to 9216. The default value is 9216. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The command sets the maximum number of DHCP snooping binding entries (including both DHCPv4 and DHCPv6 binding entries) to be learned on an interface. If the number of DHCP snooping binding entries reaches the maximum value, subsequent users cannot access.When the number of entries in the DHCP snooping binding table on an interface reaches the maximum value set by the command, the DHCP snooping-enabled device fails to add entries to the binding table and sends a DHCP Release message to the DHCP server after receiving a DHCP ACK message.For the system view configuration, the sum of the maximum numbers of DHCP snooping binding entries that can be learned by all interfaces is the configured maximum number. For the VLAN view configuration, the maximum number of DHCP snooping binding entries that can be learned by any interface in the VLAN is the configured maximum number. If the configuration is performed in the system, VLAN, and interface views, the maximum number of DHCP snooping binding entries that can be learned by the interface is the smallest value among the three views.

**Prerequisites**

Before running this command, ensure that DHCP snooping has been enabled on the device using the dhcp snooping enable command and a VLAN has been configured if the vlan parameter needs to be delivered.


Example
-------

# Set the maximum number of DHCP users in VLAN 100 to 100.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan 100
[*HUAWEI-vlan100] dhcp snooping enable
[*HUAWEI-vlan100] dhcp snooping user-bind max-number 100

```

# Set the maximum number of DHCP users on 100GE1/0/1 to 100.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping enable
[*HUAWEI-100GE1/0/1] dhcp snooping user-bind max-number 100

```