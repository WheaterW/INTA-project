(Optional) Configuring the Handshake Function
=============================================

The handshake function helps RSVP key authentication prevent replay attacks.

#### Context

If the handshake function is configured between neighbors and the lifetime is configured, the lifetime must be greater than the interval at which RSVP update messages are sent. If the lifetime is smaller than the interval at which RSVP update messages are sent, authentication relationships may be deleted because no RSVP update message is received within the lifetime. As a result, the handshake mechanism is used again when a new update message is received. An RSVP-TE tunnel may be deleted or fail to be established.


#### Procedure

* Configure the handshake function in the interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     Return to the system view.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of the interface on which the MPLS TE tunnel is established is displayed.
  3. Run [**mpls rsvp-te authentication handshake**](cmdqueryname=mpls+rsvp-te+authentication+handshake)
     
     
     
     The handshake function is enabled.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The task of "Configuring an RSVP Authentication Mode" must be complete before the RSVP handshake function is configured.
     
     The handshake function helps a device to establish an RSVP neighbor relationship with its neighbor. If a device receives RSVP messages from a neighbor, with which the device has not established an RSVP authentication relationship, the device will send Challenge messages carrying local identifier to this neighbor. After receiving the Challenge messages, the neighbor returns Response messages carrying the identifier the same as that in the Challenge messages. After receiving the Response messages, the local end checks identifier carried in the Response messages. If identifier in the Response messages is the same as the local one, the device determines to establish an RSVP authentication relationship with its neighbor.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the handshake function in the MPLS RSVP-TE peer view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls rsvp-te peer**](cmdqueryname=mpls+rsvp-te+peer) *peer-addr*
     
     
     
     The MPLS RSVP-TE neighbor view is displayed.
     
     
     
     + If *ip-address* is set to an interface IP address of a neighbor, not the neighbor LSR ID, the handshake function will only take effect on that neighbor interface.
     + If *ip-address* is set to a neighbor LSR ID, the handshake function will take effect on all interfaces of the neighbor.
  4. Run [**mpls rsvp-te authentication handshake**](cmdqueryname=mpls+rsvp-te+authentication+handshake)
     
     
     
     The handshake function is enabled.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The task of "Configuring an RSVP Authentication Mode" must be complete before the RSVP handshake function is configured. The handshake can only take effect after it is configured on both ends of an RSVP authentication relationship.
     
     The handshake function helps a device to establish an RSVP neighbor relationship with its neighbor. If a device receives RSVP messages from a neighbor, with which the device has not established an RSVP authentication relationship, the device will send Challenge messages carrying local identifier to this neighbor. After receiving the Challenge messages, the neighbor returns Response messages carrying the identifier the same as that in the Challenge messages. After receiving the Response messages, the local end checks identifier carried in the Response messages. If identifier in the Response messages is the same as the local one, the device determines to establish an RSVP authentication relationship with its neighbor.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.