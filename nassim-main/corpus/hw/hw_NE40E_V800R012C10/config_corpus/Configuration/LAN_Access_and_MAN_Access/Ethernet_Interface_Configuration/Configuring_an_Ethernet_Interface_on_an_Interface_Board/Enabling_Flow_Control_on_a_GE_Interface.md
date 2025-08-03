Enabling Flow Control on a GE Interface
=======================================

To prevent traffic congestion between a local device and its peer device, configure flow control on GE interfaces of both devices to control the rates at which the GE interfaces send and receive packets.

#### Context

Perform the following steps on target Routers:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
   
   
   
   The specified Ethernet interface view is displayed.
3. Run [**flow control**](cmdqueryname=flow+control) [ **receive** | **send** ]
   
   
   
   Flow control is enabled on a GE interface.
   
   
   
   After flow control is enabled on a GE interface, if the rate at which the peer interface sends traffic reaches the set threshold, such as 1 Gbit/s, the interface sends a Pause frame to instruct the peer interface to send traffic at a lower rate. If the peer interface also supports flow control, it sends data at a lower rate after receiving the Pause frame. This allows the local interface to process received frames properly. If the peer interface does not support flow control, it will not send data at a lower rate after receiving the Pause frame.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.