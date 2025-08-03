dhcp server option121
=====================

dhcp server option121

Function
--------

The **dhcp server option121** command configures a classless static route allocated by a DHCP server to a client.

The **undo dhcp server option121** command deletes a classless static route allocated by a DHCP server to a client.

By default, the classless static route allocated to a client is not configured.



Format
------

**dhcp server option121 ip-address** { *ip-address* *mask-length* *gateway-address* } &<1-8>

**undo dhcp server option121** [ **ip-address** *ip-address* *mask-length* *gateway-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** *ip-address* | Indicate destination IP addresses. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of a destination address. | The value is an integer ranging from 0 to 32. |
| *gateway-address* | Specifies a gateway address. | The value is in dotted decimal notation. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The **dhcp server option121 ip-address** command applies to only the DHCP server. The **dhcp server option121 ip-address** command configures Option 121 that defines a classless static route allocated to a client from an interface address pool.

The mask-length gateway-address parameter is used to specify a classless static route. The
**dhcp server option121 ip-address** command configures a maximum of eight classless static routes.

**Prerequisites**

1. The address of an interface address pool has been configured using the **ip address** command.
2. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

* To configure multiple classless static routes, run the **dhcp server option121 ip-address** command repeatedly.
* The **undo dhcp server option121** command will delete all classless static routes. To delete one classless static route, run the undo **dhcp server option121 ip-address** command.


Example
-------

# Configure a classless static route allocated by a DHCP server to a client in the interface address pool on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.2 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server option121 ip-address 10.10.10.10 24 192.168.11.11

```