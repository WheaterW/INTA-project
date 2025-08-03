Configuring Subnet-based VLAN Assignment
========================================

Configuring Subnet-based VLAN Assignment

#### Prerequisites

Before configuring subnet-based VLAN assignment, you have completed the following task:

* Create a VLAN. For details, see [Creating and Deleting a VLAN](vrp_vlan_cfg_0013.html).


#### Context

Subnet-based VLAN assignment allows users to easily join a VLAN, transfer from one VLAN to another, and exit from a VLAN. This mode applies to scenarios that require high mobility, simplified management, and low security.

An interface with subnet-based VLAN assignment enabled processes only untagged packets. When receiving such a packet, a device determines the VLAN to which the packet is to be forwarded based on its source IP address and network segment, and then forwards the packet to the target VLAN.

![](public_sys-resources/note_3.0-en-us.png) 

An interface enabled with subnet-based VLAN assignment cannot process protocol packets that need to be sent to the CPU. As such, subnet-based VLAN assignment is recommended in Layer 2 transparent transmission scenarios.


![](public_sys-resources/note_3.0-en-us.png) 

This function is not supported by the CE6885-LL (low latency mode).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Associate a subnet with the VLAN.
   
   
   ```
   [ip-subnet-vlan](cmdqueryname=ip-subnet-vlan+ip) [ ip-subnet-index ] ip ip-address { mask | mask-length } [ priority priority ]
   ```
   
   The subnet or IP address associated with a VLAN cannot be a multicast network segment or multicast address.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the view of the Ethernet interface to be added to the VLAN.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
6. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
7. Configure the attribute for the Layer 2 Ethernet interface.
   
   
   ```
   [port link-type](cmdqueryname=port+link-type) hybrid
   ```
8. Configure the hybrid interface to allow packets from the subnet-based VLANs to pass through.
   
   
   ```
   [port hybrid untagged vlan](cmdqueryname=port+hybrid+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-10> | all }
   ```
9. Enable subnet-based VLAN assignment.
   
   
   ```
   [ip-subnet-vlan enable](cmdqueryname=ip-subnet-vlan+enable)
   ```
10. (Optional) If both MAC address-based VLAN assignment and subnet-based VLAN assignment are configured on the interface, configure a higher priority to one assignment mode.
    
    
    ```
    [vlan precedence](cmdqueryname=vlan+precedence) { ip-subnet-vlan | mac-vlan }
    ```
    
    By default, MAC address-based VLAN assignment has a higher priority than subnet-based VLAN assignment.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display ip-subnet-vlan vlan**](cmdqueryname=display+ip-subnet-vlan+vlan) { *vlan-id1* [ **to** *vlan-id2* ] | **all** } command to check information about subnets associated with VLANs.