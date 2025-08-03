ip route dhcp
=============

ip route dhcp

Function
--------



The **ip route dhcp** command configures a routing entry delivered by the DHCP server to a DHCP client.

The **undo ip route dhcp** command cancels the configuration.



By default, no routing entry is delivered by the DHCP server to a DHCP client.


Format
------

**ip route** *ip-address* { *mask* | *mask-length* } { *interface-type* *interface-num* | *interface-name* } **dhcp** [ *preference-value* ]

**undo ip route** *ip-address* { *mask* | *mask-length* } { *interface-type* *interface-num* | *interface-name* } **dhcp** [ *preference-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the destination IP address. | The value is in dotted decimal notation. |
| *mask* | Specifies a subnet mask of an IP address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length. A 32-bit mask is represented by consecutive 1s, and the mask in dotted decimal notation can be replaced by the mask length. | The value is an integer ranging from 0 to 32. |
| *interface-type* | Specifies the type of the interface that forwards packets. | - |
| *interface-num* | Specifies the number of the interface that forwards packets. | - |
| *interface-name* | Specifies the name of the interface that forwards packets. | - |
| **dhcp** | Indicates that the DHCP client obtains routing entries using DHCP. | - |
| *preference-value* | Specifies the priority of the routing protocol. | The value is an integer ranging from 1 to 255. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **ip route dhcp** command is used on DHCP clients. After the **ip route dhcp** command is run, a route with the gateway address as the next-hop IP address is automatically generated when a DHCP client obtains an IP address from the DHCP server through a DHCP request.


Example
-------

# Configure a routing entry to be obtained in DHCP mode on the DHCP client, and specify VLANIF100 as the outbound interface for forwarding packets and 30 as the routing protocol priority.
```
<HUAWEI> system-view
[~HUAWEI] interface vlanif 100
[*HUAWEI-Vlanif100] quit
[*HUAWEI] ip route 10.1.1.1 24 vlanif 100 dhcp 30

```