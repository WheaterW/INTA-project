dhcp relay release
==================

dhcp relay release

Function
--------



The **dhcp relay release** command configures a DHCP relay agent to send a release message to a DHCP server for releasing the IP address assigned to a DHCP client.




Format
------

**dhcp relay release** *client-ip-address* *mac-address* [ **vpn-instance** *vpn-instance-name* ] [ *server-ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *client-ip-address* | Specifies the IP address of a DHCP client. | The value is in dotted decimal notation. |
| *mac-address* | Specifies the MAC address of a DHCP client. | The value is in the format of H-H-H, in which H is a hexadecimal number of 1 to 4 digits. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance to which a DHCP server belongs. | The value is a string of 1 to 31 case-sensitive characters without question marks (?). \_public\_ cannot be used as the VPN instance name. If the string is enclosed in double quotation marks ("), spaces are allowed in the string. The value must be an existing VPN instance name. |
| *server-ip-address* | Specifies the IP address of a DHCP server. If this parameter is specified, a DHCP relay agent sends a release message to the specified DHCP server for releasing the IP address assigned to a DHCP client. | The value is in dotted decimal notation. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP relay agents. In some situations, for example, a user is logged out, the user's IP address is no longer used. However, the user cannot access the network, and will not send a DHCP release message to the DHCP server to release the IP address assigned by the DHCP server. Before the IP address lease expires, the DHCP server will not assign the user's IP address to another client, wasting IP addresses. In this case, you can run the dhcp relay release command to configure a DHCP relay agent to send a DHCP release message to the DHCP server. After receiving the message, the DHCP server sets the status of the IP address to idle. The DHCP server then can assign the released IP address to another client.If a DHCP server address is specified, the DHCP relay agent sends an address release request only to the specified DHCP server. If no DHCP server address is specified, the following situations occur:

* When the dhcp relay release command is run in the system view, the DHCP relay agent sends an address release request to DHCP servers on all the interfaces working in DHCP relay mode.
* When the dhcp relay release command is run in the interface view, the DHCP relay agent sends an address release request to all DHCP servers on the VLANIF interface.

**Precautions**

The dhcp relay release command only releases the IP addresses dynamically assigned by DHCP servers.When multiple DHCP relay agents are connected between the DHCP client and server, this command must be executed on the first DHCP relay agent.


Example
-------

# Configure a DHCP relay agent to send a release message to the DHCP server at 10.1.1.1 for releasing the IP address 192.168.1.1 assigned to the DHCP client whose MAC address is 00e0-fc12-3456.
```
<HUAWEI> system-view
[~HUAWEI] dhcp relay release 192.168.1.1  00e0-fc12-3456 10.1.1.1

```