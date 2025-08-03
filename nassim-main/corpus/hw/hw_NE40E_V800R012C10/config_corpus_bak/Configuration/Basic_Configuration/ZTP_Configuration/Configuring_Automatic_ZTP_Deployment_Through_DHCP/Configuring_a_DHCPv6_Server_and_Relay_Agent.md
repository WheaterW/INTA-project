Configuring a DHCPv6 Server and Relay Agent
===========================================

Configuring_a_DHCPv6_Server_and_Relay_Agent

#### Context

Before powering on a device that requires automatic deployment through ZTP, deploy a DHCPv6 server from which the device can obtain a device management IP address, gateway address, intermediate file server address, and intermediate file name.

In the DHCPv6 Solicit phase, the device sends to the DHCPv6 server a DHCPv6 Solicit message that carries DHCPv6 Option 6. DHCPv6 Option 6 records the option code requested by the client.

[Table 1](#EN-US_TASK_0172360189__table_01) describes the option fields that need to be configured on the DHCPv6 server.

**Table 1** Option field description
| Option | Mandatory or Optional | Function |
| --- | --- | --- |
| 5 | Mandatory | Requested IA address, IPv6 address, and lifetime. |
| 59 | Mandatory | Path of the intermediate file. The intermediate file name extension is .ini, .py, or .cfg. The format of this field is as follows:  * tftp://*hostname*/path/filename * ftp://[*username*[:*password*]@]*hostname*/path/filename * sftp://[*username*[:*password*]@]*hostname*/path/filename |



![](../../../../public_sys-resources/note_3.0-en-us.png) 

The IPv6 address lease that ZTP applies for through DHCPv6 is at least one hour and cannot be renewed.

If a ZTP-enabled device and DHCPv6 server reside on different network segments, deploy a DHCPv6 relay agent to forward DHCPv6 packets.



#### Procedure

1. Configure an address pool carrying **Option 59** on the device that functions as a DHCPv6 server.
2. Configure the address pool to assign IP addresses to access users.
3. (Optional) Configure the DHCPv6 relay agent, if deployed. For configuration details, see [Configuring DHCPv6 Relay](../vrp/dc_vrp_dhcpv6_relay_cfg_0003.html).