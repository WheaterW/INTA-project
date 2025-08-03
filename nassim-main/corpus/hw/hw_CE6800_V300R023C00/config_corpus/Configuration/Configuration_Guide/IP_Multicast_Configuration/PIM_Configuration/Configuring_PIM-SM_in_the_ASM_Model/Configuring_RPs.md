Configuring RPs
===============

Configuring RPs

#### Context

An RP can be manually configured or dynamically elected. Manually configuring a static RP prevents frequent information exchanges between C-RPs and the BSR, thereby reducing bandwidth consumption. Dynamic RP election simplifies configuration and improves the reliability of multicast forwarding as multiple C-RPs are configured.

A static RP and dynamic RP election can both be configured, with the static RP functioning as a backup due to its lower priority. In this case, you need to ensure that the RP information is consistent among devices. Otherwise, network faults may occur. [Table 1](#EN-US_TASK_0000001176743301__tab_01) lists the default settings of some parameters related to C-BSRs and C-RPs. You are advised to use the default settings during RP configuration.

**Table 1** Default settings of some parameters related to C-BSRs and C-RPs
| Parameter | Default Setting |
| --- | --- |
| C-BSR priority | 0 |
| C-BSR hash mask length | 30 |
| BSR message fragmentation | Disabled. |
| Multicast group policy of a static RP | No multicast group policy is configured, indicating that multicast packets with any group address can be accepted. |
| Multicast group policy of a C-RP | No multicast group policy is configured, indicating that multicast packets with any group address can be accepted. |
| C-RP priority | 0 |
| Interval for sending C-RP Advertisement messages | 60s |
| Hold time of C-RP Advertisement messages | 150s |



#### Procedure

* Configure a static RP.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a type of ACL as required.
     
     
     + Configure a basic numbered ACL.
       ```
       [acl](cmdqueryname=acl) [ number ] basic-acl-number 
       ```
     + Configure a named ACL.
       ```
       [acl](cmdqueryname=acl) name acl-name basic 
       ```
  3. Configure an ACL rule.
     
     
     ```
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } source { source-ip-address { source-wildcard | 0 } | any }
     ```
  4. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  5. Enter the PIM view.
     
     
     ```
     [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
     ```
  6. Specify a static RP address.
     
     
     ```
     [static-rp](cmdqueryname=static-rp) rp-address [ basic-acl-number | acl-name acl-name ] [ preferred ]
     ```
     
     
     
     All devices in the PIM-SM domain must be configured with the same static RP address so that the static RP works properly. If **preferred** is not specified in the command, a dynamic RP elected using the BSR mechanism is preferred. The static RP is preferred only if **preferred** is specified in the command. If multiple static RPs are available for a multicast group, the RP with the highest IP address serves the group. If an ACL is specified in the command, the static RP serves only the groups permitted by the ACL.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure dynamic RP election.
  
  
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a type of ACL as required.
     + Configure a basic numbered ACL.
       ```
       [acl](cmdqueryname=acl) [ number ] basic-acl-number 
       ```
     + Configure a named ACL.
       ```
       [acl](cmdqueryname=acl) name acl-name basic 
       ```
  3. Configure an ACL rule.
     ```
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } source { source-ip-address { source-wildcard | 0 } | any }
     ```
  4. Enter the PIM view.
     ```
     [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
     ```
  5. Configure a C-BSR.
     ```
     [c-bsr](cmdqueryname=c-bsr) interface-type interface-number [ hash-length [ priority ] ]
     ```
     
     It is recommended that you configure the devices that aggregate multicast data as C-BSRs. To prevent interface flapping, which will cause frequent protocol changes, using a loopback interface for the reference of the C-BSR is recommended.
  6. (Optional) Enable BSR message fragmentation.
     ```
     [bsm semantic fragmentation](cmdqueryname=bsm+semantic+fragmentation)
     ```
     
     BSR message fragmentation prevents all fragments from becoming unavailable due to the loss of fragment information in IP fragmentation. BSR message fragmentation must be enabled on all devices. Otherwise, the devices on which the function is not enabled may receive incomplete RP information.
  7. Specify an interface for the C-RP.
     ```
     [c-rp](cmdqueryname=c-rp) interface-type interface-number [ group-policy { basic-acl-number | acl-name acl-name }basic-acl-number | priority priority | holdtime hold-interval | advertisement-interval adv-interval ] *
     ```
     
     It is recommended that you configure the devices that aggregate multicast data as C-RPs. To prevent interface flapping, which will cause frequent protocol changes, using a loopback interface for the reference of the C-RP is recommended.
     
     The **group-policy** parameter specifies the range of multicast groups that a C-RP serves. The C-RP serves only the multicast groups permitted by an ACL.
     
     The **priority** parameter specifies the priority of a C-RP. The greater the value, the lower the priority.
     
     The **holdtime** parameter specifies the timeout period during which the BSR waits to receive the Advertisement message from the C-RP.
     
     The **advertisement-interval** parameter specifies the interval at which a C-RP sends Advertisement messages.
  8. Configure a BSR boundary.
     ```
     [pim bsr-boundary](cmdqueryname=pim+bsr-boundary)
     ```
     
     BSR messages cannot pass through BSR boundaries, which divide a PIM-SM network into PIM-SM domains.
     
     It is recommended that you configure BSR boundaries on interfaces at the planned PIM-SM domain edge.
  9. (Optional) Enable Auto-RP listening. This command must be run if the device is required to interwork with an auto-RP-capable device.
     ```
     [auto-rp listening enable](cmdqueryname=auto-rp+listening+enable)
     ```
     
     Auto-RP is used for automatic RP discovery before a Bootstrap protocol is specified for PIM-SM. After this command is run, the device receives auto-RP Advertisement and Discovery messages and learns RP information from the Discovery messages.
  10. Commit the configuration.
      ```
      [commit](cmdqueryname=commit)
      ```