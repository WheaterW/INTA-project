m-lag ip address
================

m-lag ip address

Function
--------



The **m-lag ip address** command configures an IPv4 address dedicated for OSPF/BGP over M-LAG.

The **undo m-lag ip address** command deletes an IPv4 address dedicated for OSPF/BGP over M-LAG.



By default, the M-LAG IP address is not configured.


Format
------

**m-lag ip address** *ip-address* { *mask-length* | *mask* }

**undo m-lag ip address** *ip-address* { *mask-length* | *mask* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mask-length* | Specifies a mask length. | The value is an integer that ranges from 1 to 32. |
| *mask* | Specifies a mask. | The value is in dotted decimal notation. |
| **address** *ip-address* | Configures an IPv4 address. | The value is in dotted decimal notation. |



Views
-----

VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **m-lag ip address** command to configure an IPv4 address dedicated for OSPF or BGP over M-LAG.

**Precautions**

1. An M-LAG IPv4 address is a secondary IP address. An interface can be configured with only one M-LAG secondary IPv4 address and a maximum of 255 secondary IP addresses.
2. An M-LAG secondary IPv4 address must be unique on the entire network, and cannot be the same as any secondary address on the local device or other devices on the network.
3. A multicast, broadcast, or loopback address cannot be configured as an M-LAG IPv4 address.
4. If an M-LAG secondary IPv4 address has been configured on an interface and a new M-LAG secondary IPv4 address is configured on the interface, the new address overwrites the original one.
5. Before running this command, you must configure a primary IP address, and the IP address specified in this command must be on the same network segment as the primary IP address.
6. If you unbind a VNI from a BD and an IP address has been configured on the corresponding VBDIF interface using the **m-lag ip address** command, the dedicated M-LAG IPv4 address on the VBDIF interface is also deleted.
7. The **m-lag ip address** command can be configured on a VBDIF interface only after a VNI is bound to the corresponding BD.
8. If the ip address ignore primary-sub enable command is configured on the device, the **m-lag ip address** command cannot be configured.
9. If an M-LAG IPv4 address configured for an interface using the **m-lag ip address** command is the same as a primary or secondary IP address on the interface, the M-LAG IPv4 address cannot be delivered.

Example
-------

# Configure an IPv4 address dedicated for OSPF/BGP over M-LAG.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI-vlan100] interface vlanif 100
[*HUAWEI-Vlanif100] ip address 10.1.0.4 255.255.255.0
[*HUAWEI-Vlanif100] m-lag ip address 10.1.0.1 255.255.255.0

```