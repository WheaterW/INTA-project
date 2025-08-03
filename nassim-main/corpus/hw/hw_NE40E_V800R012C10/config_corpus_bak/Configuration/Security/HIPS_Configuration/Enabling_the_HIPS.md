Enabling the HIPS
=================

Enabling_the_HIPS

#### Context

After the HIPS is enabled, the configuration and enabling status of each detection module are determined by the HIPS policy file. The policy file content cannot be modified on the device and all detection modules are enabled by default. You can configure a policy file on the NMS and instruct the device to obtain and apply the new policy file.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**hips enable**](cmdqueryname=hips+enable)
   
   
   
   The HIPS is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Run the [**display hips state**](cmdqueryname=display+hips+state) command to check the enabling status of each HIPS detection module.