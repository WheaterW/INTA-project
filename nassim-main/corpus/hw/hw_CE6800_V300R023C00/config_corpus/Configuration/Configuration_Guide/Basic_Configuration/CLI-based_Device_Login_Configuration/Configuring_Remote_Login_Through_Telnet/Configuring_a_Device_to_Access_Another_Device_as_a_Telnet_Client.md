Configuring a Device to Access Another Device as a Telnet Client
================================================================

Configuring a Device to Access Another Device as a Telnet Client

#### Prerequisites

Before configuring a device to access another device as a Telnet client, you have completed the following tasks:

* Log in to the device from a terminal.
* Ensure that there are reachable routes between the device and the Telnet server.
* Enable the Telnet server function on the Telnet server.
* Obtain the Telnet user name, password, and port number configured on the Telnet server.
* The weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.

#### Context

![](public_sys-resources/note_3.0-en-us.png) 

* STelnet is more secure than Telnet, and is therefore recommended.
* In FIPS mode, Telnet cannot be used.

[Table 1](#EN-US_TASK_0000001564133137__login11tab01_dc) describes the tasks involved in configuring a device to access another device as a Telnet client.

**Table 1** Tasks involved in configuring a device to access another device as a Telnet client
| No. | Task | Description | Remarks |
| --- | --- | --- | --- |
| 1 | [(Optional) Configure Telnet client parameters.](#EN-US_TASK_0000001564133137__login1101_dc) | Configure the source address and differentiated services code point (DSCP) priority of the Telnet client. | - |
| 2 | [Log in to another device using Telnet.](#EN-US_TASK_0000001564133137__login1102_dc) | Access the Telnet server using Telnet. |



#### Procedure

1. **(Optional) Configure Telnet client parameters.**
   
   **Table 2** (Optional) Configuring Telnet client parameters
   | Operation | Command | Description |
   | --- | --- | --- |
   | Enter the system view. | [**system-view**](cmdqueryname=system-view) | - |
   | Configure the source address of the Telnet client. | [**telnet client source**](cmdqueryname=telnet+client+source) { **-a** *source-ip-address* | **-i** *interface-type* *interface-number* }  [**telnet ipv6 client source**](cmdqueryname=telnet+ipv6+client+source) **-a** *source-ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ] | By default, the source IPv4 address of a Telnet client is 0.0.0.0, and source IPv6 address of a Telnet client is ::.  The source address of the Telnet client displayed on the server is the same as that configured in this step. |
   | Configure the DSCP priority of Telnet packets. | [**telnet client dscp**](cmdqueryname=telnet+client+dscp) *value* | By default, the DSCP priority of Telnet packets is 48. |
   | Return to the user view. | [**quit**](cmdqueryname=quit) | - |
   | Commit the configuration. | [**commit**](cmdqueryname=commit) | - |
2. **Log in to another device using Telnet.**
   
   **Table 3** Logging in to another device using Telnet (normal Layer 3 network connection)
   | Operation | Command | Description |
   | --- | --- | --- |
   | Telnet to the server using an IPv4 address. | [**telnet**](cmdqueryname=telnet) [ **-i** { *interface-type* *interface-number* | *interface-name* } | [ **vpn-instance** *vpn-instance-name* ] [ **-a** *source-ip-address* ] ] *host-ip-address* [ *port-number* ] | Run either command depending on the network address type.  The Telnet client can connect to the server successfully without a specified port number only when the server is listening on port 23. If the server is listening on another port, the port number must be specified upon login. |
   | Telnet to the server using an IPv6 address. | [**telnet**](cmdqueryname=telnet) **ipv6** [ **-a** *source-ipv6-address* ] [ **public-net** | **vpn-instance** *ipv6-vpn-name* ] *ipv6-address* [ **-oi** { *interface-type interface-number* | *interface-name* } ] [ *port-number* ] |

#### Verifying the Configuration

Run the [**display tcp status**](cmdqueryname=display+tcp+status) command to check all TCP connections.