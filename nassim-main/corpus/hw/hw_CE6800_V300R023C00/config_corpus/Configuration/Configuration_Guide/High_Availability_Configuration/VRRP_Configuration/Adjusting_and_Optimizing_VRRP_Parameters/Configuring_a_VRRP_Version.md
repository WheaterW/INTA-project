Configuring a VRRP Version
==========================

Configuring a VRRP Version

#### Context

VRRP for IPv4 supports VRRPv2 and VRRPv3. For details, see [VRRP Advertisement Packets](vrp_vrrp_cfg_0005.html).

* A VRRPv2 group can send and receive only VRRPv2 Advertisement packets. If the VRRPv2 group receives VRRPv3 Advertisement packets, they are discarded.
* A VRRPv3 group can send and receive both VRRPv2 and VRRPv3 Advertisement packets. In other words, the VRRPv3 group can communicate with both VRRPv2 and VRRPv3 groups.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a VRRP version for the device.
   ```
   [vrrp version](cmdqueryname=vrrp+version) { 2 | 3 }
   ```
   By default, VRRPv2 is used.
   * A VRRPv2-enabled device can send and receive only VRRPv2 Advertisement packets. If the device receives VRRPv3 Advertisement packets, it discards these packets.
   * If VRRPv3 has been configured, you can configure a mode for the VRRPv3-enabled device to send VRRP Advertisement packets.
3. A VRRPv3 group can send and receive both VRRPv2 and VRRPv3 Advertisement packets. To configure a mode for the VRRPv3-enabled device to send VRRP Advertisement packets, run the following commands:
   * Configure a mode for the VRRPv3-enabled device to send Advertisement packets in the system view.
     ```
     [vrrp compatible-version](cmdqueryname=vrrp+compatible-version) { 2 | 3 | all }
     ```
     
     By default, a VRRPv3-enabled device sends only VRRPv3 Advertisement packets.
   * Configure a mode for the interface where the VRRP group resides to send VRRP Advertisement packets.
     1. Enter the view of the interface where a VRRP group resides.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        ```
     2. Switch the interface working mode to Layer 3. Determine whether to perform this step based on the device configuration.
        ```
        [undo portswitch](cmdqueryname=undo+portswitch)
        ```
     3. Configure a mode for the interface to send VRRP Advertisement packets.
        ```
        [vrrp](cmdqueryname=vrrp) vrid vrid-value compatible-version{ 2 | 3 | all }
        ```
        
        By default, a device in a VRRP group sends Advertisement packets in the same mode as that configured in the system view.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.