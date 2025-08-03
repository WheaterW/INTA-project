Strict ARP Learning
===================

Strict Address Resolution Protocol (ARP) learning enabled allows the device to learn the media access control (MAC) addresses of only the ARP reply packets in response to the ARP request packets sent by itself. Therefore, this function prevents attacks caused by sending ARP request packets and ARP reply packets that are not in response to the request packets that the device itself sends.

#### Background Information

This function can be configured in the system view or interface view.

* If strict ARP learning is not configured, the device processes ARP entries as follows:
  + After receiving an ARP reply packet in response to the ARP request packet that the device itself sends, the device check whether the source IP address in the packet matches an ARP entry.
    
    - If no matching entry exists, the device creates an ARP entry using source IP and MAC addresses carried in the packet.
    - If a matching entry exists, the device updates the entry based on the source IP and MAC addresses carried in the packet.
  + After receiving an ARP request packet, the device sends an ARP reply packet and then creates an ARP entry.
* If strict ARP learning is configured, the device processes ARP packets as follows:
  + After receiving an ARP reply packet, the device checks whether the packet is in response to an ARP request packet sent by itself. If so, the device creates an ARP entry or updates the existing ARP entry based on the packet. If not, the device does not create an ARP entry or update the existing ARP entry.
  + After receiving an ARP request packet, the device sends an ARP reply packet but does not create an ARP entry or update the existing ARP entry.

#### Procedure

* Enable strict ARP learning globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**arp learning strict**](cmdqueryname=arp+learning+strict)
     
     
     
     Strict ARP learning is enabled globally.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable strict ARP learning for an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**arp learning strict force-enable**](cmdqueryname=arp+learning+strict+force-enable)
     
     
     
     Strict ARP learning is enabled for the interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  After strict ARP learning is enabled globally, strict ARP learning is enabled on all interfaces. When strict ARP learning is enabled globally:
  
  + You can run the [**arp learning strict force-disable**](cmdqueryname=arp+learning+strict+force-disable) command in the interface view to disable strict ARP learning for the specified interface.
  + You can run the [**arp learning strict trust**](cmdqueryname=arp+learning+strict+trust) command to configure the specified interface to use the global strict ARP learning configuration.