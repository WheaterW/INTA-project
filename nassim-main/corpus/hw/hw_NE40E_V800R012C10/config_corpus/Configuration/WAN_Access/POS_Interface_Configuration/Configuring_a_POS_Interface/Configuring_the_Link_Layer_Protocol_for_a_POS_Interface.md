Configuring the Link Layer Protocol for a POS Interface
=======================================================

Configuring the Link Layer Protocol for a POS Interface

#### Context

PPP is a link layer protocol used to encapsulate and transmit network layer packets over P2P links. If a bit-oriented link layer protocol is needed for synchronous transmission and no complex services are configured, HDLC can be applied. HDLC does not require that data to be transmitted must be character sets. Instead, it can transparently transmit bit flows of all types, especially the control and response messages. Unlike PPP, HDLC uses authentication protocols to ensure the correctness and connectivity of links to be established. A cyclic redundancy check (CRC) is performed for HDLC frames and information frames are sequentially numbered to ensure reliable transmission. An IP-Trunk can consist of only POS links, and the link layer protocol running on IP-Trunk member interfaces must be HDLC.

Perform the following steps on the Routers:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface pos**](cmdqueryname=interface+pos) *interface-number*
   
   
   
   The POS interface view is displayed.
3. Run [**link-protocol**](cmdqueryname=link-protocol) { **ppp** | **fr** | **hdlc** }
   
   
   
   A link layer protocol is configured for the POS interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The supported protocol type is subject to the actual protocol type displayed on the device.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.