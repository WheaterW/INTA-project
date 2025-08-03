Configuring Rapid VRRP Switchback
=================================

Configuring Rapid VRRP Switchback

#### Context

Configure rapid VRRP switchback on the master device in an mVRRP group.

![](public_sys-resources/note_3.0-en-us.png) 

Rapid VRRP switchback takes effect only for an mVRRP group in which the master device monitors a VRRP-disabled interface or feature and reduces its priority if the interface or feature fails.



#### Prerequisites

Before configuring rapid VRRP switchback, you have completed the following task:

* Configure an mVRRP group.

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
4. (Optional) Configure a preemption delay of 0s for the device in the mVRRP group.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id [preempt timer](cmdqueryname=preempt+timer) delay delay-time
   ```
   
   The default preemption delay is 0s, indicating immediate preemption.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This step is required if the preemption delay is set to a non-zero value for a device in an mVRRP group.
5. Enable rapid VRRP switchback.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id fast-resume
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The [**vrrp vrid fast-resume**](cmdqueryname=vrrp+vrid+fast-resume) command takes precedence over the [**vrrp recover-delay**](cmdqueryname=vrrp+recover-delay) command. For example, if you enable rapid VRRP switchback for VRRP group 1 and set the VRRP status recovery delay to a non-zero value in the system view, the VRRP status recovery delay does not take effect for VRRP group 1.
   
   After you run the [**vrrp vrid fast-resume**](cmdqueryname=vrrp+vrid+fast-resume) command to enable rapid VRRP switchback, this function is disabled if the preemption delay is reset to a non-zero value, the VRRP device is configured to work in non-preemption mode, or the mVRRP group is deleted.
6. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.