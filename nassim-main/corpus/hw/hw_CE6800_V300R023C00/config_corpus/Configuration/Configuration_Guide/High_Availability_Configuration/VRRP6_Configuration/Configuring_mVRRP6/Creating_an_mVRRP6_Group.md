Creating an mVRRP6 Group
========================

Creating an mVRRP6 Group

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
4. Create an mVRRP6 group.
   
   
   ```
   [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id admin [ ignore-if-down ]
   ```
   
   
   
   If the user-side device does not support broadcast, it cannot transparently forward VRRP6 Advertisement packets from the master device to the backup device. In this case, you can configure the mVRRP6 group on the interfaces directly connecting the master and backup devices to implement VRRP6 status negotiation. However, if either of the directly connected VRRP6-enabled interfaces fails, the VRRP6 status on the other VRRP6-enabled interface becomes Initialize, leading to service interruptions. To prevent this issue, you are advised to specify the **ignore-if-down** parameter when configuring an mVRRP6 group. This enables the other VRRP6-enabled device to ignore interface down events and ensures proper service transmission.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```