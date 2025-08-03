Setting a Preference Value for Direct Subnet Routes on an Interface
===================================================================

Setting a Preference Value for Direct Subnet Routes on an Interface

#### Prerequisites

Before setting a preference value for direct subnet routes on an interface, configure link layer protocol parameters for the interface to ensure that the link layer protocol status on the interface is up.


#### Context

In [Figure 1](#EN-US_TASK_0000001130782556__fig_dc_vrp_ip-route_cfg_006101), VM1 and VM2 communicates with each other. Before VM2 is migrated from campus 1 to campus 2, VM1's traffic is forwarded to VM2 through DeviceA. After VM2 is migrated from campus 1 to campus 2, traffic is still forwarded along the path used before migration, because a direct route has a higher preference than a static route. As a result, traffic fails to be forwarded. To solve the preceding problem, on DeviceA, configure a static route to the virtual migration and distribution device, and run the [**direct-route ip preference**](cmdqueryname=direct-route+ip+preference) command to change the preference of direct subnet routes to be lower than that of the static route. In this way, traffic is diverted to the virtual migration and distribution device, and this device forwards the traffic to VM2, which ensures normal traffic forwarding.

**Figure 1** Network diagram of VM migration  
![](figure/en-us_image_0000001699141213.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VBDIF interface view or VLANIF interface view.
   
   
   * Enter the VBDIF interface view.
     ```
     [interface](cmdqueryname=interface) vbdif bd-id
     ```
   * Enter the VLANIF interface view.
     ```
     [interface](cmdqueryname=interface) vlanif vlan-id
     ```![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support VBDIF interfaces.
3. Switch the working mode of the interface to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set a preference value for direct subnet routes.
   
   
   ```
   [direct-route ip preference](cmdqueryname=direct-route+ip+preference) preference-value
   ```
   
   
   
   By default, this configuration does not exist on an interface, and the preference value of direct subnet routes is 0.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This command takes effect only in the VBDIF interface view and VLANIF interface view.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the interface view of a specific interface to check the configured preference value of direct subnet routes.