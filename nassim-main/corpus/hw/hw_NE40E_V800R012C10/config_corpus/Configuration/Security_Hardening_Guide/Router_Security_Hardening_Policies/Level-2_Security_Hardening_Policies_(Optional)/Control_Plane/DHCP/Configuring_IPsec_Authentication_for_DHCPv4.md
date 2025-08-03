Configuring IPsec Authentication for DHCPv4
===========================================

Configuring IPsec Authentication for DHCPv4

#### Security Policy

After IPsec authentication is enabled on a DHCPv4 relay agent and server, these two devices insert the SPI of the bound IPsec SA into DHCPv4 messages and encrypt them based on the security proposal of the bound IPsec SA before sending such messages. After receiving these messages, the DHCPv4 relay agent and server perform IPsec decryption and authentication. If the decryption or authentication fails, the relay agent and server discard the messages. The relay agent and server then check whether the SPI in the messages is the same as that in the bound IPsec SA. If they are different, the relay agent and server discard the messages.


#### Attack Methods

A DHCPv4 relay agent may receive forged DHCPv4 messages from a bogus DHCPv4 server, exposing it to DoS attacks. Similarly, a DHCPv4 server may receive forged DHCPv4 messages from a bogus DHCPv4 relay agent, exposing it to DoS attacks.


#### Configuration and Maintenance Methods

Configure IPsec authentication for DHCPv4 in the system view.
```
<HUAWEI> system-view
```
```
[~HUAWEI] dhcp ipsec sa sa1
```
```
[*HUAWEI] commit
```
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before running the **dhcp ipsec** command, you must configure an IPsec SA. For details, see "IPsec Configuration."




#### Configuration and Maintenance Suggestions

Note that configuring this function affects user access.


#### Verifying the Security Hardening Result

Run the [**display dhcp relay statistics**](cmdqueryname=display+dhcp+relay+statistics) [ **interface** { *interface-type* *interface-number* | *interface-name* } ] command to check packet statistics on the DHCP relay agent.