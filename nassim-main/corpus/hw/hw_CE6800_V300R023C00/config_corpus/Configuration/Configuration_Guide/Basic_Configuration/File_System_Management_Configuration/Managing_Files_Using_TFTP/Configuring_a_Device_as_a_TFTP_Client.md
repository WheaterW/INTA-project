Configuring a Device as a TFTP Client
=====================================

Configuring a Device as a TFTP Client

#### Prerequisites

You can configure a device as a TFTP client, through which you can log in to a TFTP server to upload and download files between the client and server.

Before configuring a device to access files on another device as a TFTP client, you have completed the following tasks:

* Ensure that there are reachable routes between the device and TFTP server.
* Obtain the IP address of the TFTP server and the directory for storing the files to be downloaded or uploaded.
* The weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.

#### Context

![](public_sys-resources/note_3.0-en-us.png) 

SFTP V2 or SCP is more secure than TFTP, and is therefore recommended.

In FIPS mode, TFTP cannot be used.

[Table 1](#EN-US_TASK_0000001512671474__file11tab01) describes the process for configuring a device to access files on another device as a TFTP client.

**Table 1** Configuring a device to access files on another device as a TFTP client
| No. | Task | Description | Remarks |
| --- | --- | --- | --- |
| 1 | [(Optional) Configure the source address for the TFTP client.](#EN-US_TASK_0000001512671474__file1101) | Configure the source interface or source IP address for the TFTP client to implement security verification. | Tasks 1 and 2 can be performed in any sequence. |
| 2 | [(Optional) Configure TFTP access control.](#EN-US_TASK_0000001512671474__file1102) | Configure TFTP access control to improve access security. |
| 3 | [Transfer files using TFTP.](#EN-US_TASK_0000001512671474__file1103) | Upload and download files. |



#### Procedure

* **(Optional) Configure the source interface or source address for the TFTP client.**
  
  
  
  The source IP address to be configured must be that of a stable interface, such as a loopback interface. This configuration makes it easier to configure ACL rules. You simply need to specify the source or destination IP address in an ACL rule as the interface IP address, thereby allowing the device to filter incoming and outgoing packets.
  
  **Table 2** (Optional) Configuring the source interface or source address for the TFTP client
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Configure the source interface or source IP address for the TFTP client. | [**tftp client source**](cmdqueryname=tftp+client+source) { **-a** *ip-address* | **-i** *interface-type* *interface-number* }  [**tftp ipv6 client source -a**](cmdqueryname=tftp+ipv6+client+source+-a) *ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ] | By default, the source IPv4 address and source IPv6 address of a TFTP client are 0.0.0.0 and 0::0, respectively. If an interface is specified, set an IP address for the interface. Otherwise, the TFTP connection fails to be set up. |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **(Optional) Configure TFTP access control.**
  
  
  
  An ACL is a list of rules that classify and filter packets according to their source address, destination address, port number, and other fields. After an ACL is applied to a routing device, the routing device determines whether to permit or deny a packet based on the ACL rules.
  
  Multiple rules can be defined in an ACL. ACL rules are classified into basic, advanced, and Layer 2 ACL rules based on rule functions.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The TFTP supports only the basic ACL whose number ranges from 2000 to 2999.
  
  ACL rule:
  + When the **permit** action is defined in an ACL rule, the local device can set up TFTP connections with devices that match the rule.
  + When the **deny** action is defined in an ACL rule, the local device cannot set up TFTP connections with devices that match the rule.
  + If packets from other devices do not match any rule in an ACL, the local device cannot set up TFTP connections with those devices.
  + If no rule is defined in an ACL, the local device can set up TFTP connections with any other devices.
  
  **Table 3** (Optional) Configuring TFTP access control
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Create an ACL and enter the ACL view. | [**acl**](cmdqueryname=acl) { [ **number** ] *acl-number* | **name** *acl-name* } | By default, no ACL is created. |
  | Configure an ACL rule. | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ **fragment-type** **fragment** | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* | **logging** ] \* | By default, no rule is configured in the basic ACL view. |
  | Exit the system view. | [**quit**](cmdqueryname=quit) | - |
  | Configure TFTP access control. | [**tftp server**](cmdqueryname=tftp+server) [ **ipv6** ] **acl** *acl-number* | - |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **Upload files to or download files from the server using TFTP commands.**
  
  
  
  **Table 4** Connecting to another device using TFTP commands
  | Operation | Command | Description |
  | --- | --- | --- |
  | Connect to the TFTP server using an IPv4 address. | [**tftp**](cmdqueryname=tftp) [ **-a** *source-ip-address* | **-i** *interface-type interface-number* ] *host-ip-address* [ **vpn-instance** *vpn-instance-name* | **public-net** ] { **get** | **put** } *source-filename* [ *destination-filename* ] | + The **get** command downloads files from the server. + The **put** command uploads files to the server. |
  | Connect to the TFTP server using an IPv6 address. | [**tftp ipv6**](cmdqueryname=tftp+ipv6) [ **-a** *source-ipv6-address* ] *tftp-server-ipv6* [ **vpn-instance** *vpn-instance-name* | **public-net** ] [ **-oi** *interface-type interface-number* ] { **get** | **put** } *source-filename* [ *destination-filename* ] |
  
  
  
  The source IP address or source interface specified in the preceding commands takes precedence over that specified in the [**tftp client source**](cmdqueryname=tftp+client+source) command. The source IP address or source interface specified in the [**tftp client source**](cmdqueryname=tftp+client+source) command applies to all TFTP connections, whereas the source IP address or source interface specified in the [**tftp**](cmdqueryname=tftp) or [**tftp ipv6**](cmdqueryname=tftp+ipv6) command applies only to the current TFTP connection.
* **Disconnect from the TFTP server.**
  
  
  
  **Table 5** Disconnecting from the TFTP server
  | Operation | Command | Description |
  | --- | --- | --- |
  | Disconnect from the TFTP server. | [**quit**](cmdqueryname=quit) | You can also run the [**bye**](cmdqueryname=bye) or [**exit**](cmdqueryname=exit) command to disconnect from the TFTP server. |

#### Verifying the Configuration

* Run the [**display tftp client**](cmdqueryname=display+tftp+client) command to check the source IP address of the TFTP client.