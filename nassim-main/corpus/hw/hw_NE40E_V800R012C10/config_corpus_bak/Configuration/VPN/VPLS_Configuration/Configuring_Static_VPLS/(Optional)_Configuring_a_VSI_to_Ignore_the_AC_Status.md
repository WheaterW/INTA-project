(Optional) Configuring a VSI to Ignore the AC Status
====================================================

If the services running on a legacy network need to switch to a new network, you can configure VSIs to ignore AC status.

#### Context

**Figure 1** Configuring VSIs to ignore AC status  
![](figure/en-us_image_0000002040250016.png)

In the scenario shown in [Figure 1](#EN-US_TASK_0172370088__en-us_task_0172370100_fig_dc_vrp_vpls_cfg_500601), if the services running on the legacy VPLS network need to switch to a new one, and you want to check whether the VSIs on the new network work normally before the service cutover, you need to configure the VSIs to ignore AC status on DeviceD'. After the configuration, the VSIs on DeviceD' remain up before the DSLAM is connected to the new network.

AC statuses are classified into the following types:

* Status of a physical or logical AC interface bound to a VSI
* UPE PW status in a VLL accessing VPLS scenario

If an AC interface is down but the PW is up, the VSI remains up after being enabled to ignore AC status. If an AC interface is up but the PW is down, the VSI also remains up after being enabled to ignore AC status.

Perform the following steps on the PE (DeviceD' in [Figure 1](#EN-US_TASK_0172370088__en-us_task_0172370100_fig_dc_vrp_vpls_cfg_500601)):


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Perform the following steps as required:
   * To enable all VSIs on the device to ignore AC status, perform the following operations:
     
     1. Run the [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) command to enter the MPLS L2VPN view.
     2. Run the [**vpls ignore-ac-state**](cmdqueryname=vpls+ignore-ac-state) command to configure all VSIs to ignore AC status.
   * To configure a certain VSI to ignore AC status, perform the following operations:
     
     1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command to enter the VSI view.
     2. Run the [**ignore-ac-state**](cmdqueryname=ignore-ac-state) command to configure the VSI to ignore AC status.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Follow-up Procedure

The [**vpls ignore-ac-state**](cmdqueryname=vpls+ignore-ac-state) or [**ignore-ac-state**](cmdqueryname=ignore-ac-state) command is used only during the service cutover from a legacy VPLS network to a new one. After the service cutover is complete, run the [**undo vpls ignore-ac-state**](cmdqueryname=undo+vpls+ignore-ac-state) or [**undo ignore-ac-state**](cmdqueryname=undo+ignore-ac-state) command to restore the default settings.