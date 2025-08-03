Configuring Unicast ARP Probe
=============================

To check whether a peer device is reachable and to enable a device to learn a peer device's MAC address, configure a local interface to send a unicast ARP request that carries the peer device's IP and MAC addresses as the destination addresses.

#### Background

To improve network security, some devices do not support broadcast packets.

* Before an ARP entry ages out, the local device broadcasts an ARP request packet in an attempt to update the ARP entry based on the reply from a peer device. If the peer device does not support broadcast packets, it does not respond to the broadcast ARP request packet, so the local device considers the peer device offline and deletes the ARP entry. As a result, services will be interrupted between the two devices.
* If the local device is new, it will broadcast an ARP request packet to learn the MAC addresses of other devices. If a peer device does not support broadcast packets, it will discard the ARP request packet, so the local device will not learn the peer device's MAC address. As a result, new services will not be started between the two devices.

To resolve these problems, enable the unicast ARP probe function. This function enables a local interface to send a unicast ARP request packet that carries the specified IP and MAC addresses. The unicast ARP probe function improves network security, without compromising service stability.

#### Pre-configuration Tasks

Before configuring unicast ARP probe, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is Up.
* Configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is Up.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before configuring unicast ARP probe, run the [**display arp**](cmdqueryname=display+arp) command to check all ARP entries of the device. This allows you to compare the ARP entries before and after unicast ARP probe is configured.




#### Data Preparation

To configure unicast ARP probe, you need the following data.

| No. | Data |
| --- | --- |
| 1 | Destination IP address for the unicast ARP request packet to be sent |
| 2 | Destination MAC address for the unicast ARP request packet to be sent |
| 3 | Type and number of the interface for sending out the unicast ARP request packet |
| 4 | Inner tag value for the unicast ARP request packet to be sent |
| 5 | Outer tag value for the unicast ARP request packet to be sent |




#### Procedure

1. Run [**arp send-packet**](cmdqueryname=arp+send-packet) *ip-address* *mac-address* **interface** *interface-type* *interface-number* [ **vid** *vid* [ **cevid** *cevid* ] ]
   
   
   
   Unicast ARP probe is enabled.

#### Verifying the Configuration

Run the [**display arp**](cmdqueryname=display+arp) command to check all ARP entries of the device.