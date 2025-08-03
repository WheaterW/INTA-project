dhcp snooping disable
=====================

dhcp snooping disable

Function
--------



The **dhcp snooping disable** command disables DHCP snooping on an interface.

The **undo dhcp snooping disable** command enables DHCP snooping on an interface.



By default, if the dhcp snooping enable command is run on an interface or in a VLAN that an interface belongs to, DHCP snooping is enabled for the interface.


Format
------

**dhcp snooping disable**

**undo dhcp snooping disable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After this command is run, both DHCPv4 snooping and DHCPv6 snooping are disabled.If you run the **dhcp snooping enable** command to enable DHCP snooping in a VLAN, DHCP snooping is enabled on all interfaces in the VLAN. If you want to disable DHCP snooping on a specified interface, you cannot run the **undo dhcp snooping enable** command to disable DHCP snooping on the interface because the **dhcp snooping enable** command is not run on the interface. To solve this problem, run the **dhcp snooping disable** command to disable DHCP snooping on the interface. Users can then go online from this interface, but no dynamic DHCP binding entry is generated.

**Precautions**

· After the dhcp snooping disable command is run, DHCP snooping configurations and dynamic DHCP snooping binding entries are deleted when DHCP snooping is disabled on an interface. Running the undo dhcp snooping enable command only disables DHCP snooping, but retains the DHCP snooping configuration and dynamic DHCP snooping binding entries.· After you run the undo dhcp snooping disable command, DHCP snooping is disabled on the interface by default. To enable DHCP snooping on the interface, run the dhcp snooping enable command.


Example
-------

# Disable DHCP snooping on 100GE1/0/1 in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] dhcp snooping enable
[*HUAWEI-vlan10] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] dhcp snooping disable
Warning: DHCP snooping will be disabled on this interface. Continue? [Y/N]:y
Info: It will take a few seconds. Please wait...

```