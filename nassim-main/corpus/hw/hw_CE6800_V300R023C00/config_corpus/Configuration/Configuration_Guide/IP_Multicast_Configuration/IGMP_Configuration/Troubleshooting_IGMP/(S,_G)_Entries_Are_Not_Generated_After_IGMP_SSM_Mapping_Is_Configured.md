(S, G) Entries Are Not Generated After IGMP SSM Mapping Is Configured
=====================================================================

(S, G) Entries Are Not Generated After IGMP SSM Mapping Is Configured

#### Fault Symptom

An interface is enabled with SSM mapping and IGMP, and is configured with a static SSM mapping policy. The interface has received IGMPv1 or IGMPv2 Report messages, but the multicast forwarding table does not contain the (S, G) entries matching the mapping rules.


#### Possible Causes

G in an IGMP Report message is not within the SSM group address range.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim)
   ```
3. Check whether the SSM group address range has been redefined on the device.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   
   If the command output displays "ssm-policy," the SSM group address range has been redefined on the device.
4. Check the ACL configuration and ensure that G is within the SSM group address range.
   
   
   ```
   [display acl](cmdqueryname=display+acl) { acl-number | name acl-name | all }
   ```
   
   
   
   By default, the SSM group address range is from 232.0.0.0 to 232.255.255.255. If G is not within the SSM group address range defined by the ACL, run the [**ssm-mapping**](cmdqueryname=ssm-mapping) *group-address* { *mask* | *mask-length* } *SrcAddr* command in the IGMP view to redefine the mapping.