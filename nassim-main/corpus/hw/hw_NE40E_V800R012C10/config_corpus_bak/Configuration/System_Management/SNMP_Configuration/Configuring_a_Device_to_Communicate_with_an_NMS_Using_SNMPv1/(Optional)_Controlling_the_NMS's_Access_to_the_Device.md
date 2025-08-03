(Optional) Controlling the NMS's Access to the Device
=====================================================

This section describes how to specify an NMS and manageable MIB objects for SNMPv1-based communication between the NMS and managed device to improve communication security.

#### Context

If a device is managed by multiple NMSs that use the same community name, note the following points:

* If all the NMSs are required to access the objects in the Viewdefault view (1.3.6.1), skip the following steps.
* If some of the NMSs are required to access the objects in the Viewdefault view (1.3.6.1), skip steps [7](#EN-US_TASK_0172360996__step_dc_vrp_snmp_cfg_000605) and [8](#EN-US_TASK_0172360996__step_dc_vrp_snmp_cfg_000606).
* If all the NMSs are required to manage specified objects on the device, skip steps [2](#EN-US_TASK_0172360996__step_dc_vrp_snmp_cfg_000602), [3](#EN-US_TASK_0172360996__step_dc_vrp_snmp_cfg_000603), [4](#EN-US_TASK_0172360996__step_dc_vrp_snmp_cfg_000000), and [5](#EN-US_TASK_0172360996__step_dc_vrp_snmp_cfg_000604).
* If some of the NMSs are required to manage specified objects on the device, perform all the following steps.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command to create a basic ACL to filter network administrators.
3. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ [ **fragment-type** { **fragment** | **fragment-subseq** | **non-fragment** | **non-subseq** | **fragment-spe-first** } ] | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* command to configure a basic ACL rule.
   
   
   * If the address of a login user matches an ACL rule in which the specified action is **permit**, the user is allowed to log in to the device.
   * If the address of a login user matches an ACL rule in which the specified action is **deny**, the user is not allowed to log in to the device.
   * If the address of a login user is not within the address range specified in the configured ACL rule, the user is not allowed to log in to the device.
   * If the referenced ACL does not contain any rules or does not exist, the login of users is not subject to the ACL, and any users can log in to the device.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
6. (Optional) Run the [**snmp-agent acl**](cmdqueryname=snmp-agent+acl) { *acl-number* | *acl-name* } command to configure an ACL for SNMP.
7. Run the [**snmp-agent mib-view**](cmdqueryname=snmp-agent+mib-view) *type* *view-name* *oid-tree* command to create a MIB view and specify manageable MIB objects.
   
   
   * **excluded**: If a few MIB objects on the device or some objects in the current MIB view do not or no longer need to be managed by the NMS, configure **excluded** in the command to exclude these MIB objects.
   * **included**: If a few MIB objects on the device or some objects in the current MIB view need to be managed by the NMS, configure **included** in the command to include these MIB objects.
8. Run the [**snmp-agent community**](cmdqueryname=snmp-agent+community) { **read** | **write** } **cipher** *host-string* [ **mib-view** *security-string-cipher* | **acl** { *acl-number* | *acl-name* } | **alias** *alias-name* ] \* command to specify the NMS's access permissions.
   
   
   * **read** needs to be configured in the command if the NMS administrator needs the read permission in a specified view. For example, a low-level administrator needs to read certain data.
   * **write** needs to be configured in the command if the NMS administrator needs the read and write permissions in a specified view. For example, a high-level administrator needs to read and write certain data.
   * **mib-view** *view-name* does not need to be configured in the command if some of the NMSs that use the community name need to have permissions to access the objects in the Viewdefault view (1.3.6.1).
   * **acl** *acl-number* does not need to be configured in the command if all the NMSs that use the community name need to manage specified objects on the device.
     
     **mib-view** and **acl** need to be configured in the command if some of the NMSs that use the community name need to manage specified objects on the device.
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Follow-up Procedure

After the access permissions are configured, especially after the IP address of the NMS is specified, if the IP address changes (for example, the NMS changes its location, or IP addresses are reallocated due to network adjustment), you need to change the IP address of the NMS in the ACL. Otherwise, the NMS cannot access the device.