(Optional) Binding an E-Trunk to BFD
====================================

If the master device in an E-Trunk fails, to ensure that the backup device promptly detects the failure and takes over traffic, bind the E-Trunk to a Bidirectional Forwarding Detection (BFD) session for fast failure detection.

#### Context

A BFD session can be bound to an E-Trunk in either of the following modes:

* Manually create a BFD session and bind it to an E-Trunk.
  
  1. Manually create a BFD session, which is also called a static BFD session. The type of the BFD session must be BFD for IP.
  2. Manually bind the BFD session to an E-Trunk.
* Enable a device to automatically create a BFD session and bind the session to an E-Trunk.
  
  After a device is enabled to create a dynamic BFD session, the device automatically creates a BFD session and binds it to an E-Trunk.


#### Procedure

* Manually create a BFD session and bind it to an E-Trunk.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
     
     The E-Trunk view is displayed.
  3. Run [**e-trunk track bfd-session**](cmdqueryname=e-trunk+track+bfd-session) **session-name** *bfd-session-name*
     
     A BFD session is bound to the E-Trunk.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable a device to automatically create a BFD session and bind the session to an E-Trunk.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
     
     The E-Trunk view is displayed.
  3. Run [**e-trunk bfd enable**](cmdqueryname=e-trunk+bfd+enable) [ **track** **interface** { *interface-name* | *interface-type interface-number* } ]
     
     The device is enabled to create a dynamic BFD session. The device automatically creates a BFD session and binds it to an E-Trunk.
     
     For example, an E-Trunk is deployed on PE1 and PE2. To enable a dynamic BFD session to rapidly detect the changes in the user-side interface on a PE, run the [**e-trunk bfd enable**](cmdqueryname=e-trunk+bfd+enable) **track** **interface** *interface-type interface-number* command to associate the dynamic BFD session with the interface.
  4. (Optional) Run [**e-trunk bfd**](cmdqueryname=e-trunk+bfd) { **detect-multiplier** *multiplier* | **min-rx-interval** *mintx* | **min-tx-interval** *imintx* }\*
     
     The local detection multiplier, minimum interval between receiving BFD packets, and minimum interval between sending BFD packets are set for the dynamic BFD session.
     
     You can set proper BFD session parameters as required.
     
     If a device does not receive BFD packets from its peer within a specified detection period, the device considers the link faulty and sets the BFD session to down. To reduce system resource consumption, the device automatically changes the local receive interval to a random value greater than 1000 ms after detecting that the BFD session goes down. When the BFD session goes up again, the device restores the configured receive interval.
     
     + Interval between sending BFD packets = max (Local minimum interval between sending BFD packets, Peer minimum interval between receiving BFD packets)
     + Interval between receiving BFD packets = max (Peer minimum interval between sending BFD packets, Local minimum interval between receiving BFD packets)
     + Detection period = Peer detection multiplier x max (Peer minimum interval between sending BFD packets, Local minimum interval between receiving BFD packets)
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.