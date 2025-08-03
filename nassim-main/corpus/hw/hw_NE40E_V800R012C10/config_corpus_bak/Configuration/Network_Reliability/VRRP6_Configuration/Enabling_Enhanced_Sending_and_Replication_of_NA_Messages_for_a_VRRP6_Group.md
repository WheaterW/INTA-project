Enabling Enhanced Sending and Replication of NA Messages for a VRRP6 Group
==========================================================================

After enhanced sending and replication of Neighbor Advertisement (NA) messages is enabled for a VRRP6 group, when a backup device in the VRRP6 group assumes the master role, it sends an NA message for each virtual IPv6 address six consecutive times. At the same time, the device replicates each NA message to be sent to each Eth-Trunk member interface if the VRRP6 group is configured on an Eth-Trunk interface or Eth-Trunk sub-interface. This ensures that downstream devices can receive the NA messages and update destination MAC addresses and outbound interfaces in time.

#### Context

To ensure that downstream devices can receive the NA messages and update destination MAC addresses and outbound interfaces in time, enable enhanced sending of NA messages for the VRRP6 group. After this function is enabled, when a backup device in the VRRP6 group assumes the master role, it sends an NA message for each virtual IPv6 address six consecutive times.

In the scenario where a VRRP6 group is configured on an Eth-Trunk interface or Eth-Trunk sub-interface, when a backup device in the VRRP6 group assumes the master role, it sends an NA message for each virtual IPv6 address to only one Eth-Trunk member interface by default. To ensure that downstream devices can receive the NA messages in time and improve network convergence performance, enable replication of NA messages for the VRRP6 group. After this function is enabled, when a backup device in the VRRP6 group assumes the master role, it replicates each NA message to be sent to each Eth-Trunk member interface. This allows downstream devices to receive the NA messages and update entries in time, speeding up network convergence.


#### Procedure

* Enable enhanced sending of NA messages for a VRRP6 group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp6 na enhance enable**](cmdqueryname=vrrp6+na+enhance+enable)
     
     
     
     Enhanced sending of NA messages is enabled for a VRRP6 group.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable replication of NA messages for a VRRP6 group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **eth-trunk** *trunk-id [ .subnumber ]*
     
     
     
     An Eth-Trunk interface or Eth-Trunk sub-interface is displayed.
  3. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* [ **virtual-ip** *virtual-address* [ **link-local** ] ]
     
     
     
     A VRRP6 group is created and a virtual IPv6 address is assigned to it.
  4. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id1* **track** **admin-vrrp** **interface** *interface-type* *interface-number* **vrid** *virtual-router-id2* **unflowdown**
     
     
     
     The VRRP6 group is bound to an mVRRP6 group in unflowdown mode.
  5. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **na copy-to-member**
     
     
     
     Replication of NA messages is enabled for the VRRP6 group.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring enhanced sending and replication of NA messages for a VRRP6 group, run the [**display vrrp6**](cmdqueryname=display+vrrp6) **interface** *interface-type* *interface-number* [ **vrid** *virtual-id* ] **verbose** command to check whether replication of NA messages is enabled for the VRRP6 group. Specifically, check whether **enabled** is displayed in the **Na Copy** field of the command output.