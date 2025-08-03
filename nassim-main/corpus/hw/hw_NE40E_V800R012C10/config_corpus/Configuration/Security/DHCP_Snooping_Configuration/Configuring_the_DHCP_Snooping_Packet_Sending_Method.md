Configuring the DHCP Snooping Packet Sending Method
===================================================

Configuring the DHCP Snooping Packet Sending Method

#### Usage Scenario

When DHCP snooping unicast packets are forwarded using CPU, the EXP values of MPLS packets sent to the tunnel side are mapped to the DSCP values (equal to the EXP values) of IP packets. After CPU forwarding is disabled for DHCP snooping unicast packets, DHCP snooping unicast packets are forwarded using hardware. The EXP values of MPLS packets sent to the tunnel side are mapped to the DSCP values (6 by default) of IP packets based on the DSCP-EXP mappings specified using the [**host-packet dscp**](cmdqueryname=host-packet+dscp) command.


#### Procedure

1. Enable DHCP snooping.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**dhcp enable**](cmdqueryname=dhcp+enable) DHCP is enabled globally.
   3. Run [**dhcp snooping enable**](cmdqueryname=dhcp+snooping+enable) DHCP snooping is enabled.
2. Configure the DHCP snooping packet sending method.
   
   
   1. Run [**dhcp snooping unicast cpu-forward disable**](cmdqueryname=dhcp+snooping+unicast+cpu-forward+disable)
      
      Hardware forwarding is configured for DHCP snooping unicast packets.
   2. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.