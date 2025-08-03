dhcp snooping enable no-user-binding
====================================

dhcp snooping enable no-user-binding

Function
--------



The **dhcp snooping enable no-user-binding** command disables an interface from generating DHCP snooping binding entries after DHCP snooping is enabled.

The **undo dhcp snooping enable no-user-binding** command restores the default setting.



By default, an interface generates DHCP snooping binding entries after DHCP snooping is enabled.


Format
------

**dhcp snooping enable no-user-binding**

**undo dhcp snooping enable no-user-binding**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After DHCP snooping is enabled on a device, the device generates DHCPv4 and DHCPv6 snooping binding entries for users by default. If the number of binding entries on the device reaches the upper limit, new users cannot go online. On a trusted DHCP network, if you do not want to limit the number of online users but want to record user location information, run the **dhcp snooping enable no-user-bind** command to disable the device from generating DHCP snooping binding entries.If the command is run in the interface view, the command takes effect for all DHCP users connected to the interface. If the command is run in the VLAN view, the command takes effect for DHCP users connected to all interfaces that belongs to the VLAN. The configuration in the system view is similar to that in the VLAN view. The difference is that the configuration in the system view takes effect for multiple VLANs.

**Prerequisites**

DHCP snooping has been enabled using the dhcp snooping enable command.

**Precautions**

After this command is executed, the device deletes the binding entries of the corresponding VLAN or interface. If the DHCP snooping binding table-dependent function, such as IPSG or DAI, is configured on the device, the corresponding function does not take effect after this command is run. This command cannot be used together with the dhcp snooping check dhcp-request enable command. Otherwise, online users cannot go offline.


Example
-------

# In the VLAN view, disable the interfaces in VLAN 10 from generating DHCP snooping binding entries.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] dhcp snooping enable
[*HUAWEI-vlan10] dhcp snooping enable no-user-binding
Warning: To execute no-user-binding will delete all dynamic binding table with the same vlan. Continue? [Y/N]:y
Info: It will take a few seconds. Please wait...

```

# In the interface view, disable 100GE1/0/1 from generating binding entries for users.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping enable
[*HUAWEI-100GE1/0/1] dhcp snooping enable no-user-binding
Warning: To execute no-user-binding will delete all dynamic binding table with the same interface. Continue? [Y/N]:y
Info: It will take a few seconds. Please wait...

```