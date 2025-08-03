(Optional) Configuring HDLC Link Status Monitoring
==================================================

The HDLC link status can be effectively monitored by configuring the HDLC link status monitoring function.

#### Context

The parameters for HDLC link status monitoring are as follows:

* **Keepalive time**
  
  + **Keepalive count**
    
    If a device does not receive a Keepalive message from its peer within a specified polling interval, the Keepalive count increases by 1. If the device still fails to receive a Keepalive message from its peer after a specified Keepalive count is reached, the device considers the link connecting to the peer device to be faulty and sets the HDLC link to Down.
  
  The Keepalive time equals the polling interval multiplied by the Keepalive count. In situations with unfavorable network delay or significant congestion, a short Keepalive time may cause network flapping. Conversely, a long Keepalive time would lead to slow link detection. Therefore, make sure that the Keepalive time is appropriate and fits the network situations.
* **IP-Trunk member link monitoring**
  
  An IP-Trunk link is established between two devices, and multiple transmission devices may be deployed on the link to transparently transmit data. If a link connecting a POS interface of the IP-Trunk is faulty, the POS interface sets its HDLC status to Down. If the loopback detection function is enabled on the transmission devices, loopback messages will cause the HDLC status of the POS interface to become Up. As a result, IP-Trunk traffic will continue to be distributed to the faulty POS interface and gets discarded, causing service interruption. To prevent IP-Trunk traffic from being discarded, you can enable IP-Trunk member link monitoring so that when a POS interface detects a loopback message, the POS interface sets its HDLC status to Down.

#### Procedure

* Configure a polling interval.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed
  3. Run [**timer hold**](cmdqueryname=timer+hold) *interval*
     
     
     
     A polling interval is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The polling intervals on two interconnected devices must be set to the same value (other than 0s). If both polling intervals are set to 0s, the link detection function is disabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure IP-Trunk member link monitoring.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**down-when-looped**](cmdqueryname=down-when-looped)
     
     
     
     IP-Trunk member link monitoring is enabled on a specific POS interface. When the POS interface detects a loopback message, the POS interface sets its HDLC status to Down.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.