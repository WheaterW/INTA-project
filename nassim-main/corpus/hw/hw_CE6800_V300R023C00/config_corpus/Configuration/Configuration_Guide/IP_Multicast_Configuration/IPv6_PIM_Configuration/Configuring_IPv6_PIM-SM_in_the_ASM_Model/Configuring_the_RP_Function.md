Configuring the RP Function
===========================

Configuring the RP Function

#### Context

An RP can be manually configured or dynamically elected. Manually configuring a static RP prevents frequent information exchanges between C-RPs and the BSR, thereby reducing bandwidth consumption. Dynamic RP election simplifies configuration and improves the reliability of multicast forwarding as multiple C-RPs are configured.

On an IPv6 PIM-SM network, the embedded RP function is enabled on each device by default, which is different from the implementation on an IPv4 network. When a device receives a multicast packet of a multicast group, the device directly parses the RP information from the corresponding group address, without the need to know the mapping between the RP and the group address in advance. The range of group addresses that a device can parse can be manually changed.

A static RP and dynamic RP election can both be configured. If they are both configured, the static RP functions as a backup RP because it has a lower priority. If both the mechanisms are used, ensure that all the devices on the network have the same RP information. Otherwise, network faults may occur.

[Table 1](#EN-US_TASK_0000001589525005__tab_01) lists the default settings of some parameters related to C-BSRs and C-RPs. You are advised to use the default settings during RP configuration.

**Table 1** Default settings of some parameters related to C-BSRs and C-RPs
| Parameter | Default Value |
| --- | --- |
| C-BSR priority | 0 |
| C-BSR hash mask length | 126 |
| BSR message fragmentation | Disabled |
| Multicast group policy of a static RP | No multicast group policy is configured, indicating that multicast packets with any group address can be accepted. |
| Multicast group policy of a C-RP | No multicast group policy is configured, indicating that multicast packets with any group address can be accepted. |
| C-RP priority | 192 |
| Interval for sending C-RP Advertisement messages | 60s |
| Hold time of C-RP Advertisement messages | 150s |
| Default group address range corresponding to the embedded RP | FF7x::/12, in which *x* is 0 or any value ranging from 3 to F. |



#### Procedure

* Configure a static RP.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an ACL6 and enter the ACL6 view.
     
     
     ```
     [acl ipv6](cmdqueryname=acl+ipv6) { name basic-acl6-name basic | [ number ] basic-acl6-number }
     ```
  3. Configure a rule for the ACL6.
     
     
     ```
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment | source { source-ipv6-address { prefix-length | source-wildcard } | source-ipv6-address/prefix-length | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
     ```
  4. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  5. Enter the IPv6 PIM view.
     
     
     ```
     [pim ipv6](cmdqueryname=pim+ipv6) [ vpn-instance vpn-instance-name ]
     ```
  6. Specify a static RP address.
     
     
     ```
     [static-rp](cmdqueryname=static-rp) rp-address [ basic-acl6-number | acl6-name acl6-name ] [ preferred ]
     ```
     
     
     
     To ensure that the static RP runs normally, you need to specify the same static RP address on all PIM devices in the PIM-SM domain. If **preferred** is not specified in the command when you configure the static RP, a dynamic RP elected using the BSR mechanism is preferred. The static RP is preferred only if **preferred** is specified in the command. If multiple static RPs are available for a multicast group, the RP with the highest IP address serves the group. If an ACL6 is specified in the command, the static RP serves only the groups permitted by the ACL6.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure dynamic RP election.
  
  
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an ACL6 and enter the ACL6 view.
     ```
     [acl ipv6](cmdqueryname=acl+ipv6) { name basic-acl6-name basic | [ number ] basic-acl6-number }
     ```
  3. Configure a rule for the ACL6.
     ```
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment | source { source-ipv6-address { prefix-length | source-wildcard } | source-ipv6-address/prefix-length | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
     ```
  4. Enter the IPv6 PIM view.
     ```
     [pim ipv6](cmdqueryname=pim+ipv6) [ vpn-instance vpn-instance-name ]
     ```
  5. Configure a C-BSR.
     ```
     [c-bsr](cmdqueryname=c-bsr) ipv6-address [ hash-length [ priority-value ] ]
     ```
     
     It is recommended that you configure the devices that aggregate multicast data as C-BSRs. To prevent interface flapping (which may otherwise cause frequent protocol changes), using a loopback interface for the reference of the C-BSR is recommended.
  6. (Optional) Enable BSR message fragmentation.
     ```
     [bsm semantic fragmentation](cmdqueryname=bsm+semantic+fragmentation)
     ```
     
     BSR message fragmentation prevents all fragments from becoming unavailable due to the loss of fragment information in IP fragmentation. BSR message fragmentation must be enabled on all devices. Otherwise, the devices on which the function is not enabled may receive incomplete RP information.
  7. Specify an interface as a C-RP.
     ```
     [c-rp](cmdqueryname=c-rp) ipv6-address [ group-policy { basic-acl6-number | acl6-name acl6-name } | holdtime hold-interval | priority priority | advertisement-interval adv-interval ] *
     ```
     
     The *ipv6-address* parameter specifies the IPv6 address of the interface which functions as a C-RP. The interface must be enabled with IPv6 PIM-SM.
     
     The **group-policy** parameter specifies the range of multicast groups that a C-RP serves. The C-RP serves only the multicast groups permitted by an ACL6.
     
     The **priority** parameter specifies the priority of a C-RP. The greater the value, the lower the priority.
     
     The **holdtime** parameter specifies the timeout period during which the BSR waits to receive the Advertisement message from the C-RP.
     
     The **advertisement-interval** parameter specifies the interval at which a C-RP sends Advertisement messages.
  8. Configure a BSR boundary.
     ```
     [pim ipv6 bsr-boundary](cmdqueryname=pim+ipv6+bsr-boundary)
     ```
     
     BSR messages cannot pass through BSR boundaries, which divide a PIM-SM network into PIM-SM domains.
     
     It is recommended that you configure BSR boundaries on interfaces at the planned PIM-SM domain edge.
  9. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```