Configuring Dynamic ARP
=======================

Hosts and Routers can learn dynamic ARP entries by default. However, you can adjust dynamic ARP aging parameters or optimize the ARP entry update policy.

#### Usage Scenario

ARP aging parameters include the aging time, number of ARP aging probes, and ARP aging probe interval. Proper setting of these aging parameters can improve network reliability:

* Aging time: When the aging time of a dynamic ARP entry expires, a device sends an ARP probe packet (ARP Request message) from the outbound interface recorded in the dynamic ARP entry, and starts counting the number of ARP probes.
* Number of ARP aging probes: Before deleting an aged dynamic ARP entry, a device sends ARP probe packets to the IP address recorded in the ARP entry at specified intervals. If the configured number of ARP aging probes is exceeded but the ARP entry has not been updated, the device will delete the ARP entry.
* ARP aging probe interval: It is the interval at which probe packets are sent.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  1. If the aging time of dynamic ARP entries is set too short, for example, 1 minute, the device will be busy updating dynamic ARP entries. This consumes a lot of system resources and affects the processing of other services.
  2. Length of time before the deletion of a dynamic ARP entry = Number of ARP aging probes x Probe interval
     
     Setting a long probe interval is not recommended, because a long interval will delay the deletion of an aged dynamic ARP entry according to the formula.

After the Layer 2 topology detection function is enabled, the aging time of all ARP entries corresponding to the VLAN to which a Layer 2 interface belongs is set to 0 when the status of the Layer 2 interface changes from Down to Up. Then the device resends ARP probe packets to update all ARP entries.

After the device is disabled from responding to TC messages on a ring network, it does not age or delete ARP entries after receiving TC messages, reducing resource consumptions caused by frequent ARP entry updates and minimizing adverse impacts on user services.


#### Pre-configuration Tasks

Before configuring dynamic ARP, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is Up.
* Configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is Up.

#### Procedure

* Adjust dynamic ARP aging parameters.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**arp expire-time**](cmdqueryname=arp+expire-time) *expire-time*
     
     
     
     The aging time is set for dynamic ARP entries.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In specific scenarios, after MAC entries are aged, the VLANIF interface fails to obtain the Layer 2 outbound interface and broadcast a unicast packet in the VLAN. To ensure service security, you can run the [**arp expire-time**](cmdqueryname=arp+expire-time) *expire-time* [**vlanif**](cmdqueryname=vlanif) command to set the aging time for dynamic ARP entries on all VLANIF interfaces to a value smaller than the aging time for MAC entries. This prevents unicast packets from being broadcast due to Layer 2 outbound interface mismatch.
  4. Run [**arp detect-times**](cmdqueryname=arp+detect-times) *detect-times*
     
     
     
     The number of ARP aging probes is set.
  5. Run [**arp detect-interval**](cmdqueryname=arp+detect-interval) *detect-interval*
     
     
     
     The interval for sending ARP aging probe packets is set.
  6. Run [**arp detect-mode unicast**](cmdqueryname=arp+detect-mode+unicast)
     
     
     
     The interface is configured to unicast ARP aging probe packets.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable Layer 2 topology detection.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2-topology detect enable**](cmdqueryname=l2-topology+detect+enable)
     
     
     
     Layer 2 topology detection is enabled.
* Disable the device from responding to TC packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**arp topology-change disable**](cmdqueryname=arp+topology-change+disable)
     
     
     
     The device is disabled from responding to TC packets.

#### Verifying the Configuration

After configuring dynamic ARP, verify the configuration.

* Run the [**display arp all**](cmdqueryname=display+arp+all) command to check the ARP mapping tables on the main control boards and all interface boards.
* Run the [**display arp interface**](cmdqueryname=display+arp+interface) *interface-name* command to check the ARP mapping table on a specified interface.
* Run the [**display arp slot**](cmdqueryname=display+arp+slot) *slot-id* command to check the ARP mapping table on the board in a specified slot.
* Run the [**display arp vpn-instance**](cmdqueryname=display+arp+vpn-instance) *vpn-instance-name* **slot** *slot-id* [ **dynamic** | **static** ] command to check the ARP mapping table of a specified VPN instance.