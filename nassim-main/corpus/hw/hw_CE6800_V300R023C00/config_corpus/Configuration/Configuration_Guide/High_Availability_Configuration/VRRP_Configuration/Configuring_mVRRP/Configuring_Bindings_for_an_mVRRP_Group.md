Configuring Bindings for an mVRRP Group
=======================================

Configuring Bindings for an mVRRP Group

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface where a common VRRP group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
   
   A common VRRP group and an mVRRP group must be configured on different interfaces.
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Bind the common VRRP group to an mVRRP group.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id1 track admin-vrrp interface interface-type interface-number vrid virtual-router-id2 [ unflowdown ]
   ```
   A common VRRP group can be bound to an mVRRP group in either of the following modes:
   * Flowdown: This mode applies to networks on which both user-to-network and network-to-user traffic is transmitted over the same path. Some devices check the consistency of the paths used for transmitting user-to-network and network-to-user traffic. If user-to-network and network-to-user traffic is transmitted over different paths, traffic may be discarded. In this case, configure the flowdown mode to ensure that traffic is forwarded properly.
   * Unflowdown: This mode applies to networks where user-to-network and network-to-user traffic is transmitted over different paths. In this mode, the mVRRP group and its bound service VRRP groups are in the same state.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.

Run the **[**display vrrp binding**](cmdqueryname=display+vrrp+binding)** [ ****interface**** { **interface-name1** | **interface-type1** **interface-number1** } ] [ ****vrid**** **admin-virtual-router-id** ] [ ****member-vrrp**** [ ****interface**** { **interface-name2** | **interface-type2** **interface-number2** } ] [ ****vrid**** **member-vrid-value** ] ] command to check the bindings between a service VRRP group, service interface, and service PW and the mVRRP group