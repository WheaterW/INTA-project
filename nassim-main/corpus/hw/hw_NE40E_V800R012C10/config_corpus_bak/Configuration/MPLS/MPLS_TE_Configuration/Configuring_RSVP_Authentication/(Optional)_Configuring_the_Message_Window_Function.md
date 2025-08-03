(Optional) Configuring the Message Window Function
==================================================

The message window function prevents RSVP message mis-sequence. RSVP message mis-sequence terminates RSVP authentication between neighboring nodes.

#### Context

The message window function prevents RSVP message mis-sequence.

If the window size is greater than 1, the local device stores several latest valid sequence numbers of RSVP messages from neighbors.


#### Procedure

* Configure the message window function in the interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which the MPLS TE tunnel is established is displayed.
  3. Run [**mpls rsvp-te authentication handshake**](cmdqueryname=mpls+rsvp-te+authentication+handshake)
     
     
     
     The handshake function is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The task of "Configuring an RSVP Authentication Mode" must be complete before the RSVP handshake function is configured. The handshake can only take effect after it is configured on both ends of an RSVP authentication relationship.
  4. Run [**mpls rsvp-te authentication window-size**](cmdqueryname=mpls+rsvp-te+authentication+window-size) *window-size*
     
     
     
     The message window function is configured.
     
     
     
     The value is the number of valid sequence numbers of received RSVP messages that can be stored.
     
     If RSVP is enabled on a trunk interface, only one neighbor relationship is established on the trunk interface between RSVP neighbors. This means any trunk member interface receives RSVP messages in a random order, which results in message mis-sequence. An RSVP message sliding window is configured to address this problem. If the sliding window is too small, received out-of-order RSVP messages outside the window size are discarded, which terminates the RSVP neighbor relationship.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the message window function in the MPLS RSVP-TE peer view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls rsvp-te peer**](cmdqueryname=mpls+rsvp-te+peer) *peer-addr*
     
     
     
     The MPLS RSVP-TE peer view is displayed.
     
     
     
     + If *peer-addr* is set to an interface IP address of a neighbor, not the neighbor LSR ID, the message window will only take effect on that interface of the neighbor.
     + If *peer-addr* is set to a neighbor LSR ID, the message window will take effect on all interfaces of the neighbor.
  4. Run [**mpls rsvp-te authentication handshake**](cmdqueryname=mpls+rsvp-te+authentication+handshake)
     
     
     
     The handshake function is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The task of "Configuring an RSVP Authentication Mode" must be complete before the RSVP handshake function is configured. The handshake can only take effect after it is configured on both ends of an RSVP authentication relationship.
  5. Run [**mpls rsvp-te authentication window-size**](cmdqueryname=mpls+rsvp-te+authentication+window-size) *window-size*
     
     
     
     The message window function is configured. The value is the number of valid sequence numbers of received RSVP messages that can be stored.
     
     If RSVP is enabled on a trunk interface, only one neighbor relationship is established on the trunk interface between RSVP neighbors. This means any trunk member interface receives RSVP messages in a random order, which results in message mis-sequence. An RSVP message sliding window is configured to address this problem. If the sliding window is too small, received out-of-order RSVP messages outside the window size are discarded, which terminates the RSVP neighbor relationship.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.