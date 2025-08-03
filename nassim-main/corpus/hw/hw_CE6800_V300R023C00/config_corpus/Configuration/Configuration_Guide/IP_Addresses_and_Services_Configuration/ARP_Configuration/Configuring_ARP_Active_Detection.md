Configuring ARP Active Detection
================================

Configuring ARP Active Detection

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001176743497__fig13689206552), Host1 and Host2 reside on the same network segment and their default gateways are DeviceA and DeviceB, respectively. They both use the same IP address (192.168.1.1/24) as their default gateway addresses, and DeviceA and DeviceB both advertise routes to the corresponding network segment (192.168.1.0/24) to DeviceC. As a result, DeviceC considers that there are two equal-cost routes to both Host1 and Host2. If DeviceC chooses to transmit traffic to Host1 through DeviceB, the traffic is discarded because DeviceB does not have Host1's ARP information. To resolve this issue, enable ARP active detection on DeviceA and DeviceB so that they can actively learn ARP information of the hosts connected to them. Then, run the **arp direct-route enable** command in the system view or the **arp direct-route enable** command in the interface view on DeviceA and DeviceB to convert the learned ARP information into Vlink host routes and advertise the routes to DeviceC. In this way, DeviceC can accurately forward packets.

**Figure 1** Network diagram of ARP active detection  
![](figure/en-us_image_0000001130624060.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Configure an interval at which the device sends ARP probe messages and the number of ARP probe messages to be sent in each interval.
   
   
   ```
   [arp smart-discover interval](cmdqueryname=arp+smart-discover+interval+count) interval-value count count-value
   ```
   
   By default, the interval at which the device sends ARP probe messages and the number of ARP probe messages to be sent in each interval are 1 second and 128, respectively.
3. Enter the VLANIF interface view.
   
   
   ```
   [interface vlanif](cmdqueryname=interface+vlanif) vlan-id
   ```
4. Enable ARP active detection.
   
   
   ```
   arp smart-discover enable
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```