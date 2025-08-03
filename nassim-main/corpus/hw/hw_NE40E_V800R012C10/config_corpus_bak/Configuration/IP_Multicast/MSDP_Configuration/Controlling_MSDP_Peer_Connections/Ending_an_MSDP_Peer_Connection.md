Ending an MSDP Peer Connection
==============================

After the connection between MSDP peers is ended, the MSDP peers no longer exchange Source Active (SA) messages and do not retry to set up a new connection. You can reestablish the connection between MSDP peers as required.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MSDP view is displayed.
3. Run [**shutdown**](cmdqueryname=shutdown) *peer-address*
   
   
   
   The connection to the remote MSDP peer is ended.
   
   *peer-address*: specifies the IP address of a remote MSDP peer.
   
   Ending the connection does not delete the connection configurations. To reestablish the TCP connection, run the [**undo shutdown**](cmdqueryname=undo+shutdown) *peer-address* command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.