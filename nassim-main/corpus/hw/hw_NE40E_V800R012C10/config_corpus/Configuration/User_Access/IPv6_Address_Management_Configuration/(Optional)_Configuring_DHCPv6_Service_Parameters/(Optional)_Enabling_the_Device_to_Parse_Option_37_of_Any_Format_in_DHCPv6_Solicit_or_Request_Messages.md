(Optional) Enabling the Device to Parse Option 37 of Any Format in DHCPv6 Solicit or Request Messages
=====================================================================================================

The device can be enabled to parse Option 37 of any format
in DHCPv6 Solicit or Request messages.

#### Context

In DHCPv6 scenarios, Layer 2 relay agents insert Option
37 to the relay header of Relay-forward messages. When the NE40E receives the Relay-forward messages, the NE40E can parse Option 37. However, if Layer 2 relay agents
insert Option 37 to DHCPv6 Solicit or Request messages instead of
the relay header of Relay-forward messages, the NE40E can parse Option 37 only if it is 10 or 16 bytes in length.
In this case, configure the NE40E to parse Option 37 of any format in DHCPv6 Solicit or
Request messages.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 option-37 any-format decode enable**](cmdqueryname=dhcpv6+option-37+any-format+decode+enable)
   
   
   
   The NE40E is enabled to parse Option 37 of any format in DHCPv6
   Solicit or Request messages.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.