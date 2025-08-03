dhcp server ip-range
====================

dhcp server ip-range

Function
--------

The **dhcp server ip-range** command sets the range of IP addresses that a DHCP server pre-allocates to DHCP clients.

The **undo dhcp server ip-range** command deletes the configured IP address range.

By default, the range of IP addresses that a DHCP server pre-allocates to DHCP clients is not configured.



Format
------

**dhcp server ip-range** *start-ip-address* *end-ip-address*

**undo dhcp server ip-range**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-ip-address* | Specifies the start IP address. | The value is in dotted decimal notation. |
| *end-ip-address* | Specifies the end IP address. | The value is in dotted decimal notation. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

You can run the **dhcp server ip-range** command to change the range of IP addresses in an address pool based on actual usage of IP addresses.

**Prerequisites**

1. IP addresses in the interface address pool have been configured using the **ip address** command.
2. The DHCP server function of the interface address pool has been enabled on interfaces using the **dhcp select interface** command.


Example
-------

# Enable a DHCP server on
100GE
1/0/1 to pre-allocate IP addresses 192.168.1.2 to 192.168.1.100 to DHCP clients.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server ip-range 192.168.1.2 192.168.1.100

```