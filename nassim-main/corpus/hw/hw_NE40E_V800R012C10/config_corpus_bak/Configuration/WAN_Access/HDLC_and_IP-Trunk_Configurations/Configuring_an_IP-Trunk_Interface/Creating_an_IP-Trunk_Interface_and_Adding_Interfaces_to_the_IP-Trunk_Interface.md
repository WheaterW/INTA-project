Creating an IP-Trunk Interface and Adding Interfaces to the IP-Trunk Interface
==============================================================================

You can create an IP-Trunk interface and add interfaces to the IP-Trunk interface.

#### Procedure

* Perform the following steps in the IP-Trunk interface view:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface ip-trunk**](cmdqueryname=interface+ip-trunk) *trunk-id*
     
     
     
     The IP-Trunk interface view is displayed.
  3. Run either of the following commands:
     
     
     + To add interfaces to the IP-Trunk interface in a batch, run:
       
       ```
       [trunkport](cmdqueryname=trunkport) PortType { beginifnum [ to endifnnum ] } &<1-16>
       ```
     + To add an interface to the IP-Trunk interface, run:
       
       ```
       [trunkport](cmdqueryname=trunkport) ifname
       ```
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps in the view of the interface to be added to an IP-Trunk interface:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface ip-trunk**](cmdqueryname=interface+ip-trunk) *trunk-id*
     
     
     
     An IP-Trunk interface is created.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface pos**](cmdqueryname=interface+pos) *interface-number*
     
     
     
     The view of the interface to be added to the IP-Trunk interface is displayed.
  5. Run [**link-protocol hdlc**](cmdqueryname=link-protocol+hdlc)
     
     
     
     The link layer protocol of the interface is set to HDLC.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     HDLC must run as a link layer protocol on each interface to be added to an IP-Trunk interface.
  6. Run [**ip-trunk**](cmdqueryname=ip-trunk) *trunk-id*
     
     
     
     The interface is added to the IP-Trunk interface.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) When configuring an IP-Trunk interface, note the following issues:
     + HDLC must run on each interface to be added to the IP-Trunk interface.
     + The interface to be added to the IP-Trunk interface has no Layer 3 features, such as the IP address, or any service configured.
     + A POS interface can be added to only one IP-Trunk interface. If the POS interface needs to be added to another IP-Trunk interface, it must be deleted from the current IP-Trunk interface before being added to another IP-Trunk interface.
     + An IP-Trunk interface cannot be added to another IP-Trunk interface.
     + POS interfaces on different interface boards can be added to the same IP-Trunk interface.
     + Do not add interfaces with different forwarding capabilities to the same IP-Trunk interface. If POS interfaces working at different rates are added to the same IP-Trunk interface, the bandwidth of the IP-Trunk interface is determined by the following factors:
       - Member interfaces selected using the hash algorithm
       - Number of Up member interfaces and bandwidth of each member interface
       
       For example, a 10 Gbit/s POS interface and a 2.5 Gbit/s POS interface are added to the same IP-Trunk interface. If both POS interfaces are Up and only the 2.5 Gbit/s POS interface is selected as the member interface using the hash algorithm, the forwarding capability of the IP-Trunk interface is 2.5 Gbit/s but not 12.5 Gbit/s.
     + If a member interface of an IP-Trunk interface is connected to the peer, the directly connected interface on the peer must also be a member interface of an IP-Trunk interface.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.