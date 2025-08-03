(Optional) Configuring a 1588v2 Packet Encapsulation Mode
=========================================================

1588v2 packets can be encapsulated into Layer 2 or Layer 3 packets. You can configure an encapsulation mode for 1588v2 packets based on the actual network conditions, as well as the source and destination addresses and transmission priority for the 1588v2 packets.

#### Prerequisites

Before configuring a 1588v2 packet encapsulation mode, check the link type used for 1588v2 packet transmission.

* For the 1588v2 packets transmitted over a Layer 2 link, configure the MAC encapsulation mode.
* For the 1588v2 packets transmitted over a Layer 3 link, configure the UDP encapsulation mode.


#### Context

Perform the following steps on each 1588v2 device:


#### Procedure

* Configure the MAC encapsulation mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run [**ptp mac-egress**](cmdqueryname=ptp+mac-egress) { **destination-mac** *destination-mac* | **vlan** *vlan-id* [ **priority** *priority-value* ] }The MAC encapsulation mode is configured for 1588v2 packets to be sent from the interface, and a destination MAC address is configured.
     
     
     + For unicast MAC encapsulation
       
       Run this command to specify the destination MAC address for the 1588v2 packets to be sent from the interface.
       
       The configured destination MAC address must be the same as the MAC address of the peer.
     + For multicast MAC encapsulation
       
       A default multicast destination MAC address is adopted, which means that no extra configuration is required. Default multicast destination MAC addresses for different delay measurement mechanisms For details, see the following table.
       
       **Table 1** Default multicast destination MAC addresses for different delay measurement mechanisms
       | Delay Measurement Mechanism | MAC Address |
       | --- | --- |
       | Non-peer delay measurement mechanism | 01-1B-19-00-00-00 |
       | Peer delay measurement mechanism | 01-80-C2-00-00-0E |
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If no unicast destination MAC address is specified, the interface uses the multicast destination MAC address by default.
  4. Run the [**ptp mac-egress**](cmdqueryname=ptp+mac-egress) **vlan** *vlan-id* [ **priority** *priority-value* ] command to set a VLAN ID and 802.1p value for sending MAC-encapsulated 1588v2 packets.
     
     
     
     1588v2 services require a greater *priority-value* value than other services. A high transmission priority minimizes the delay or congestion impact on clock signal recovery. Using the default maximum priority value is recommended.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the UDP encapsulation mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run the [**ptp udp-egress**](cmdqueryname=ptp+udp-egress) **source-ip** *source-ip* [ **destination-ip** *destination-ip* ] command to configure the interface to use UDP to encapsulate 1588v2 packets with the specified source and destination IP addresses.
     
     
     + For UDP unicast encapsulation:
       
       Specify a destination IP address for unicast encapsulation.
     + For UDP multicast encapsulation:
       
       Multicast 1588v2 packets have a default multicast destination IP address. Therefore, the **destination-ip** *destination-ip* parameter does not need to be specified. The multicast destination IP address used by UDP encapsulation varies according to the delay measurement mechanism. For details, see the following table.
       
       **Table 2** Multicast destination IP addresses used for UDP encapsulation in different delay measurement mechanisms
       | Delay Measurement Mechanism | IP Address |
       | --- | --- |
       | Non-peer delay measurement mechanism | 224.0.1.129 |
       | Peer delay measurement mechanism | 224.0.0.107 |
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the **destination-ip** *destination-ip* parameter is not specified, the multicast IP address is used by default.
  4. Run the [**ptp udp-egress**](cmdqueryname=ptp+udp-egress) **destination-mac** *destination-mac* command to specify the next-hop MAC address of 1588v2 packets.
  5. Run the [**ptp udp-egress**](cmdqueryname=ptp+udp-egress) **source-ip** *source-ip* [ **dscp** *dscp* ] command to set a DSCP value for the UDP 1588v2 packets to be sent from the interface.
  6. Run the [**ptp udp-egress**](cmdqueryname=ptp+udp-egress) **source-ip** *source-ip* **vlan** *vlan-id* [ **priority** *priority-value* ] command to set a VLAN ID and a priority value for UDP 1588v2 packets to be sent or received by the interface.
     
     
     
     1588v2 services require a greater *dscp* value and a greater *priority* value than other services. A high transmission priority minimizes the delay or congestion impact on clock signal recovery. Using the default maximum priority value is recommended.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.