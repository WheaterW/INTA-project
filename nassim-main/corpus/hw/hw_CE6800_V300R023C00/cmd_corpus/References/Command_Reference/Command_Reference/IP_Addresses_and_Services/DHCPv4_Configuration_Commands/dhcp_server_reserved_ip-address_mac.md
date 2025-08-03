dhcp server reserved ip-address mac
===================================

dhcp server reserved ip-address mac

Function
--------

The **dhcp server reserved ip-address mac** command enables the function of reserving IP address allocation records.

The **undo dhcp server reserved ip-address mac** command disables the function of reserving IP address allocation records.

By default, a device reserves IP address allocation records.



Format
------

**dhcp server reserved ip-address mac**

**undo dhcp server reserved ip-address mac**



Parameters
----------

None


Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

After a user goes offline, the IP address is reclaimed. The status of the IP address then is set to Idle and the device does not reserve allocation records of the IP address. When the user attempts to go online again, the user wants to use the original IP address. However, the device does not reserve any allocation record of the IP address and the original IP address may have been allocated to another user.

To resolve this issue, you can enable the function of reserving IP address allocation records. If a user goes offline after this function is enabled, the status of the IP address is set to Expired and the device reserves allocation records of the IP address based on the user's MAC address. If the user attempts to go online again, the device preferentially allocates the original IP address to the user.

**Prerequisites**

1. IP addresses in the interface address pool have been configured using the **ip address** command.
2. The DHCP server function of the interface address pool has been enabled on interfaces using the **dhcp select interface** command.


Example
-------

# Enable the function of reserving IP address allocation records in the interface address pool on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server reserved ip-address mac

```