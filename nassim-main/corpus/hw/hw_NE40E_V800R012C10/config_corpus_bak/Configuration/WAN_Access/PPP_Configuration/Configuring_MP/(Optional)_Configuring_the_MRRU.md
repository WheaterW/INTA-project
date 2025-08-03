(Optional) Configuring the MRRU
===============================

The maximum receive reconstructed unit (MRRU) defines the maximum size (in bytes) of each packet a device can receive without fragmenting the packet. The MRRU is negotiated by two ends on a Multilink Point-to-Point Protocol (MP) link. A local end sends packets or fragments with the maximum size equal to the negotiated MRRU to its peer. Upon receipt, the peer can accept the packets or reassemble fragments into packets.

#### Context

The interface MRRU, which is used in Link Control Protocol (LCP) negotiation, is closely related to the interface maximum transmission unit (MTU):

* If the MRRU of the peer MP-Group interface is greater than or equal to the MTU of the local MP-Group interface, the local MP-Group interface keeps its own MTU unchanged during LCP negotiation.
* If the MRRU of the peer MP-Group interface is less than the MTU of the local MP-Group interface, the local MP-Group interface uses the MRRU of the peer MP-Group interface as its own MTU during LCP negotiation.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface mp-group**](cmdqueryname=interface+mp-group) *number*
   
   
   
   An MP-Group interface is created, and the MP-Group interface view is displayed.
3. Run [**mrru**](cmdqueryname=mrru) *mrru*
   
   
   
   The MRRU of the MP-Group interface is configured.
4. Restart the MP-Group interface.
   1. Run [**shutdown**](cmdqueryname=shutdown)
      
      
      
      The interface is shut down.
   2. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   3. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
      
      
      
      The interface is restarted.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), and [**undo shutdown**](cmdqueryname=undo+shutdown) commands must be run in sequence so that the preceding configuration can take effect after the interface is restarted.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.