IPv6 Multicast Data Cannot Be Forwarded
=======================================

IPv6 Multicast Data Cannot Be Forwarded

#### Fault Symptom

Transit devices on an IPv6 multicast network can receive multicast data, but the data cannot reach leaf devices. As a result, user hosts cannot receive multicast data.


#### Possible Causes

A multicast boundary or source filtering policy is configured on the device.


#### Procedure

1. Check whether a multicast boundary is correctly configured.
   
   
   ```
   [display current-configuration](cmdqueryname=display+current-configuration) interface interface-type interface-number
   ```
   
   If **multicast ipv6 boundary** is displayed in the configuration of the interface, a multicast boundary is configured on the interface. You are advised to run the [**undo multicast ipv6 boundary**](cmdqueryname=undo+multicast+ipv6+boundary) { *ipv6-group-address* *ipv6-group-mask-length* | **all** } command to delete the configuration or replan the network to ensure that no multicast boundary is configured on the RPF interface or RPF neighbor interface.
2. Check whether the source filtering policy is correctly configured.
   
   
   ```
   [display current-configuration](cmdqueryname=display+current-configuration) configuration pim
   ```
   
   If the command output contains **source-policy acl6-number** or **source-policy acl6-name**, a source filtering policy is configured. Any multicast data that is not permitted by the ACL is then discarded. In this case, run the [**undo source-policy**](cmdqueryname=undo+source-policy) command to delete the configuration or reconfigure ACL rules to ensure that the multicast data required by users can be forwarded normally.