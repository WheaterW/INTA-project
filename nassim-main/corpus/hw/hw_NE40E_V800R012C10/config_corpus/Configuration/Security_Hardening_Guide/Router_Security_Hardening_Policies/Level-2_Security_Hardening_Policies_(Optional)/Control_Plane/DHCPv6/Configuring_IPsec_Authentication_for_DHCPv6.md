Configuring IPsec Authentication for DHCPv6
===========================================

Configuring IPsec Authentication for DHCPv6

#### Security Policy

After IPsec authentication is enabled on a DHCPv6 relay agent and server, these two devices insert the SPI of the bound IPsec SA into DHCPv6 messages and encrypt them based on the security proposal of the bound IPsec SA before sending such messages. After receiving these messages, the DHCPv6 relay agent and server perform IPsec decryption and authentication. If the decryption or authentication fails, the relay agent and server discard the messages. The relay agent and server then check whether the SPI in the messages is the same as that in the bound IPsec SA. If they are different, the relay agent and server discard the messages.


#### Attack Methods

A DHCPv6 relay agent may receive forged DHCPv6 messages from a bogus DHCPv6 server, exposing it to DoS attacks. Similarly, a DHCPv6 server may receive forged DHCPv6 messages from a bogus DHCPv6 relay agent, exposing it to DoS attacks.


#### Configuration and Maintenance Methods

Configure IPsec authentication for DHCPv6 in the system view.
```
<HUAWEI> system-view
```
```
[~HUAWEI] dhcpv6 ipsec sa sa1
```
```
[*HUAWEI] commit
```
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before running the **dhcpv6 ipsec** command, you must configure an IPsec SA. For details, see "IPsec Configuration."




#### Configuration and Maintenance Suggestions

Note that configuring this function affects user access.


#### Verifying the Security Hardening Result

* Run the [**display dhcpv6 relay statistics**](cmdqueryname=display+dhcpv6+relay+statistics) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] command to check packet statistics on a DHCPv6 relay agent.
* Run the [**display dhcpv6 server**](cmdqueryname=display+dhcpv6+server) { **database** | **interface** { *interface-name* | *interface-type* *interface-number* } | **statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] } command to check information about the DHCPv6 server.