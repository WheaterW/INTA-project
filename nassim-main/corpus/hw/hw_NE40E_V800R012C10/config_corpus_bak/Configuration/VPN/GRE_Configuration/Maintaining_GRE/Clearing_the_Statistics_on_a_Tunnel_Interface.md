Clearing the Statistics on a Tunnel Interface
=============================================

When you need to clear the statistics on a tunnel interface, you can run the **reset** commands to clear the statistics about Keepalive packets and Keepalive Response packets sent and received by a GRE tunnel interface.

#### Procedure

* Run the [**reset counters interface**](cmdqueryname=reset+counters+interface) **tunnel** [ *interface-number* ] command in the user view to clear statistics on the tunnel interface.
* Clear the statistics about Keepalive packets on the tunnel interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The tunnel interface view is displayed.
  3. Run [**reset keepalive packets count**](cmdqueryname=reset+keepalive+packets+count)
     
     
     
     The statistics about Keepalive packets are cleared on the tunnel interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**reset keepalive packets count**](cmdqueryname=reset+keepalive+packets+count) command can be run only in the tunnel interface view, and the interface tunnel protocol must be GRE.