Enabling Enhanced Sending and Replication of Gratuitous ARP Packets for a VRRP Group
====================================================================================

After enhanced sending and replication of gratuitous ARP packets is enabled for a VRRP group, when a backup device in the VRRP group assumes the master role, it sends a gratuitous ARP packet for each virtual IP address six consecutive times. At the same time, the device replicates each gratuitous ARP packet to be sent to each Eth-Trunk member interface if the VRRP group is configured on an Eth-Trunk interface or Eth-Trunk sub-interface. This ensures that downstream devices can receive the gratuitous ARP packets and update destination MAC addresses and outbound interfaces in time.

#### Context

To ensure that downstream devices can receive the gratuitous ARP packets and update destination MAC addresses and outbound interfaces in time, enable enhanced sending of gratuitous ARP packets for the VRRP group. After this function is enabled, when a backup device in the VRRP group assumes the master role, it sends a gratuitous ARP packet for each virtual IP address six consecutive times.

In the scenario where a VRRP group is configured on an Eth-Trunk interface or Eth-Trunk sub-interface, when a backup device in the VRRP group assumes the master role, it sends a gratuitous ARP packet for each virtual IP address to only one Eth-Trunk member interface by default. To ensure that downstream devices can receive the gratuitous ARP packets in time and improve network convergence performance, enable replication of gratuitous ARP packets for the VRRP group. After this function is configured, when a backup device in the VRRP group assumes the master role, it replicates each gratuitous ARP packet to be sent to each Eth-Trunk member interface. This allows downstream devices to receive the gratuitous ARP packets and update entries in time, speeding up network convergence.


#### Procedure

* Enable enhanced sending of gratuitous ARP packets for a VRRP group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp gratuitous-arp enhance enable**](cmdqueryname=vrrp+gratuitous-arp+enhance+enable)
     
     
     
     Enhanced sending of gratuitous ARP packets is enabled for a VRRP group.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable replication of gratuitous ARP packets for a VRRP group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **eth-trunk** *trunk-id [ .subnumber ]*
     
     
     
     An Eth-Trunk interface or an Eth-Trunk sub-interface is created.
  3. Run [**vrrp**](cmdqueryname=vrrp) **vrid** *virtual-router-id* [ **virtual-ip** *virtual-address* ]
     
     
     
     A VRRP group is configured and a virtual IP address is configured for the VRRP group.
  4. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id**1* **track** **admin-vrrp** **interface** *interface-type* *interface-number* **vrid** *virtual-router-id2* **unflowdown**
     
     
     
     The VRRP group is bound to an mVRRP group in unflowdown mode.
  5. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **gratuitous-arp copy-to-member**
     
     
     
     Replication of gratuitous ARP packets is enabled for the VRRP group.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring enhanced sending and replication of gratuitous ARP packets for a VRRP group, run the [**display vrrp**](cmdqueryname=display+vrrp) [ [ **interface** *interface-type* *interface-number* [ *virtual-router-id* ] [ **verbose** | **brief** ] ] | **brief** ] command to check whether replication of gratuitous ARP packets is enabled for the VRRP group. Specifically, check whether **enabled** is displayed in the **Arp Copy** field of the command output.