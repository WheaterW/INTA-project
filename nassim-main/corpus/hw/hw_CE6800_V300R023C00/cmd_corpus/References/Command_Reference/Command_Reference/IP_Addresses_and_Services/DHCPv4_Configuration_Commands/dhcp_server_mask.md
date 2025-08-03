dhcp server mask
================

dhcp server mask

Function
--------

The **dhcp server mask** command sets the subnet mask of IP addresses that a DHCP server pre-allocates to DHCP clients.

The **undo dhcp server mask** command deletes the configured subnet mask.

By default, the subnet mask of IP addresses that a DHCP server pre-allocates to DHCP clients is not configured.



Format
------

**dhcp server mask** { *mask* | *masklen* }

**undo dhcp server mask**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mask* | Specifies a subnet mask. | The value is in dotted decimal notation. |
| *masklen* | Specifies the length of the subnet. | The value is an integer that ranges from 0 to 32, except values 0, 1, 31 and 32. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

After enabling the DHCP server function on an interface, you can configure the range and subnet mask of IP addresses that a DHCP server pre-allocates to DHCP clients. Run the dhcp server ip-range command to configure the IP address range and run the **dhcp server mask** command to configure the subnet mask of the IP addresses.

**Prerequisites**

The DHCP server function of the interface address pool has been enabled on interfaces using the **dhcp select interface** command.



Example
-------

# Set the subnet mask of IP addresses that a DHCP server on
100GE
1/0/1 pre-allocates to DHCP clients to 255.255.255.0.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server mask 255.255.255.0

```