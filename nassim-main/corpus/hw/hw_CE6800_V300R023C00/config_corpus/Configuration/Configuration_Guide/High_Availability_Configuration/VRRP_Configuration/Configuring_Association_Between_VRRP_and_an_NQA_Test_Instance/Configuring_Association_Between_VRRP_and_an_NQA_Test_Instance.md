Configuring Association Between VRRP and an NQA Test Instance
=============================================================

Configuring Association Between VRRP and an NQA Test Instance

#### Prerequisites

Before configuring association between VRRP and an NQA test instance, you have completed the following tasks:

* Create an NQA test instance.
* Create a VRRP group.

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface where a VRRP group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the VRRP group to track the NQA test instance.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id track nqa admin-name test-name [ reduce value-reduced ]
   ```
   
   By default, the device that tracks the NQA instance reduces its priority by 10 if the status of the NQA test instance becomes Failed.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The NQA test instance associated with VRRP can only be an ICMP test instance.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.