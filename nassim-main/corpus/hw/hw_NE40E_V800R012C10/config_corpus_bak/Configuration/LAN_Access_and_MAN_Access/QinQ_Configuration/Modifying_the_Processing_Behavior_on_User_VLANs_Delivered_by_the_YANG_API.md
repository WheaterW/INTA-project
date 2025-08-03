Modifying the Processing Behavior on User VLANs Delivered by the YANG API
=========================================================================

You can modify the processing behavior on user VLANs that are consecutively delivered to the same sub-interface by the YANG API.

#### Usage Scenario

When the YANG API consecutively delivers user VLANs to a QinQ VLAN tag termination sub-interface on a device, if the inner or outer VLAN IDs delivered successively are adjacent, the device merges them into a VLAN range by default. However, this behavior is incompatible with the YANG data. Based on whether QoS services are configured for the user VLANs delivered earlier, one of the following situations arise:

* If no QoS service is configured, the user VLAN configuration fails to be delivered later.
* If QoS services are configured, the device successfully merges consecutive VLANs into a VLAN range. However, because this behavior is not compatible with the YANG data, YANG cannot be used to perform any separate operations on the pre-merged user VLANs.

To prevent errors caused by such incompatibility between the device and YANG, you can modify the processing behavior on user VLANs delivered by YANG API in advance from the merge mode to the non-merge mode.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ethernet yang-mode user-vlan no-merge**](cmdqueryname=ethernet+yang-mode+user-vlan+no-merge)
   
   
   
   The merge mode (default mode) is switched to the non-merge mode. This command takes effect only for YANG API-delivered configurations.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it as follows:

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check whether the mode is successfully switched.