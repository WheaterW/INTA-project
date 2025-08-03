Enabling HIPS
=============

Enabling HIPS

#### Context

After HIPS is enabled, the configuration and enabling status of each detection module are determined by the HIPS policy file. The policy file content cannot be modified on the device and all detection modules are enabled by default. You can configure the policy file on the NMS, which then instructs the device to obtain and apply the newly configured policy file. Before connecting the device to the NMS, complete the NETCONF configuration. For details, see "Establishing Communication Between the NMS and a Device Using NETCONF" in Configuration Guide > System Management Configuration > NETCONF Configuration. For details about the configuration on the NMS, see the product documentation of the NMS.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable HIPS.
   
   
   ```
   [hips enable](cmdqueryname=hips+enable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display hips state**](cmdqueryname=display+hips+state) command in any view to check the status of each HIPS detection module.