Configuring Static ARP
======================

Configuring Static ARP

#### Prerequisites

Before configuring static ARP, you have completed the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is up.

#### Context

You can deploy static ARP on important network devices such as servers to set up a static mapping between IP and MAC addresses of the peers communicating with the devices. The mapping cannot be modified by forged ARP messages, and it prevents the devices from responding to invalid ARP request messages. In this way, the devices are protected against network attacks.

![](public_sys-resources/note_3.0-en-us.png) 

Static ARP entries will never be overwritten, but configuring a large number of ARP entries is laborious. Therefore, static ARP is applicable to small networks on which host IP addresses seldom change.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a static ARP entry.
   
   
   ```
   [arp static](cmdqueryname=arp+static) ip-address mac-address [ vpn-instance vpn-instance-name ]
   ```
   
   The optional parameters for configuring static ARP of different types vary. For details, see the [**arp static**](cmdqueryname=arp+static) command.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display arp vpn-instance**](cmdqueryname=display+arp+vpn-instance) *vpn-instance-name* **static** command to check static ARP entries of a VPN instance.
* Run the [**display arp**](cmdqueryname=display+arp) [ **network** *network-address* [ *network-mask* | *mask-length* ] ] **static** command to check static ARP entries.