Configuring MAC Address-based VLAN Assignment
=============================================

Configuring MAC Address-based VLAN Assignment

#### Prerequisites

Before configuring MAC address-based VLAN assignment, you have completed the following task:

* Create a VLAN. For details, see [Creating and Deleting a VLAN](vrp_vlan_cfg_0013.html).


#### Context

In MAC address-based VLAN assignment mode, you do not need to reconfigure VLANs for users when their physical locations change. This improves network access security and flexibility.

In MAC address-based VLAN assignment mode, only untagged packets are processed. For tagged packets, only interface-based VLAN assignment mode is used.

When receiving an untagged packet, an interface matches the source MAC address of the packet against MAC-VLAN entries:

* If a matching entry is found, the interface forwards the packet based on the VLAN ID and priority in the entry.
* Otherwise, the interface matches the packet according to other matching rules.

![](public_sys-resources/note_3.0-en-us.png) 

An interface enabled with MAC address-based VLAN assignment cannot process protocol packets that need to be sent to the CPU. As such, MAC address-based VLAN assignment is recommended in Layer 2 transparent transmission scenarios.


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
3. Associate a MAC address with the VLAN.
   
   
   ```
   [mac-vlan mac-address](cmdqueryname=mac-vlan+mac-address) mac-address [ priority priority ]
   ```
   
   The MAC address cannot be all Fs, all 0s, or a multicast MAC address.
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
8. Configure the hybrid interface to allow packets from the MAC address-based VLANs to pass through.
   
   
   ```
   [port hybrid untagged vlan](cmdqueryname=port+hybrid+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-10> | all }
   ```
9. Enable MAC address-based VLAN assignment.
   
   
   ```
   [mac-vlan enable](cmdqueryname=mac-vlan+enable)
   ```
10. (Optional) Configure a higher priority for MAC address-based VLAN assignment or subnet-based VLAN assignment if both of them are configured on the interface.
    
    
    ```
    [vlan precedence](cmdqueryname=vlan+precedence) { ip-subnet-vlan | mac-vlan }
    ```
    
    By default, MAC address-based VLAN assignment has a higher priority than subnet-based VLAN assignment.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display mac-vlan**](cmdqueryname=display+mac-vlan) { **vlan** *vlan-id* | **mac-address** { *mac-address* | **all** } } command to check information about VLANs assigned based on MAC addresses.