(Optional) Manually Configuring Mappings Between Instances and VLANs
====================================================================

(Optional) Manually Configuring Mappings Between Instances and VLANs

#### Context

Based on the instance-to-VLAN mapping model of MSTP, VBST establishes 1:1 mappings between instances and VLANs. The 1:1 mappings between instances and VLANs are used by devices only to determine the VBST forwarding status.

The mappings between instances and VLANs in VBST can be configured manually or generated dynamically. A manually configured mapping takes precedence over a dynamically generated mapping.

* You can manually configure mappings between the instances and VLANs on a device. After VLANs are deleted or VBST is disabled globally, the mappings can only be manually deleted.
* After VBST is enabled, the system dynamically allocates instance IDs in ascending order to existing or new VLANs. Dynamically generated mappings cannot be changed manually; instead, they are automatically deleted after VLANs are deleted or VBST is disabled globally. If a VLAN is created when the number of dynamically specified instances exceeds the number of protected VLANs, a configuration indicating that STP is disabled in the VLAN is displayed in the configuration file.

When manually configuring mappings between instances and VLANs, consider the following factors:

* To prevent temporary loops, instance 4094 is reserved in VBST mode, and it cannot be manually mapped to a specific VLAN. Therefore, before changing the spanning tree working mode to VBST, clear instance 4094's configuration or map the VLAN to which this instance is mapped to a different available instance.
* In VBST, each instance maps a different VLAN. Therefore, to prevent multiple VLANs from being mapped to one instance, it is recommended that you run the [**display stp vlan instance**](cmdqueryname=display+stp+vlan+instance) command to view the existing mappings between instances and VLANs before configuring new mappings.
* If the number of specified instances exceeds that supported by the device, when VLANs are created, VBST does not take effect in the VLANs by default and an alarm is generated. The number of instances supported by the device is the total number of instances in manually configured and dynamically generated mappings. To enable VBST in these VLANs, release the instances mapped to the other VLANs by running the [**undo vlan**](cmdqueryname=undo+vlan) command. When the number of VBST-enabled VLANs decreases to less than 95% of the upper limit, the alarm clears and the system automatically reallocates an instance to the specific VLAN.
* If the number of configured VLANs exceeds the upper limit, deleting manually configured mappings will cause the system to reallocate the available instances to VLANs. In this scenario, VLANs that are not dynamically mapped to instances preferentially occupy the available instances. If you run the [**rollback configuration**](cmdqueryname=rollback+configuration) command to enable the system to reallocate available instances to the VLANs, configuration rollback will fail if all instances have been allocated. To prevent this from occurring, before implementing configuration rollback, determine whether the configuration can be rolled back as planned by running the [**display configuration commit changes**](cmdqueryname=display+configuration+commit+changes) command to view configuration changes. If certain configurations fail to be rolled back, run the [**display configuration rollback result**](cmdqueryname=display+configuration+rollback+result) command to check the configurations and system prompt displayed when configuration commands are run, and then manually restore the configurations.

Perform the following steps to manually configure mappings between instances and VLANs.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MST region view.
   
   
   ```
   [stp region-configuration](cmdqueryname=stp+region-configuration)
   ```
3. Configure a 1:1 mapping between an instance and a VLAN.
   
   
   ```
   [instance](cmdqueryname=instance) instance-id vlan vlan-id
   ```
   
   By default, all VLANs are mapped to the CIST instance, namely, instance 0.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```