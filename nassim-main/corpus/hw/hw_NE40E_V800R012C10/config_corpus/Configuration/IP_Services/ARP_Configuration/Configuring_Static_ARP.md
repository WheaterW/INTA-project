Configuring Static ARP
======================

When static ARP is used, mappings between IP addresses and MAC addresses are configured and cannot be changed on hosts or Routers. Static ARP entries are always not aged on Routers that are working properly.

#### Usage Scenario

Static ARP entries are manually configured and maintained. They cannot be aged or overwritten by dynamic ARP entries. Configuring static ARP entries improves communication security. When device A communicates with device B using a specified IP address, device A can be configured with a fixed mapping between device B's IP address and MAC address. This mapping will not be changed because devices do not update ARP entries after receiving attack packets. This ensures communication between the two devices.

Static ARP can be used for the following purposes:

* To enable a local gateway to forward packets with destination IP addresses not on the local network segment.
* To bind the invalid IP addresses of received ARP messages to a non-existent MAC address so that these ARP messages can be filtered out.

You can deploy static ARP on important network devices like servers to set up static mappings between IP addresses and MAC addresses of the peers communicating with the devices. The static mappings cannot be modified by forged ARP messages, and prevent the devices from responding to illegal ARP request messages. In this way, the devices are protected from network attacks.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Static ARP entries will never be overwritten, but configuring a large number of ARP entries is heavy workload. Therefore, static ARP is applicable to small networks on which host IP addresses seldom change.



#### Pre-configuration Tasks

Before configuring static ARP, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is Up.
* Configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is Up.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**arp static**](cmdqueryname=arp+static) *ip-address* *mac-address* [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   A static ARP entry is configured.
   
   
   
   The optional parameters for configuring static ARP on different types of interfaces vary. For details, see the command format of [**arp static**](cmdqueryname=arp+static).
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring static ARP, verify the configuration.

* Run the [**display arp slot**](cmdqueryname=display+arp+slot) *slot-id* **static** command to check the ARP entries on the board in a specified slot.
* Run the [**display arp vlan**](cmdqueryname=display+arp+vlan) *vlan-id* **interface** *interface-type interface-number* command to check the ARP entries for VLANs.
* Run the [**display arp track**](cmdqueryname=display+arp+track) command to check the ARP entries learned by VLANIF/VBDIF interfaces and outbound interface changes.