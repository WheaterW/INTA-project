(S, G) Entries Are Not Generated After MLD SSM Mapping Is Configured
====================================================================

(S, G) Entries Are Not Generated After MLD SSM Mapping Is Configured

#### Fault Symptom

An interface that is enabled with SSM mapping and MLD and configured with a static SSM mapping policy has received MLDv1 Report messages, but the multicast forwarding table does not contain the (S, G) entries matching the mapping rules.


#### Possible Causes

G in an MLD Report message is not within the SSM group address range.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PIM view.
   
   
   ```
   [pim ipv6](cmdqueryname=pim+ipv6)
   ```
3. Check whether the SSM group address range has been redefined on the device.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   
   If the command output displays "ssm-policy," the SSM group address range has been redefined on the device.
4. Check the ACL6 configuration and ensure that G is within the SSM group address range.
   
   
   ```
   [display acl ipv6](cmdqueryname=display+acl+ipv6) { basic-acl6-number | acl6-name acl6-name | all }
   ```
   
   
   
   By default, the SSM group address range is FF3x::/32. If G is not within the SSM group address range defined by the ACL6, run the [**ssm-mapping**](cmdqueryname=ssm-mapping) *ipv6-group-address* *ipv6-group-mask-length* *ipv6-source-address* command in the MLD view to redefine the mapping.