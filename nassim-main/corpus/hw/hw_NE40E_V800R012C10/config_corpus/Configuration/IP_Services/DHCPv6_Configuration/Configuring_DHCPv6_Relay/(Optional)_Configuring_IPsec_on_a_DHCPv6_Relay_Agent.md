(Optional) Configuring IPsec on a DHCPv6 Relay Agent
====================================================

To defend against DoS attacks, configure IPsec on a DHCPv6 relay agent so that IPsec can be implemented on packets exchanged between DHCPv6 relay agents or between the DHCPv6 relay agent and DHCPv6 server.

#### Context

If an attacker pretends to be a DHCPv6 server and sends bogus DHCPv6 messages to a client, the client may suffer from DoS attacks or be incorrectly configured. To defend against DoS attacks, implement IPsec on packets exchanged between DHCPv6 relay agents or between a DHCPv6 relay agent and a DHCPv6 server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 ipsec**](cmdqueryname=dhcpv6+ipsec) **sa** *sa-name* [ **peer** *peer-ipv6-address* [ **vpn-instance** *vpn-instance* ] ]
   
   
   
   IPsec is enabled on the DHCPv6 relay agent to authenticate packets exchanged between DHCPv6 relay agents or between the DHCPv6 relay agent and DHCPv6 server.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An IPsec SA must have been configured before you run this command. For details, see IPsec Configuration.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.