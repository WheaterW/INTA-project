Configuring a Management VLAN for Centralized Device Management
===============================================================

Configuring a Management VLAN for Centralized Device Management

#### Prerequisites

Before configuring a management VLAN for centralized device management, you have completed the following tasks:

* Create VLANs. For details, see [Creating and Deleting a VLAN](vrp_vlan_cfg_0013.html).
* Assign VLANs. For details, see [Configuring Interface-based VLAN Assignment](vrp_vlan_cfg_0018.html), [Configuring MAC Address-based VLAN Assignment](vrp_vlan_cfg_0019.html), [Configuring Subnet-based VLAN Assignment](vrp_vlan_cfg_0020.html), and [Configuring Protocol-based VLAN Assignment](vrp_vlan_cfg_0021.html).

#### Context

Once a management VLAN is configured, you can use its VLANIF interface to log in to a device for centralized device management. You can log in to only the local device using the management interface of the local device, whereas you can log in to both the local and remote devices using the VLANIF interface of the management VLAN.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Create a management VLAN.
   
   
   ```
   [management-vlan](cmdqueryname=management-vlan)
   ```
   
   Only trunk and hybrid interfaces can be added to a management VLAN.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Create a VLANIF interface and enter the VLANIF interface view.
   
   
   ```
   [interface](cmdqueryname=interface) vlanif vlan-id
   ```
   
   *vlan-id* must be the ID of the management VLAN.
6. Configure an IP address for the VLANIF interface.
   
   
   ```
   [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
   ```
   
   In most cases, a VLANIF interface of a management VLAN needs to be configured with only one management IP address. However, in some situations, for example, when users in the same management VLAN belong to multiple network segments, you need to configure one primary management IP address and multiple secondary management IP addresses for a VLANIF interface of the management VLAN.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vlan**](cmdqueryname=display+vlan) command to check the management VLAN configurations. In the command output, VLANs marked with an asterisk (\*) are management VLANs.


#### Follow-up Procedure

You can log in to a device using a VLANIF interface of a management VLAN to manage devices in a centralized manner. Select either of the following login modes as needed:

* To manage a local device, log in to the local device through Telnet or STelnet. For details, see "CLI-based Device Login" in the Configuration Guide.
* To manage remote devices, log in to the local device using Telnet or STelnet, and then log in to remote devices using Telnet or STelnet from the local device. For details, see "CLI-based Device Login" in *Configuration Guide - Basic Configuration*.