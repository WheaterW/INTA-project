Configuring Transparent Transmission in a VLAN to Improve Packet Forwarding Efficiency
======================================================================================

Configuring Transparent Transmission in a VLAN to Improve Packet Forwarding Efficiency

#### Prerequisites

Before configuring transparent transmission in a VLAN, you have completed the following tasks:

* Create VLANs. For details, see [Creating and Deleting a VLAN](vrp_vlan_cfg_0013.html).
* Assign VLANs. For details, see [Configuring Interface-based VLAN Assignment](vrp_vlan_cfg_0018.html), [Configuring MAC Address-based VLAN Assignment](vrp_vlan_cfg_0019.html), [Configuring Subnet-based VLAN Assignment](vrp_vlan_cfg_0020.html), and [Configuring Protocol-based VLAN Assignment](vrp_vlan_cfg_0021.html).

#### Context

The VLAN transparent transmission function allows devices to transparently transmit packets from specific VLANs. In this way, packets are not sent to devices' CPUs for processing, thereby improving packet forwarding efficiency. Specifically, sending packets to devices' CPUs for processing is called software-based forwarding, which compromises forwarding efficiency due to the additional packet processing.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure transparent transmission in the VLAN.
   
   
   ```
   [protocol-transparent](cmdqueryname=protocol-transparent)
   ```
   
   
   
   By default, transparent transmission in a VLAN is disabled.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the VLAN view to check whether transparent transmission is enabled.