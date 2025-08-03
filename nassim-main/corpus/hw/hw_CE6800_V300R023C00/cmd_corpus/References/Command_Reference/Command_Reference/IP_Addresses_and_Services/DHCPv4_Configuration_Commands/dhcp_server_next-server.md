dhcp server next-server
=======================

dhcp server next-server

Function
--------

The **dhcp server next-server** command specifies a server IP address for DHCP clients.

The **undo dhcp server next-server** command cancels the configuration.

By default, no server IP address is specified by the DHCP Server for DHCP clients.



Format
------

**dhcp server next-server** *ip-address*

**undo dhcp server next-server**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a server IP address. | The value is in dotted decimal notation. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The **dhcp server next-server** command is used on DHCP servers. When assigning a DHCP client an IP address, a DHCP server can also assign the DHCP client an IP address of the server that provides network services for the client. For example, some clients like IP phones still need other configuration parameters after automatically obtaining IP addresses. You can run the **dhcp server next-server** command to specify the server address used after a client obtains an IP address. The client then requests the configuration parameters from the specified server after obtaining an IP address.

If users use addresses in the interface address pool, run the
**dhcp server next-server** command to specify the DHCP server IP address. If users use addresses in the global address pool, run the
**next-server** command to specify the DHCP server IP address.

**Prerequisites**

1. The address of an interface address pool has been configured using the **ip address** command.
2. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

* The **dhcp server next-server** command takes effect for only users who use addresses in the interface address pool.
* If you run the **dhcp server next-server** command multiple times, only the latest configuration takes effect.


Example
-------

# Specify the server IP address 192.168.1.2 in the interface address pool on interface
100GE
1/0/1 used to provide services for terminal users.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.2 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server next-server 192.168.1.2

```