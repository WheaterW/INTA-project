Configuring Transparent Transmission of DHCPv4 Packets
======================================================

You need to configure transparent transmission of DHCPv4
packets when STB users send only one DHCPv4 Discover packet after
they restart.

#### Context

When a user shuts down the STB and then restarts it immediately,
the NE40E cannot detect that the user goes offline and retains the
user entry. When receiving the DHCPv4 Discover packet that the STB
sends after restart, the NE40E forces the user to go offline and waits until the user
sends a DHCPv4 Discover packet to obtain the address through DHCPv4.

Some STBs, however, send only one DHCPv4 Discover packet after
they restart. In this case, the users cannot go online after shutting
down their STBs.

You can configure the function to transparently
transmit DHCPv4 packets to solve this problem.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp through-packet**](cmdqueryname=dhcp+through-packet)
   
   
   
   The function to transparently transmit DHCPv4 packets is
   configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.