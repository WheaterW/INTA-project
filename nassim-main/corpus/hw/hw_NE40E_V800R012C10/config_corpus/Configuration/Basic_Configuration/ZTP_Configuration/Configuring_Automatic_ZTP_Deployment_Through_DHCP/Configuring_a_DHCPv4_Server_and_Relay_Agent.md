Configuring a DHCPv4 Server and Relay Agent
===========================================

Configuring a DHCPv4 Server and Relay Agent

#### Context

Before powering on a device that requires automatic deployment through ZTP, deploy a DHCPv4 server from which the device can obtain a device management IP address, gateway address, intermediate file server address, and intermediate file name.

In the DHCP discover phase, the device sends to the DHCPv4 server a DHCP discover packet that carries DHCP Option 60 and Option 61. Option 60 (Vendor class identifier) records the device manufacturer and model, and Option 61 (Client-identifier) records the device ESN.

[Table 1](#EN-US_TASK_0172360188__table_01) describes the Option fields that need to be configured on the DHCPv4 server.

**Table 1** Option field description
| Option | Mandatory or Optional | Function |
| --- | --- | --- |
| 1 | Mandatory | Specifies the subnet mask of an IP address. |
| 3 | Mandatory | Specifies the egress gateway of a DHCP client. |
| 6 | Optional | Specifies the IP address of a DNS server. If a domain name (for example, www.ztp.com) is specified as the host name of an intermediate file server, deploy a DNS server to resolve the domain name to an IP address. If an IP address is specified as the host name of an intermediate file server, a DNS server does not need to be deployed. |
| 66 | Optional | Specifies the host name of the intermediate file server. An intermediate file server can be a TFTP, an FTP, or an SFTP server. The format of this field is as follows:  * tftp://*hostname* * ftp://[*username*[:*password*]@]*hostname* * sftp://[*username*[:*password*]@]*hostname*[:*port*]  *username*, *password*, and *port* are optional. *hostname* can be a domain name or an IP address. If *hostname* is set to a domain name, a DNS server needs to be deployed. The value of *port* ranges from 0 to 65535. If the specified value is out of the range, the default value 22 is used. A port number can be configured only when *hostname* of an SFTP server is set to an IPv4 address.  NOTE:  If *hostname* is set to an IP address, you do not need to set the file transfer type. The default file transfer type is TFTP. |
| 67 | Mandatory | Specifies the name of an intermediate file. The intermediate file name extension is .ini, .py, or .cfg.   * The name of an intermediate file must not exceed 64 characters. Otherwise, the file may fail to be downloaded. * The name of an intermediate file must not contain special characters, such as the ampersand (&), greater-than sign (>), less-than sign (<), double quote ("), and single quote ('). * The intermediate file name is in the format *path*/*filename*. In the format, *path* can be a relative path without the host name of the file server, **/script/ztp\_script.py** for example, or an absolute path with the host name of the file server, **sftp://10.1.1.1/script/ztp\_script.py** for example. If a path does not contain a host name, Option 66 needs to be set. |
| 150 | Optional | Specifies the IP address of a TFTP server. |



![](../../../../public_sys-resources/note_3.0-en-us.png) 

The IPv4 address lease that ZTP applies for through DHCPv4 is at least one hour and cannot be renewed.

If a ZTP device and DHCPv4 server reside on different network segments, deploy a DHCP relay agent to forward DHCP packets.

A router is used as a DHCPv4 server or relay agent example in the following procedures. If another type of device is used as the DHCPv4 server or relay agent, see the documentation of the corresponding product.


#### Procedure

1. Configure an address pool on the DHCPv4 server. For configuration details, see [Configuring an Address Pool](dc_ne_ipv4_address_cfg_0050.html). For details about configuring the options 6, 66, 67, and 150, see [(Optional) Configuring DHCPv4 User-Defined Options](dc_ne_ipv4_address_cfg_0054.html).
2. Configure the DHCPv4 server to assign addresses in the specified address pool. For configuration details, see [Example for Configuring User Address Assignment Through a Local Address Pool](dc_ne_ipv4_address_cfg_0066.html).
3. (Optional) Configure the DHCP relay agent, if deployed. For configuration details, see [Configuring DHCP Relay](../vrp/dc_vrp_dhcp_relay_cfg_0003.html).