dhcp select interface
=====================

dhcp select interface

Function
--------

The **dhcp select interface** command enables an interface to use the interface address pool.

The **undo dhcp select interface** command disables an interface from using the interface address pool.

By default, the DHCP server function using the interface address pool is disabled on an interface.



Format
------

**dhcp select interface**

**undo dhcp select interface**



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

The **dhcp select interface** command applies to DHCP servers. After receiving a DHCP Request message from a DHCP client, a DHCP server assigns an IP address from the local address pool to the client. Run the **dhcp select interface** command to configure a DHCP server to assign IP addresses from the interface address pool to clients.

The device can also assign IP addresses from a global address pool using the dhcp select global command.

**Prerequisites**

1. DHCP has been enabled globally using the **dhcp enable** command in the system view.
2. An IP address has been configured for an interface using the **ip address** command. The IP addresses assigned by the address pool and configured on the interface are on the same network segment.


Example
-------

# Enable
100GE
1/0/1 to use the interface address pool.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.2 24
[*HUAWEI-100GE1/0/1] dhcp select interface

```