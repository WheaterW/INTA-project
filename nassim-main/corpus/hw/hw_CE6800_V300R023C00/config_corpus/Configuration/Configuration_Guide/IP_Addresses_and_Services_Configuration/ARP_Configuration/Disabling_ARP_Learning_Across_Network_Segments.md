Disabling ARP Learning Across Network Segments
==============================================

Disabling ARP Learning Across Network Segments

#### Context

You can choose to enable or disable ARP learning across network segments based on service access and network security requirements.

On the network shown in [Figure 1](#EN-US_TASK_0000001130624042__fig172472619584), DeviceA and DeviceC reside on different network segments. To allow them to communicate, enable routed proxy ARP on DeviceB.

1. DeviceA sends an ARP request message for the MAC address of DeviceC.
2. Upon receipt of the ARP request message, DeviceB finds that the route destined for the IP address 10.2.2.1 is reachable, which meets the requirement for routed proxy. Then, DeviceB replies with an ARP reply message in which the source IP address is 10.2.2.1 and the source MAC address is 2â2â2 (the MAC address of DeviceB's interface that receives the ARP request message).
3. Upon receipt of the ARP reply message, DeviceA learns the MAC address without checking the validity of the source IP address in the message, and then sends DeviceC a datagram with the destination MAC address of 2â2â2. In this manner, DeviceA and DeviceC communicate through DeviceB.

**Figure 1** ARP learning across network segments  
![](figure/en-us_image_0000001130783854.png)

By default, ARP learning across network segments is disabled on logical interfaces and sub-interfaces of a device, but enabled on its main physical interfaces, allowing the device to access other devices on different network segments through routed proxy ARP. This, however, may pose the device to risks. For example, if an attacker on the same network segment sends a large number of ARP request messages with a false source IP address, ARP entry resources of the device may be used up. To resolve this issue, disable ARP learning across network segments on the main physical interfaces. The device will then check the source IP address of an ARP message received on a physical interface. If the source IP address is on a different network segment, the device does not learn the corresponding ARP entry, protecting the device against attacks.

You can choose to disable ARP learning across network segments on main physical interfaces based on service access and network security requirements.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable ARP learning across network segments.
   
   
   ```
   [arp learning on-different-segment disable](cmdqueryname=arp+learning+on-different-segment+disable)
   ```
   
   
   
   After this command is run, the device cannot learn the ARP entries for the IP addresses on different network segments. However, the ARP entries for the IP addresses on different network segments that have been learned before this configuration are still valid until the aging period of the ARP entries ends.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display arp**](cmdqueryname=display+arp) [ **network** *network-address* [ *network-mask* | *mask-length* ] ] [ **dynamic** | **static** ] command to check specified ARP entries.