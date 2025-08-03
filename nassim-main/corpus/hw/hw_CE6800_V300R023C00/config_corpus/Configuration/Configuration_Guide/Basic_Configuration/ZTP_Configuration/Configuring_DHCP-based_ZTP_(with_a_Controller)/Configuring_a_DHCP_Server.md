Configuring a DHCP Server
=========================

Configuring a DHCP Server

#### Context

The DHCP server uses Option parameters to carry network configuration parameters that are required for ZTP. The device can function as a DHCP server. If a controller is deployed, you can enable the built-in DHCP function of iMaster NCE-Fabric or deploy an independent DHCP server.

The device sends a DHCP Discover message that carries DHCP Option parameters when the DHCP discover phase starts. [Table 1](#EN-US_TASK_0000001513034418__table1153892244716) describes the DHCP Option parameters.

[Table 2](#EN-US_TASK_0000001513034418__table13809745134517) describes the DHCPv4 Option parameters.

If the device to be deployed and DHCP server are on different network segments, configure a DHCP relay agent to forward DHCP packets exchanged between them.

![](public_sys-resources/caution_3.0-en-us.png) 

* The DHCP server does not support authentication and may be spoofed. You are advised to use a trusted DHCP server for deployment on a secure network.
* DHCP uses a non-encrypted transmission protocol, so the user name and password of the SFTP file server carried in DHCP Option 66 and Option 67 have security risks. You are advised to use this protocol on a secure network.

**Table 1** DHCPv4 Option parameters in a request
| Option | Function | Example |
| --- | --- | --- |
| Option 60 | Vendor ID, which indicates the vendor and model of a device. | "HUAWEI CE6866-48S8CQ-P" |
| Option 61 | Client ID, which indicates the ESN and MAC address of a device. | "2102354LMB0123456517 00e0-fc12-3456" |


**Table 2** DHCPv4 Option parameters
| Option | Mandatory or Not | Function |
| --- | --- | --- |
| Option 1 | Yes | Specifies the subnet mask of the IP address. |
| Option 3 | Yes | Specifies the egress gateway of the DHCP client. |
| Option 6 | No | Specifies the IP address of the DNS server.  A DNS server is required if a domain name (for example, www.ztp.com), instead of an IP address, is specified as the host name of the bootstrap server. |
| Option 7 | No | Specifies the IPv4 address of the Syslog server. |
| Option 43 (suboption 5) | No | Specifies the IP address and port number of the bootstrap server, from which the device can download a CA certificate.  The value format is as follows: bootstrap-domain=https://*ip-address-or-hostname*:*port*;bootstrap-trust=*xxx*;bootstrap-voucher=*xxx*.   * **bootstrap-domain**: specifies the IPv4 address or domain name and port number of the bootstrap server. *port* is optional, and its default value is **443**. * **bootstrap-trust**: indicates whether to trust the downloaded CA certificate. The value can be **true** or **false**. The value **true** indicates that the device trusts the CA certificate and will verify the signature of the CA certificate only when the CA certificate sent by the bootstrap server is signed. The value **false** indicates that the device does not trust the CA certificate and will always verify the signature of the CA certificate. If **bootstrap-trust** is not specified, the default value **false** is used. * **bootstrap-voucher**: specifies the CA certificate verification mode. The value can be **DOMAIN\_IP** or **ESN**. The value **DOMAIN\_IP** indicates that the IP address is used to verify the validity of the certificate, and the value **ESN** indicates that the device ESN is used to verify the validity of the certificate. The CA certificate can be obtained only after being successfully verified.   NOTE:  The ESN of the device cannot contain spaces. |
| Option 66 | No | Specifies the host name of the file server (where the Python script containing controller information is located). This field applies to the scenario where an independent DHCP server is deployed. The following file servers are supported:  * The address format of an SFTP server is sftp://*username*:*password*@*hostname*:*port*. * The address format of an HTTP server is http://*hostname*:*port*. * The address format of a TFTP server is tftp://*hostname*. * The address format of an FTP server is ftp://*username*:*password*@*hostname*:*port*.  In this format, *port* is optional and *hostname* can be set to a domain name or an IP address. If *hostname* is set to a domain name, a DNS server is required.  NOTE:   * The configured server URL cannot contain forward slashes (/) or number signs (#). * The domain name of the SFTP server, TFTP server, FTP server, or HTTP server is in the standard URL format. * You are advised to use an SFTP or HTTPS server as the file server for security purposes. |
| Option 150 | No | Specifies the host name of the file server (where the Python script containing controller information is located). This field applies to the scenario where an independent DHCP server is deployed.  This field can be set to the IP address of the TFTP server only. The value format is *hostname*, for example, 10.1.1.1.  NOTE:  If both Option 66 and Option 150 are configured, the Option 66 field is preferentially parsed. |
| Option 67 | No | Specifies the python script that contains the controller information. This field is used when a DHCP server is independently deployed. The value format is *path*/*filename*. In the format:   * *path* may or may not contain the host name of the intermediate file server. For example, the value can be **/script/ztp\_script.py** without a host name, or **sftp://sftp\_user:Hyx\_Hy1234@10.1.3.2/ztp\_script.py** with a host name. If a relative path is used, you need to set Option 66. If the server type is TFTP server, you can also set Option 150. * *filename* is a string of at most 64 characters and must be in format of **ztp\*\*\*.py**. |
| Option 148 | Yes | This field is used when the DHCP server function is built in iMaster NCE-Fabric. After the DHCP server function is enabled on iMaster NCE-Fabric, devices can register with iMaster NCE-Fabric and the Syslog port can be set. The value format is *user\_name:**ac\_ip:**ac\_port:**syslog\_port* or *user\_name:**ac\_ip:**ac\_port*.  * *user\_name*: user name of iMaster NCE-Fabric, which does not need to be set on iMaster NCE-Fabric. * *ac\_ip*: IP address of the iMaster NCE-Fabric server, which does not need to be set on iMaster NCE-Fabric. * *ac\_port*: port number of the iMaster NCE-Fabric server, which does not need to be set on iMaster NCE-Fabric. * *syslog\_port*: port number for sending Syslogs, which needs to be configured on iMaster NCE-Fabric only when the device needs to upload Syslogs. |



#### Procedure

1. Configure the DHCP server.
2. (Optional) Configure the DHCP relay agent.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If a Huawei device is used as the DHCP relay agent, see "DHCPv4 Configuration" in Configuration Guide > IP Address and Service Configuration.
   
   If a third-party device is used as the DHCP relay agent, see the operation guide of the third-party DHCP server and DHCP relay agent.