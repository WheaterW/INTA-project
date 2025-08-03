Configuring an Interface to Send Testing Packets
================================================

Testing packets are Ethernet packets that are used together with remote loopback to test the packet loss ratio of a link. Perform the following steps on the device on which an interface in active mode resides:

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**test-packet start**](cmdqueryname=test-packet+start) **interface** *interface-type interface-number* [ **-c** *count* | **-p** *speed* | **-s** *size* ] \*
   
   
   
   The specified interface is configured to send testing packets.
   
   
   
   The outbound interface of testing packets must be the interface connecting the tested link.
   
   When testing packets are being sent, parameters cannot be modified.
   
   To stop sending testing packets, press **Ctrl+C**.