Configuring Bindings for an mVRRP6 Group
========================================

Configuring Bindings for an mVRRP6 Group

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface where a common VRRP6 group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number 
   ```
   
   A common VRRP6 group and an mVRRP6 group must be configured on different interfaces.
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Bind the common VRRP6 group to an mVRRP6 group.
   ```
   [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id1 track admin-vrrp interface interface-type interface-number vrid virtual-router-id2 [ unflowdown ]
   ```
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display vrrp6 admin-vrrp**](cmdqueryname=display+vrrp6+admin-vrrp) command to check mVRRP6 group information.
* Run the [**display vrrp6 binding**](cmdqueryname=display+vrrp6+binding) [ **interface** *interface-type1* *interface-number1* ] [ **vrid** *virtual-router-id1* ] [ **member-vrrp** [ **interface** *interface-type2* *interface-number2* ] ] [ **vrid** *virtual-router-id2* ] command to check the bindings between the mVRRP6 group and service VRRP6 groups.