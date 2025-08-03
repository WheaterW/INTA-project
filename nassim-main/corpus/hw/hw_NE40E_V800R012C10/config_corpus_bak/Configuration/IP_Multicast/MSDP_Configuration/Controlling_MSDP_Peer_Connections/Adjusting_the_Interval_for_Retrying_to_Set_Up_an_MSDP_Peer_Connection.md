Adjusting the Interval for Retrying to Set Up an MSDP Peer Connection
=====================================================================

A TCP connection needs to be immediately set up between the MSDP peers when a new MSDP peer relationship is created, an ended MSDP peer connection is restarted, or a faulty MSDP peer recovers. You can flexibly adjust the interval for retrying to set up a TCP connection between MSDP peers.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MSDP view is displayed.
3. Run [**timer retry**](cmdqueryname=timer+retry) *timeRetryInterval*
   
   
   
   The interval for the Router to send a TCP connection request to the remote MSDP peer is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.