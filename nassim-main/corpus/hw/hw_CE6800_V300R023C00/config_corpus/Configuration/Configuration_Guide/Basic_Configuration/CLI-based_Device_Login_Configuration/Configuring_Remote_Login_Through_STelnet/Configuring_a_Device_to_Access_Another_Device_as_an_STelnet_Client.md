Configuring a Device to Access Another Device as an STelnet Client
==================================================================

Configuring a Device to Access Another Device as an STelnet Client

#### Prerequisites

Before configuring a device to access another device as an STelnet client, you have completed the following tasks:

* Log in to the device from a terminal.
* Ensure that there are reachable routes between the device and the STelnet server.
* Enable the STelnet server function on the STelnet server.
* Obtain the SSH user name, password, and port number configured on the STelnet server.

![](public_sys-resources/note_3.0-en-us.png) 

SSHv2 is more secure than SSHv1, and is therefore recommended for STelnet login.



#### Procedure

1. **Configure the mode for connecting the device (SSH client) to the SSH server for the first time.**
   
   
   
   For details, see [Configuring the Mode for Connecting a Device to the SSH Server for the First Time](galaxy_ssh_cfg_0014.html) in Configuration Guide > Security Configuration.
2. **Set SSH client parameters.**
   
   
   
   For details, see [Setting SSH Client Parameters](galaxy_ssh_cfg_0015.html) in Configuration Guide > Security Configuration.
3. **Log in to another device using STelnet.**
   
   
   
   **Table 1** Logging in to another device using STelnet (normal Layer 3 network connection)
   | Operation | Command | Description |
   | --- | --- | --- |
   | Log in to the SSH server through an IPv4 address using STelnet. | [**stelnet**](cmdqueryname=stelnet)[ **-a***source-ip-address* | **-i***interface-type* *interface-number* ] [ **-force-receive-pubkey** ] *host-ip-address* [ *server-port* ] [ [ **prefer\_kex***prefer\_kex* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress zlib** ] | [ **prefer\_stoc\_compress zlib** ] | [ **-vpn-instance***vpn-instance-name* ] | [ **-ki***interval* ] | [ **-kc***count* ] | [ **identity-key***identity-key-type* ] | [ **user-identity-key***user-key* ] ] \* | * Run either command depending on the network address type. * The STelnet client can connect to the server successfully with no port number specified only when the server is listening on port 22. If the server is listening on another port, the port number must be specified upon login. * When connecting to the SSH server, the STelnet client can carry the source IP address, VPN instance name, a key exchange algorithm, an encryption algorithm, a compression algorithm, and an HMAC algorithm, and be configured with the keepalive function. * If the source interface is specified using **-i** *interface-type interface-number*, the **public-net** and **-vpn-instance** *vpn-instance-name* parameters are not supported. |
   | Log in to the SSH server through an IPv6 address using STelnet. | [**stelnet ipv6**](cmdqueryname=stelnet+ipv6)[ **-a** *source-ipv6-address* ] [ **-force-receive-pubkey** ] *host-ipv6-address* [ [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] | [ *server-port* ] | [ **prefer\_kex** *prefer\_kex* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress zlib** ] | [ **prefer\_stoc\_compress zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key***identity-key-type* ] | [ **user-identity-key***user-key* ] ] \* |

#### Verifying the Configuration

* Run the [**display ssh server-info**](cmdqueryname=display+ssh+server-info) command on the SSH client to check the mappings between all SSH servers and public keys on the SSH client.
* Run the [**display ssh client**](cmdqueryname=display+ssh+client) **session** command on the SSH client to check the number of transmitted and received packets for online sessions, data volume of the transmitted and received packets, and STelnet login duration after key renegotiation.