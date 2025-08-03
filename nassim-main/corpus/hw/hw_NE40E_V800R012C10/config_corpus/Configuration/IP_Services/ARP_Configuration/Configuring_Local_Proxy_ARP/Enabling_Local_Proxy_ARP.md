Enabling Local Proxy ARP
========================

To allow isolated devices in a BD to communicate, enable the local proxy ARP function.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface vbdif**](cmdqueryname=interface+vbdif) *bd-id*
   
   
   
   The VBDIF interface view is displayed.
3. Run [**arp-proxy local enable**](cmdqueryname=arp-proxy+local+enable)
   
   
   
   Local proxy ARP is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After local proxy ARP is enabled, all the users in the BD can communicate. To allow only specific users in a BD to intercommunicate, running the [**undo
   split-horizon enable**](cmdqueryname=undo+split-horizon+enable) command on these member interfaces that need intercommunicate to disable split horizon is recommended.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.