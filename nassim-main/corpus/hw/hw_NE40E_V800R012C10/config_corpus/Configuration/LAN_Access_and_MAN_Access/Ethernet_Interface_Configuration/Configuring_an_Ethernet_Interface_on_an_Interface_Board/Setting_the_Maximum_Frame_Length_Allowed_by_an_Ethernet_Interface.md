Setting the Maximum Frame Length Allowed by an Ethernet Interface
=================================================================

Jumbo frames are designed for gigabit Ethernet networks. They are giant frames and their lengths vary according to vendors. To enable devices that transmit different lengths of jumbo frames to communicate successfully, adjust the maximum frame length allowed by either the local or peer Ethernet interface.

#### Context

An Ethernet network splits data into frames with a certain length and adds frame headers and trailers when transmitting them. If jumbo frames are used to complete file transfer, frame costs are reduced, and network resource utilization and transmission efficiency are improved.

To enable two interfaces to communicate successfully, ensure that a jumbo frame sent by an interface is not greater than that allowed by the other interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Properly plan the jumbo frame length before network deployment. A jumbo frame is discarded or processed incorrectly if its length exceeds that allowed by an interface.
* Setting the maximum frame length allowed by an Ethernet interface limits the maximum length of Ethernet Layer 2 packets, thus affecting the MTU for Layer 3 packets. If a service also has MTU requirements, plan both the MTU and maximum frame length properly.

Perform the following steps on each Router:


#### Procedure

* Set the maximum frame length allowed by an Ethernet interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
     
     
     
     The specified Ethernet interface view is displayed.
  3. Run [**jumboframe**](cmdqueryname=jumboframe) *value*
     
     
     
     The maximum frame length allowed by the Ethernet interface is set.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.