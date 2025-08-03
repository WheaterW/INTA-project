Configuring a Multicast MAC Address for Layer 2 Protocol Tunneling
==================================================================

Configuring a Multicast MAC Address for Layer 2 Protocol Tunneling

#### Context

The device can replace the original multicast MAC address of Layer 2 protocol packets from user networks with a specified multicast MAC address to allow the packets to be transparently transmitted between user networks and prevent the packets from being processed by devices on an ISP network.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to replace the destination multicast MAC address of Layer 2 protocol packets with a specified multicast MAC address.
   
   
   ```
   [l2protocol-tunnel](cmdqueryname=l2protocol-tunnel) protocol group-mac { group-mac | default-group-mac }
   ```
   
   Most Layer 2 protocols can be distinguished by protocol type. The group MAC addresses of these Layer 2 protocols can be configured to be the same. You can specify the **default-group-mac** parameter to set the default group MAC address to the fixed value of 0100-0ccd-cdd0, reducing the configuration workload and the possibility of configuration errors.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The destination MAC addresses of STP and GMRP packets cannot be replaced with the same multicast MAC address.
   
   The destination MAC addresses of EOAM3ah and LACP packets cannot be replaced with the same multicast MAC address.
   
   When configuring Layer 2 protocol tunneling, do not use the following multicast MAC addresses to replace the destination MAC addresses of Layer 2 protocol packets:
   * Destination MAC addresses of BPDUs: 0180-C200-0000 to 0180-C200-002F
   * MAC addresses of Smart Link packets: 010F-E200-0004
   * Special multicast MAC addresses: 0100-0CCC-CCCC and 0100-0CCC-CCCD
   * Common multicast MAC addresses that have been used on the device
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```