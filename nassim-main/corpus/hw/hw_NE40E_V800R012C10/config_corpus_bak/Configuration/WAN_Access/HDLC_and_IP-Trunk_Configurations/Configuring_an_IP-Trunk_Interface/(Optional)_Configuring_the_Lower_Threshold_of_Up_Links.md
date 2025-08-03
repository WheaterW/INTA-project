(Optional) Configuring the Lower Threshold of Up Links
======================================================

The lower threshold of Up links is the minimum number of
member interfaces in the Up state. When the number of member interfaces
in the Up state falls below the configured lower threshold, an IP-Trunk
interface goes Down. When the number of member interfaces in the Up
state reaches the configured lower threshold, the IP-Trunk interface
goes Up.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface ip-trunk**](cmdqueryname=interface+ip-trunk) *trunk-id*
   
   
   
   The IP-Trunk interface
   view is displayed.
3. Run [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number*
   
   
   
   The lower threshold of member interfaces in the Up state
   is set.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To ensure normal forwarding,
   configure the same lower threshold for the IP-Trunk interfaces on
   both ends of an IP-Trunk link.
   
   This command
   is mutually exclusive with the [**least active-bandwidth**](cmdqueryname=least+active-bandwidth) *bandwidth* command. Check that the [**least active-bandwidth**](cmdqueryname=least+active-bandwidth) *bandwidth* command configuration does not exist before running this command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.