Understanding ARP
=================

Understanding ARP

#### ARP Message Format

[Figure 1](#EN-US_CONCEPT_0000001176743503__fig1054852051912) shows the ARP message format. An Ethernet frame in which an ARP message is encapsulated in the payload is called an ARP frame. An ARP message is only 28 bytes long. The minimum data length of an Ethernet frame is 46 bytes and the maximum data length is 1500 bytes. If the data length of an Ethernet frame is less than 46 bytes, padding bytes are added to meet the requirement for the minimum data length. The padding length may vary with devices. The minimum padding length is 18 bytes.

**Figure 1** ARP message format  
![](figure/en-us_image_0000001378894410.png "Click to enlarge")

**Table 1** Description of main fields
| Field | Description |
| --- | --- |
| Ethernet destination address | Ethernet destination MAC address. For an ARP request message, the value of this field is the broadcast MAC address 0xFF-FF-FF-FF-FF-FF. |
| Ethernet source address | Ethernet source MAC address. |
| Frame type | Data type.  For an ARP request or reply message, the value of this field is 0x0806. |
| Data | Payload. The minimum data length of an Ethernet frame is 46 bytes and the maximum data length is 1500 bytes. If the data length of an Ethernet frame is less than 46 bytes, padding bytes are added to meet the requirement for the minimum data length. |
| Hardware type | Hardware address type. For an Ethernet network, the value of this field is 1. |
| Protocol type | Mapped protocol address type. For an IP address, the value of this field is 0x0800. |
| Hardware address length | Hardware address length. For an ARP request or reply message, the value of this field is 6. |
| Protocol address length | Protocol address length. For an ARP request or reply message, the value of this field is 4. |
| OP | Operation type. Values 1 and 2 indicate an ARP request and reply, respectively. |
| Sender MAC address | MAC address of the sender. |
| Sender IP address | IP address of the sender. |
| Target MAC address | Destination MAC address. For an ARP request message, the value of this field is 0x00-00-00-00-00-00. |
| Target IP address | IP address of the receiver. |
| CRC | Cyclic redundancy check, which is used to check whether an error occurs in the frame. |



#### Address Resolution Process

ARP uses ARP request and reply messages to complete address resolution.

**Figure 2** ARP request  
![](figure/en-us_image_0000001130624068.png)

As shown in [Figure 2](#EN-US_CONCEPT_0000001176743503__fig_dc_fd_ARP_000101), HostA and HostB are on the same network segment, and HostA needs to send IP datagrams to HostB.

HostA searches the local ARP table for the ARP entry corresponding to HostB. If the corresponding ARP entry is found, HostA encapsulates the IP datagrams into Ethernet frames and forwards them to HostB based on its MAC address.

If the corresponding ARP entry is not found, HostA caches the IP datagrams and broadcasts an ARP request message. In the ARP request message, the IP and MAC addresses of the sender are the IP and MAC addresses of HostA. The destination IP address is the IP address of HostB, and the destination MAC address comprises all 0s. All hosts on the same network segment can receive the ARP request message, but only HostB processes the message.

**Figure 3** ARP reply  
![](figure/en-us_image_0000001176663609.png)

HostB compares its IP address with the destination IP address in the ARP request message. If the two addresses are the same, HostB adds the IP and MAC addresses of the sender (HostA) to the local ARP table. HostB then unicasts an ARP reply message, which contains its MAC address, to HostA, as shown in [Figure 3](#EN-US_CONCEPT_0000001176743503__fig_dc_fd_ARP_000102).

After receiving the ARP reply message, HostA adds HostB's MAC address into the local ARP table. In addition, HostA encapsulates the IP datagrams and forwards them to HostB.