dhcp select global
==================

dhcp select global

Function
--------

The **dhcp select global** command enables an interface to use the global address pool.

The **undo dhcp select global** command disables an interface from using the global address pool.

By default, an interface is disabled from using the global address pool.



Format
------

**dhcp select global**

**undo dhcp select global**



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

The **dhcp select global** command applies to DHCP servers. After receiving a DHCP Request message from a DHCP client, a DHCP server assigns an IP address from the local address pool to the client. Run the **dhcp select global** command to configure the device to assign IP addresses from the global address pool. When no interface address pool is created for the DHCP server, the DHCP server assigns an IP address from the global address pool to an online user.

The device can also assign IP addresses from an interface address pool using the
**dhcp select interface** command in the interface view.

**Prerequisites**

1. DHCP has been enabled using the **dhcp enable** command in the system view.
2. Before running the **dhcp select global** command, you need to run the **ip address** command to configure the interface IP address.


Example
-------

# Enable
100GE
1/0/1 to use the global address pool.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select global

```