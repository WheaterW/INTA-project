Configuring the Device to Use Extended Source Ports to Send and Receive RADIUS Packets
======================================================================================

Configuring_the_Device_to_Use_Extended_Source_Ports_to_Send_and_Receive_RADIUS_Packets

#### Context

You can configure the device to use extended source ports instead of the default ports for sending and receiving RADIUS packets. This configuration also enables you to increase the number of non-retransmitted packets sent to the RADIUS server in a certain period of time.

The first half of the extended source ports are used to send and receive RADIUS authentication packets, whereas the second half of the ports are used to send and receive RADIUS accounting packets. If an odd number of ports is specified, one port more is used for sending and receiving authentication packets than for accounting packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**radius-server extended-source-ports**](cmdqueryname=radius-server+extended-source-ports) [ **start-port** *start-port-number* ] **port-number** *port-number*
   
   
   
   Extended source ports for sending and receiving RADIUS packets are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you do not specify *start-port-number* when configuring extended source ports, the system assigns a configured number of valid extended source ports.
3. Run [**radius-server extended-source-ports algorithm round-robin**](cmdqueryname=radius-server+extended-source-ports+algorithm+round-robin)
   
   
   
   The device is configured to use the round-robin algorithm to select extended source ports for sending RADIUS packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.