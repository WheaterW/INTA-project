server(DHCP server group view)
==============================

server(DHCP server group view)

Function
--------



The **server** command adds a DHCP server to a DHCP server group.

The **undo server** command deletes a DHCP server from a DHCP server group.



By default, no DHCP server is added to a DHCP server group.


Format
------

**server** *ip-address* [ *ip-address-index* ]

**undo server** { *ip-address* | *ip-address-index* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of a DHCP server. | The value is in dotted decimal notation. |
| *ip-address-index* | Specifies the index of an IP address. When configuring the IP address of the DHCP server, you can specify the index of the IP address. If you do not specify the server index, the system allocates an idle index to the server. To delete a DHCP server address, you can specify the IP address or address index. When the index of an IP address is specified, if the index has been allocated to another IP address, the configuration fails to be issued and a message is displayed indicating that the index has been allocated. If an IP address has been assigned an index, you can specify another index. If no index is specified, the system automatically assigns an idle index to overwrite the original index. | The value is an integer ranging from 0 to 19. |



Views
-----

DHCP server group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To load-balance traffic and improve network reliability, run the server command to add multiple DHCP servers to a DHCP server group.The VPN instance bound to a DHCP server group on the DHCP relay agent must be the same as the VPN instance bound to the IP address pool on the DHCP server.


Example
-------

# Add a DHCP server with the IP address 10.10.78.56 to a DHCP server group named dhcp-srv1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp relay server group dhcp-srv1
[*HUAWEI-dhcp-relay-server-group-dhcp-srv1] server 10.10.78.56

```