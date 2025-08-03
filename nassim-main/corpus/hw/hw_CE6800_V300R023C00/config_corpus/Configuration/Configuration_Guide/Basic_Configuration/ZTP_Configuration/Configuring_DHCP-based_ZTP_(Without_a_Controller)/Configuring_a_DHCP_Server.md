Configuring a DHCP Server
=========================

Configuring a DHCP Server

#### Context

The DHCP server uses Option parameters to carry network configuration parameters that are required for ZTP. The device can function as a DHCP server. If the device to be deployed and DHCP server are on different network segments, configure a DHCP relay agent to forward DHCP packets exchanged between them.

The device sends a DHCP Discover message that carries DHCP Option parameters when the DHCP discover phase starts. [Table 1](#EN-US_TASK_0000001563754729__table1153892244716) describes the DHCP Option parameters.

[Table 2](#EN-US_TASK_0000001563754729__table13809745134517) describes the DHCPv4 Option parameters.

[Table 3](#EN-US_TASK_0000001563754729__table186467222167) describes the DHCP Option parameters required in SZTP.

![](public_sys-resources/caution_3.0-en-us.png) 

* The DHCP server does not support authentication and may be spoofed. You are advised to use a trusted DHCP server for deployment on a secure network.

* DHCP uses a non-encrypted transmission protocol, so the user name and password of the SFTP file server carried in DHCP Option 66 and Option 67 have security risks. You are advised to use this protocol on a secure network.

**Table 1** DHCPv4 Option parameters in a request
| Option | Function | Example |
| --- | --- | --- |
| Option 60 | Vendor ID, which indicates the vendor and model of a device. | "HUAWEI CE6866-48S8CQ-P" |
| Option 61 | Client ID, which indicates the ESN and MAC address of a device. | "2102354LMB0123456517 00e0-fc12-3456" |


**Table 2** DHCPv4 Option parameters for intermediate file-based ZTP
| Option | Mandatory or Not | Function |
| --- | --- | --- |
| Option 1 | Yes | Specifies the subnet mask of the IP address. |
| Option 3 | Yes | Specifies the egress gateway of the DHCP client. |
| Option 6 | No | Specifies the IP address of the DNS server.  A DNS server is required if a domain name (for example, www.ztp.com) is specified as the host name of the intermediate file server. If an IP address is specified as the host name of the intermediate file server, no DNS server is required. |
| Option 7 | No | Specifies the IPv4 address of the Syslog server. |
| Option 66 | No | Specifies the host name of the intermediate file server. The following file servers are supported:  * The address format of an SFTP server is sftp://*username*:*password*@*hostname*:*port*. * The address format of an HTTP server is http://*hostname*:*port*. * The address format of a TFTP server is tftp://*hostname*. * The address format of an FTP server is ftp://*username*:*password*@*hostname*:*port*.  In this format, *port* is optional and *hostname* can be set to a domain name or an IP address. If *hostname* is set to a domain name, a DNS server is required.  NOTE:   * The configured server URL cannot contain forward slashes (/) or number signs (#). * The domain name of the SFTP, HTTP, TFTP, or FTP server is in the standard URL format. * SFTP is recommended because it is more secure than TFTP, FTP, and HTTP. |
| Option 150 | No | Specifies the host name of the intermediate file server.  This field can be set to the IP address of the TFTP server only. The value format is *hostname*, for example, 10.1.1.1.  NOTE:  If both Option 66 and Option 150 are configured, the Option 66 field is preferentially parsed. |
| Option 67 | Yes | Specifies the name of the intermediate file.  The value format is *path*/*filename*, whereby:   * *path* may or may not contain the host name of the intermediate file server. For example, the value can be **/script/ztp\_script.py** without a host name, or **sftp://sftp\_user:Hyx\_Hy1234@10.1.3.2/ztp\_script.py** with a host name. If the path without a host name is used, you must set Option 66. If the server type is TFTP server, you can also set Option 150. * *filename* can be **ztp\*\*\*.ini** or **ztp\*\*\*.py**, and has a maximum length of 64 characters.   NOTE:  The configured intermediate file name cannot contain forward slashes (/) or number signs (#). |
| Option 148 | No | Specifies the Syslog port number.  The value format is *syslog\_port*.   * *syslog\_port*: port number for sending Syslogs.   NOTE:  If the Syslog port number corresponding to the Syslog IP address specified by Option 7 is invalid, port 514 is used by default, and the ZTP process is not terminated. |


**Table 3** DHCP Option parameters for SZTP
| Option | Mandatory or Not | Function |
| --- | --- | --- |
| Option 1 | Yes | Specifies the subnet mask of the IP address. |
| Option 3 | Yes | Specifies the egress gateway of the DHCP client. |
| Option 6 | No | Specifies the IP address of the DNS server.  A DNS server is required if a domain name (for example, www.ztp.com) is specified as the host name of the intermediate file server. If an IP address is specified as the host name of the intermediate file server, no DNS server is required. |
| Option 7 | No | Specifies the IP address of the Syslog server. |
| Option 143 | Yes | Specifies the bootstrap server address list.  NOTE:  This field must be configured using the [**option**](cmdqueryname=option) **143** **hex** *sub-hex-string* command. |



#### Procedure

1. Configure the DHCP server.
2. (Optional) Configure the DHCP relay agent.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If a Huawei device is used as the DHCP relay agent, see "DHCPv4 Configuration" in Configuration Guide > IP Address and Service Configuration.
   
   If a third-party device is used as the DHCP relay agent, see the operation guide of the third-party DHCP server and DHCP relay agent.