Configuring Association Between ARP and Interface Status
========================================================

Association between ARP and interface status allows the local device to check whether the peer device is able to properly forward packets.

#### Background

To minimize the impact of device faults on services and improve network availability, a network device must be able to quickly detect communication faults of devices that are not directly connected. Then, measures can be taken to quickly rectify the faults to ensure the normal running of services.

Association between ARP and interface status allows the local interface to send ARP probe packets to the peer interface and checks whether the peer interface can properly forward packets based on whether a reply packet is received. This triggers fast route convergence.


#### Pre-configuration Tasks

Before configuring association between ARP and interface status, complete the following tasks:

* Configure physical parameters of the interface and ensure that the interface is physically Up.
* Configure the link layer protocol parameters and IP addresses for the interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   The view of the interface on which ARP and interface status needs to be enabled is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   The IP address of the interface is configured.
4. Run [**arp status-detect**](cmdqueryname=arp+status-detect) *ip-address*
   
   Association between ARP and interface status is enabled.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The destination IP address of ARP probe messages must be on the same network segment as the IP address of the local interface. The probed device does not need to be configured.
5. (Optional) Run [**arp status-detect mode loose**](cmdqueryname=arp+status-detect+mode+loose)
   
   The interface is configured to send ARP probe messages in loose mode.
   
   * In strict mode, an interface sends ARP probe messages when the physical status is Up. The protocol status of the local interface remains unchanged only when the local interface receives an ARP reply message from the peer interface and the source IP address of the ARP reply message is the same as the destination IP address of the ARP probe message. If no ARP reply message is received from the peer interface within the allowable attempts, the protocol status of the local interface is set to Down.
   * In loose mode, an interface sends ARP probe messages only when both the physical status and protocol status are Up. The protocol status of the local interface remains unchanged only when the local interface receives an ARP message from the peer interface and the source IP address of the ARP message is the same as the destination IP address of the ARP probe message. If no ARP message is received from the peer interface within the allowable attempts, the protocol status of the local interface is set to Down.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If association between ARP and interface status is configured on devices at both ends, you are advised to configure at least the device at one end to work in strict mode. That is, do not configure devices at both ends to send ARP probe messages in loose mode.
6. (Optional) Run [**arp status-detect interval**](cmdqueryname=arp+status-detect+interval) *detect-interval*
   
   The interval at which ARP probe messages are sent is configured.
   
   You are advised to set the interval at which ARP probe messages are sent to a large value to prevent interface flapping upon operations such as an active/standby switchover.
7. (Optional) Run [**arp status-detect times**](cmdqueryname=arp+status-detect+times) *detect-times*
   
   The maximum number of times that the interface can consecutively send ARP probe messages is configured.
   
   You are advised to set the maximum number of times an interface can consecutively send ARP probe messages to a large value to prevent interface flapping upon operations such as an active/standby switchover.
8. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command to check the status information and statistics of the interface.