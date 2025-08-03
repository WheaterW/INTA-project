Creating an mVRRP Group
=======================

Creating an mVRRP Group

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
4. Configure an mVRRP group.
   
   
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id admin [ ignore-if-down ]
   ```
   
   
   
   If the user-side device does not support broadcast, it cannot transparently forward VRRP Advertisement packets from the master device to the backup device. In this case, you can configure the mVRRP group on the interfaces directly connecting the master and backup devices to implement VRRP status negotiation.
   
   However, if either of the directly connected VRRP-enabled interfaces fails, the VRRP status on the other VRRP-enabled interface becomes Initialize, leading to service interruptions. To prevent this issue, you are advised to specify the **ignore-if-down** parameter when configuring an mVRRP group. This enables the other VRRP-enabled device to ignore interface down events and ensures proper service transmission.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```