Configuring Dynamic ARP
=======================

Configuring Dynamic ARP

#### Prerequisites

Before configuring dynamic ARP, you have completed the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is up.


#### Context

Hosts and devices can learn dynamic ARP entries by default. You can adjust dynamic ARP aging parameters or optimize the ARP entry update policy as required.

![](public_sys-resources/note_3.0-en-us.png) 

If the aging time of dynamic ARP entries is too short, for example, 1 minute, the device will be busy updating dynamic ARP entries. This consumes a lot of system resources and affects the processing of other services.

Length of time before the deletion of a dynamic ARP entry = Number of ARP aging probes x Probe interval. Setting a long probe interval is not recommended, because a long interval will delay the deletion of an aged dynamic ARP entry.



#### Procedure

* Adjust aging parameters of dynamic ARP entries in the system view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Adjust aging parameters of dynamic ARP entries.
     
     
     
     **Table 1** Adjusting aging parameters of dynamic ARP entries
     | Operation | Command | Description |
     | --- | --- | --- |
     | Set an aging time for dynamic ARP entries. | [**arp timeout**](cmdqueryname=arp+timeout) *expire-time* | You can run this command to adjust the aging time of dynamic ARP entries, updating the entries promptly. |
     | Set the number of probes for aging dynamic ARP entries. | [**arp detect times**](cmdqueryname=arp+detect+times) *times-value* | To improve communication reliability, run this command to adjust the number of probes for aging dynamic ARP entries, updating the entries promptly. |
     | Set a probe interval for aging dynamic ARP entries. | [**arp detect interval**](cmdqueryname=arp+detect+interval) *detect-interval* | You can run this command to set a probe interval for aging dynamic ARP entries, improving probe flexibility. Before aging a dynamic ARP entry, the system performs probes. If the system does not receive any response within the probe interval, it deletes the entry. |
     | Enable the device to unicast ARP aging probe messages through interfaces. | [**arp detect mode unicast**](cmdqueryname=arp+detect+mode+unicast) | If the IP address of the peer device remains unchanged but its MAC address changes frequently, it is recommended that you configure the local device to broadcast ARP aging probe messages. If the MAC address of the peer device remains unchanged, network bandwidth resources are insufficient, and the aging time of ARP entries is set to a small value, it is recommended that you configure the local device to unicast ARP aging probe messages. |
     | Disable the device from responding to TC messages. | [**arp topology-change disable**](cmdqueryname=arp+topology-change+disable) | After the device is disabled from responding to TC messages, it does not age or delete ARP entries after receiving TC messages, reducing resource consumptions caused by frequent ARP entry updates and minimizing adverse impacts on user services. |
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Adjust aging parameters of dynamic ARP entries in the interface view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  4. Adjust aging parameters of dynamic ARP entries.
     
     
     
     **Table 2** Adjusting aging parameters of dynamic ARP entries
     | Operation | Command | Description |
     | --- | --- | --- |
     | Set an aging time for dynamic ARP entries. | [**arp timeout**](cmdqueryname=arp+timeout) *expire-time* | You can run this command to adjust the aging time of dynamic ARP entries, updating the entries promptly. |
     | Set the number of probes for aging dynamic ARP entries. | [**arp detect times**](cmdqueryname=arp+detect+times) *times-value* | To improve communication reliability, run this command to adjust the number of probes for aging dynamic ARP entries, updating the entries promptly. |
     | Set a probe interval for aging dynamic ARP entries. | [**arp detect interval**](cmdqueryname=arp+detect+interval) *detect-interval* | You can run this command to set a probe interval for aging dynamic ARP entries, improving probe flexibility. Before aging a dynamic ARP entry, the system performs probes. If the system does not receive any response within the probe interval, it deletes the entry. |
     | Enable the device to unicast ARP aging probe messages through interfaces. | [**arp detect mode unicast**](cmdqueryname=arp+detect+mode+unicast) | If the IP address of the peer device remains unchanged but its MAC address changes frequently, it is recommended that you configure the local device to broadcast ARP aging probe messages. If the MAC address of the peer device remains unchanged, network bandwidth resources are insufficient, and the aging time of ARP entries is set to a small value, it is recommended that you configure the local device to unicast ARP aging probe messages. |
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display arp interface**](cmdqueryname=display+arp+interface) { *interface-name* | *interface-type interface-number* } command to check ARP entries on an interface.
* Run the [**display arp vpn-instance**](cmdqueryname=display+arp+vpn-instance) *vpn-instance-name* **dynamic** command to check dynamic ARP entries of a VPN instance.
* Run the [**display arp**](cmdqueryname=display+arp) [ **network** *network-address* [ *network-mask* | *mask-length* ] ] **dynamic** command to check dynamic ARP entries.