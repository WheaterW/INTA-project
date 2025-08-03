IPv4 Multicast Group Filtering Policy Fails to Take Effect
==========================================================

IPv4 Multicast Group Filtering Policy Fails to Take Effect

#### Fault Symptom

Hosts can receive multicast data sent to multicast groups that are not permitted in a multicast group filtering policy configured on a device.


#### Procedure

1. Run the [**display acl**](cmdqueryname=display+acl) command to check whether a correct ACL rule is configured for a multicast group filtering policy.
2. Run the [**display igmp snooping configuration**](cmdqueryname=display+igmpsnooping+configuration) command to check whether a correct multicast group filtering policy is applied to the VLAN. If not, run the [**igmp snooping group-policy**](cmdqueryname=igmpsnooping+group-policy) command to apply a correct multicast group filtering policy to the VLAN.
3. Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | **include unknown-multicast** command to check whether the device is enabled to discard unknown multicast data packets. If not, run the [**unknown-multicast discard**](cmdqueryname=unknown-multicast+discard) command to enable the device to discard unknown multicast data packets.