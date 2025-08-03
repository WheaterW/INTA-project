(Optional) Setting the Lower Limit for an IP-Trunk Interface's Bandwidth
========================================================================

This section describes how to set the lower limit for an
IP-Trunk interface's bandwidth. An IP-Trunk interface goes Down when
the sum of all Up member interfaces' bandwidth is lower than the lower
limit. An IP-Trunk interface goes Up when the sum of all Up member
interfaces' bandwidth reaches the lower limit.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface ip-trunk**](cmdqueryname=interface+ip-trunk) *trunk-id*
   
   
   
   The IP-Trunk interface
   view is displayed.
3. Run [**least active-bandwidth**](cmdqueryname=least+active-bandwidth) *bandwidth*
   
   
   
   The lower limit is set for an IP-Trunk interface's bandwidth.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command is mutually exclusive with the [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number* command. Check that the [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number* command configuration does not exist before running this command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.