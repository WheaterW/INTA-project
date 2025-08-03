(Optional) Configuring IPsec Authentication for the DHCPv6 Server
=================================================================

To defend against certain network attacks, configure IPsec to authenticate messages between a DHCPv6 relay agent and server.

#### Context

An attacker may initiate an attack on the DHCPv6 server by masquerading as a DHCPv6 client and sending forged DHCPv6 messages to the server. To defend against such attacks, configure IPsec authentication for DHCPv6 messages exchanged between the DHCPv6 relay agent and server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 ipsec**](cmdqueryname=dhcpv6+ipsec) **sa** *sa-name* [ **peer** *peer-ipv6-address* [ **vpn-instance** *vpn-instance* ] ]
   
   
   
   IPsec authentication is enabled for messages exchanged between DHCPv6 relay agents and between the DHCPv6 relay agent and server.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before running this command, you must configure an IPsec SA. For details, see "IPsec Configuration."
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.