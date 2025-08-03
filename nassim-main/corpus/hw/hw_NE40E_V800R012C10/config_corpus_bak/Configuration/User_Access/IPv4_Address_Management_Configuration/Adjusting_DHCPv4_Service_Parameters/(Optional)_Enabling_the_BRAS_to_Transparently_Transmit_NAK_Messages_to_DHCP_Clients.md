(Optional) Enabling the BRAS to Transparently Transmit NAK Messages to DHCP Clients
===================================================================================

In scenarios where IP addresses are assigned from a DHCPv4 remote address pool, if a DHCP client sends a Discover message to the DHCP server through a BRAS and the BRAS receives a NAK message from the DHCP server, the BRAS discards the NAK message by default. After the BRAS is enabled to transparently transmit NAK messages to clients, the clients can be informed of login failures if parsing of NAK messages is supported on the client terminals.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp through-nak**](cmdqueryname=dhcp+through-nak)
   
   
   
   The BRAS is enabled to transparently transmit NAK messages sent by the DHCPv4 server in response to the Offer messages to DHCP clients in DHCPv4 remote address pool scenarios.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.