(Optional) Configuring the Method of Sending Trap Messages from an IP-Trunk Member Interface
============================================================================================

You can configure an IP-Trunk member interface to send
trap messages through a private MIB.

#### Context

Perform the following steps on the devices where IP-Trunk
interfaces are created:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**trunk-member trap in private-mib enable**](cmdqueryname=trunk-member+trap+in+private-mib+enable)
   
   
   
   An IP-Trunk member interface in the Up or Down
   state sends trap messages through the private MIB.
   
   The trap message sent through the public MIB does not carry information
   about the IP-Trunk interface. If you want the trap message sent by
   an IP-Trunk member interface to carry information about the IP-Trunk
   interface, run the [**trunk-member trap in
   private-mib enable**](cmdqueryname=trunk-member+trap+in+private-mib+enable) command.