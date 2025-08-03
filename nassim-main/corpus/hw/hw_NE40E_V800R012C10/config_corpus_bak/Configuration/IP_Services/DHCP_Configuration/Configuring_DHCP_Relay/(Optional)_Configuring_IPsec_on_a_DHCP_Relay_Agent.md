(Optional) Configuring IPsec on a DHCP Relay Agent
==================================================

To defend against certain network attacks, configure IPsec to authenticate messages between a DHCP relay agent and server.

#### Context

If an attacker masquerades as a DHCP server and sends forged DHCP messages to a DHCP relay agent, the relay agent may be exposed to DoS attacks. Similarly, an attacker that masquerades as a DHCP relay agent can send forged DHCP messages to a DHCP server, exposing the server to DoS attacks. To defend against DoS attacks, configure IPsec to authenticate DHCP messages exchanged between the DHCP relay agent and server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp ipsec sa**](cmdqueryname=dhcp+ipsec+sa) *saName* [ **peer** *peerAddr* [ **vpn-instance** *vpnInstance* ] ]
   
   
   
   IPsec is enabled to authenticate messages exchanged between DHCP relay agents and between the DHCP relay agent and server.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before running this command, you must configure an IPsec SA. For details, see "IPsec Configuration."
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.