(Optional) Configuring PPP Link Status Monitoring
=================================================

The PPP link status can be effectively monitored using the PPP link status monitoring function.

#### Context

The parameters for PPP link status monitoring are as follows:

* **Keepalive time**
  
  + **Polling interval**
    
    The polling interval determines how often an interface sends a Keepalive message. When PPP is specified as the link layer protocol on the interface, the interface sends a Keepalive message to its peer device at the set polling interval. If the interface fails to receive a Keepalive message from the peer after five polling intervals, the interface considers the peer device to be faulty and sets the PPP link to Down. In situations with unfavorable network delay or significant congestion, you can increase the polling interval to reduce network flapping.
  + **Keepalive count**
    
    If a device does not receive a Keepalive message from its peer within a specified polling interval, the Keepalive count increases by 1. If the device still fails to receive a Keepalive message from its peer after a specified Keepalive count is reached, the device considers the link connecting to the peer device to be faulty and sets the PPP link to Down.
  
  The Keepalive time equals the polling interval multiplied by the Keepalive count. In situations with unfavorable network delay or significant congestion, a short Keepalive time may cause network flapping. Conversely, a long Keepalive time would lead to slow link detection. Therefore, make sure that the Keepalive time is appropriate and fits the network situations.
* **PPP magic number check**
  
  PPP magic number check is used to trigger LCP renegotiation. On a network where two devices are connected over intermediate transmission devices, if the two devices are incorrectly connected, the transmission devices will adjust the connection relationship between the two devices. However, the two devices are not aware of this adjustment because the status of their interfaces does not alternate between Down and Up. Consequently, LCP renegotiation between the two devices is not triggered. After the PPP magic number check function is enabled, when the local device finds that the magic number carried in the Echo Reply packet from the remote device is inconsistent with the one previously learned, the local device will record an error. After error statistics on an interface reach a specific threshold, the interface sets the PPP link to Down, triggering LCP renegotiation.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  This function of PPP magic number check is supported only by the NE40E-M2E, NE40E-M2F, NE40E-M2H.

#### Procedure

* Configure a polling interval.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**timer hold**](cmdqueryname=timer+hold) *interval*
     
     
     
     A polling interval is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The polling intervals on two interconnected devices must be set to the same value (other than 0s). If both polling intervals are set to 0s, the link detection function is disabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a Keepalive count.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**keepalive count**](cmdqueryname=keepalive+count) *number*
     
     
     
     A Keepalive count is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the PPP magic number check function.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ppp magic-number check**](cmdqueryname=ppp+magic-number+check)
     
     
     
     The PPP magic number check function is enabled.
     
     
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     After configuring the PPP magic number check function, to make the configuration take effect, you must run the [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), [**undo shutdown**](cmdqueryname=undo+shutdown), and [**commit**](cmdqueryname=commit) commands in sequence, or run the [**restart**](cmdqueryname=restart) and [**commit**](cmdqueryname=commit) commands.