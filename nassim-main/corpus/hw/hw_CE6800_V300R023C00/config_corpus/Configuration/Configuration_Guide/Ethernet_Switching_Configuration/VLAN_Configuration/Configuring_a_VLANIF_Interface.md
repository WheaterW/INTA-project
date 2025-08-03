Configuring a VLANIF Interface
==============================

Configuring a VLANIF Interface

#### Prerequisites

Before configuring a VLANIF interface, you have completed the following tasks:

* Create the VLAN corresponding to the VLANIF interface.
* Add an interface to the VLAN corresponding to the VLANIF interface. For details, see [Configuring Interface-based VLAN Assignment](vrp_vlan_cfg_0018.html), [Configuring MAC Address-based VLAN Assignment](vrp_vlan_cfg_0019.html), [Configuring Subnet-based VLAN Assignment](vrp_vlan_cfg_0020.html), and [Configuring Protocol-based VLAN Assignment](vrp_vlan_cfg_0021.html).

#### Context

For more information about VLANIF interfaces, see [Configuring VLANIF Interfaces to Implement Inter-VLAN Communication](vrp_vlan_cfg_0030.html).

To prevent network flapping caused by a VLANIF interface status change, set a delay after which a VLANIF interface goes down. This function is also called VLAN damping.

If a VLAN goes down because all interfaces in the VLAN have gone down, the system immediately reports the VLAN Down event to the corresponding VLANIF interface, instructing the VLANIF interface to also go down. To avoid network flapping caused by a VLANIF interface status change, enable VLAN damping on the VLANIF interface. This function enables a device to start a delay timer when the last interface in a VLAN changes from up to down, and the device will not inform the corresponding VLANIF interface of the VLAN Down event until the timer expires. If an interface in the VLAN goes up before the timer expires, the VLANIF interface remains up.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a VLANIF interface and enter the VLANIF interface view.
   
   
   ```
   [interface](cmdqueryname=interface) vlanif vlan-id
   ```
3. Configure an IP address for the VLANIF interface.
   
   
   ```
   [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
   ```
4. (Optional) Configure the delay after which the VLANIF interface goes down.
   
   
   ```
   [damping time](cmdqueryname=damping+time) delay-time
   ```
5. (Optional) Set the maximum transmission unit (MTU) for the VLANIF interface.
   
   
   ```
   [mtu](cmdqueryname=mtu) mtu
   ```
6. (Optional) Configure the bandwidth for the VLANIF interface.
   
   
   ```
   [bandwidth](cmdqueryname=bandwidth) bandwidth
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display interface vlanif**](cmdqueryname=display+interface+vlanif) [ *vlan-id* | **main** ] command to check information relating to a VLANIF interface, such as its physical status and IP address.