Configuring a Device as an SCP Client
=====================================

Configuring a Device as an SCP Client

#### Prerequisites

SCP is a utility of the SSH protocol that is used to securely copy files from one system to another. A device can be configured as an SCP client to set up a secure connection with an SCP server to upload or download files.

Before configuring a device to access files on another device as an SCP client, you have completed the following tasks:

* Ensure that there are reachable routes between the device and SSH server.
* Obtain the host name or IP address of the SSH server and SSH user information.
* Obtain the port number configured for the server if the standard port number is not used.

#### Context

[Table 1](#EN-US_TASK_0000001513030642__file14tab01) describes the process for configuring a device to access files on another device as an SCP client.

**Table 1** Configuring a device to access files on another device as an SCP client
| No. | Task | Description | Remarks |
| --- | --- | --- | --- |
| 1 | [(Optional) Configure the source interface or source IP address for the SCP client.](#EN-US_TASK_0000001513030642__step2559894175329) | Configure the source interface or source IP address for the SCP client to implement security verification. | Tasks 1, 2, and 3 can be performed in any sequence. |
| 2 | [Configure the mode for connecting a device to the SSH server for the first time.](#EN-US_TASK_0000001513030642__file1403) | You can enable first login for the SSH client or configure the SSH client to assign a public key to the SSH server. |
| 3 | [Configure SCP client parameters.](#EN-US_TASK_0000001513030642__step396319558312) | SCP client parameters include the interval for sending keepalive packets and the maximum number of keepalive packets sent by the SCP client. |
| 4 | [Connect to another device using SCP commands.](#EN-US_TASK_0000001513030642__step1324694965175329) | - |



#### Procedure

* **(Optional) Configure the source interface or source IP address for the SCP client.**
  
  
  
  **Table 2** (Optional) Configuring the source interface or source IP address for the SCP client
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Configure the source interface or source IP address for the SCP client. | [**scp client-source**](cmdqueryname=scp+client-source) { [**-a**](cmdqueryname=-a) *source-ip-address* [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | [**-i**](cmdqueryname=-i) { *interface-type* *interface-number* | *interface-name* } }  [**scp ipv6 client-source -a**](cmdqueryname=scp+ipv6+client-source+-a) *source-ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ] | By default, the source IPv4 address of an SCP client is 0.0.0.0, and the IPv6 address of an SCP client is 0::0.  To use [**-i**](cmdqueryname=-i) to specify a logical interface as the source interface, ensure that the logical interface has been created. |
  | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
* **Configure the mode for connecting a device to the SSH server for the first time.**
  
  
  
  For details, see "Configuring the Mode for Connecting a Device to the SSH Server for the First Time" in Configuration Guide > Security Configuration.
* **Configure SCP client parameters.**
  
  
  
  For details, see "Setting SSH Client Parameters" in Configuration Guide > Security Configuration.
* **Connect to another device using SCP commands.**
  
  
  
  Different from SFTP that uses separate commands for connection setup and file transfer, after the SCP connection is established, the client can directly upload files to or download files from the server.
  
  **Table 3** Connecting to another device using SCP commands
  | Operation | Command | Description |
  | --- | --- | --- |
  | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
  | Connect to the SCP server using an IPv4 address. | [**scp**](cmdqueryname=scp) [ **-a** *source-ip-address* | **-i** *interface-type* *interface-number* ] [ **-force-receive-pubkey** ] [ [ **-port** *server-port* ] | [ **public-net**  | **vpn-instance** *vpn-instance-name* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] | **-r** | **-c** | [ **-cipher** *cipher* ] | [ **-prefer-kex** *prefer-kex* ] ] \* *source-filename* *destination-filename* | Select either of the commands based on the address type.  If the source interface is specified using **-i** *interface-type* *interface-number*, the **public-net** and **vpn-instance** *vpn-instance-name* parameters are not supported. |
  | Connect to the SCP server using an IPv6 address. | [**scp ipv6**](cmdqueryname=scp+ipv6) [ [ [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* ] | **public-net** ] [ **-force-receive-pubkey** ] [ [ **-port** *server-port* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] | [ [ **-a** *source-ipv6-address* ] | [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] ] | **-r** | **-c** | [ **-cipher** *cipher* ] | [ **-prefer-kex** *prefer-kex* ] ] \* *source-filename* *destination-filename* |
* **Disconnect from the SCP server.**
  
  
  
  **Table 4** Disconnecting from the SCP server
  | Operation | Command | Description |
  | --- | --- | --- |
  | Disconnect from the SCP server. | [**quit**](cmdqueryname=quit) | You can also run the [**bye**](cmdqueryname=bye) or [**exit**](cmdqueryname=exit) command to disconnect from the SCP server. |

#### Verifying the Configuration

* Run the [**display scp client**](cmdqueryname=display+scp+client) command to check the configuration of the SCP client.
* Run the [**display ssh server-info**](cmdqueryname=display+ssh+server-info) command to check the mapping between all SSH servers and public keys on the client.