(Optional) Setting Priorities for a DHCPv6 Option
=================================================

When a DHCPv6 option is configured in multiple views, you can configure the priorities in which the DHCPv6 option takes effect.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 option-priority**](cmdqueryname=dhcpv6+option-priority) **pool** **radius** **domain**
   
   
   
   The highest, medium, and lowest priorities are configured for the DHCPv6 option configured in the address pool view, delivered by the RADIUS server, and configured in the domain view, respectively.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.