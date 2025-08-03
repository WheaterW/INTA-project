(Optional) Configuring an SMPTE-2059-2 Packet Encapsulation Mode
================================================================

This section describes how to configure an SMPTE-2059-2 packet encapsulation mode. SMPTE-2059-2 packets can be encapsulated into Layer 3 packets for transmission. Select the encapsulation type based on networking environments and configure the source and destination IP addresses and transmission priority.

#### Prerequisites

Before configuring an SMPTE-2059-2 packet encapsulation mode, check the type of the link over which SMPTE-2059-2 packets are transmitted.

* For Layer 3 link transmission, select the UDP encapsulation mode.


#### Context

Select an SMPTE-2059-2 packet encapsulation mode based on networking environments and specify the source IP address, destination IP address, and transmission priority for SMPTE-2059-2 packets.

Perform the following operations on an SMPTE-2059-2 device:


#### Procedure

* Configure the UDP encapsulation mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ptp udp-egress**](cmdqueryname=ptp+udp-egress) **source-ip** *source-ip* [ **destination-ip** *destination-ip* ]
     
     
     
     The interface is configured to use UDP to encapsulate SMPTE-2059-2 packets with the specified source and destination IP addresses.
     
     + For unicast UDP encapsulation:
       
       Specify the unicast destination IP address encapsulated in the PTP packet in the interface view.
     + For multicast UDP encapsulation:
       
       A default multicast destination IP address is adopted, which means that the **destination-ip** *destination-ip* parameter does not need to be configured. The following table lists the mapping between default multicast destination IP addresses and delay measurement mechanisms.
       
       **Table 1** Mapping between default multicast destination IP addresses and delay measurement mechanisms
       | Packet Type | IP Address |
       | --- | --- |
       | Non-peer delay measurement mechanism | 224.0.1.129 |
       | Peer delay measurement mechanism | 224.0.0.107 |
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the **destination-ip** *destination-ip* parameter is not specified, a multicast IP address is used by default.
  4. Run [**ptp udp-egress**](cmdqueryname=ptp+udp-egress) **destination-mac** *destination-mac*
     
     
     
     The next-hop MAC address is specified for the interface to send SMPTE-2059-2 packets.
  5. Run [**ptp udp-egress**](cmdqueryname=ptp+udp-egress) **source-ip** *source-ip* [ **dscp** *dscp* ]
     
     
     
     A DSCP value is set for the interface to send UDP-encapsulated SMPTE-2059-2 packets.
  6. Run [**ptp udp-egress**](cmdqueryname=ptp+udp-egress) **source-ip** *source-ip* **vlan** *vlan-id* [ **priority** *priority* ]
     
     
     
     A VLAN ID and a priority value are set for the interface to send or receive UDP-encapsulated SMPTE-2059-2 packets.
     
     For SMPTE-2059-2 services, higher values of *dscp* and *priority* minimize the delay or congestion impact on clock signal recovery. Using the largest values of *dscp* and *priority* is recommended.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.