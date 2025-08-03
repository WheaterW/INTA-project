Configuring a Device to Add Double VLAN Tags to Untagged Packets
================================================================

Configuring a Device to Add Double VLAN Tags to Untagged Packets

#### Context

Generally, two devices are required to add double tags to packets. After this function is configured:

* One device can add double tags to packets, facilitating user configurations.
* A Layer 2 interface can add double tags to untagged packets to differentiate services or users.

![](public_sys-resources/note_3.0-en-us.png) 

* Because only hybrid interfaces can distinguish between tagged and untagged modes, you are advised to set the interface type to hybrid.
* If an interface is configured as a trunk interface, you can run the **port trunk pvid vlan** command to configure the interface to remove the VLAN tag from packets carrying the default VLAN ID.
* Only the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, CE8875, CE8865, CE8865-SAN, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885H, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ support this function.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a VLAN to function as the outer VLAN.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
   
   
   
   The interface can be a physical interface or an Eth-Trunk interface.
5. Change the interface working mode from Layer 3 to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
6. Set the Layer 2 interface attribute to hybrid or trunk.
   
   
   ```
   [port link-type](cmdqueryname=port+link-type) { hybrid | trunk }
   ```
   
   
   
   By default, the link type of an interface is access.
7. Add the interface to VLANs.
   
   
   * For a hybrid interface that sends frames in untagged mode, add it to VLANs in untagged mode.
     ```
     [port hybrid untagged vlan](cmdqueryname=port+hybrid+untagged+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-10> | all }
     ```
   
   
   * For a trunk interface, add it to VLANs.
     ```
     [port trunk allow-pass vlan](cmdqueryname=port+trunk+allow-pass+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-40> | all }
     ```
8. Configure the interface to add double VLAN tags to untagged packets.
   
   
   ```
   [port vlan-stacking untagged](cmdqueryname=port+vlan-stacking+untagged) stack-vlan vlan-id3 stack-inner-vlan stackInnerVid
   ```
   
   If the PVID of an interface is not VLAN 1 (default value), restore the PVID to the default value before running the **port vlan-stacking** command.
9. Exit the interface view and return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
10. Enter the interface view.
    
    
    ```
    [interface](cmdqueryname=interface) interface-type interface-number
    ```
    
    
    
    This interface is the outbound interface for QinQ packets, different from the interface specified in Step 2.
11. Configure interface attributes.
    
    
    ```
    [port link-type](cmdqueryname=port+link-type) trunk
    ```
12. Configure the outer VLANs to which the interface needs to be added.
    
    
    ```
    [port trunk allow-pass vlan](cmdqueryname=port+trunk+allow-pass+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-40> | all }
    ```
13. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display this**](cmdqueryname=display+this) command in the interface view of the inbound interface to check the VLAN stacking configuration on the inbound interface.
* Run the [**display this**](cmdqueryname=display+this) command in the interface view of the outbound interface to check the VLAN stacking configuration on the outbound interface.