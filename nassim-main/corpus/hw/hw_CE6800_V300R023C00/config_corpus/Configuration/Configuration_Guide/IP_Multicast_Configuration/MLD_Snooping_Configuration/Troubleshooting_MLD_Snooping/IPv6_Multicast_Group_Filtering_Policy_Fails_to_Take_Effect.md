IPv6 Multicast Group Filtering Policy Fails to Take Effect
==========================================================

IPv6 Multicast Group Filtering Policy Fails to Take Effect

#### Fault Symptom

A multicast group policy is configured on a device to allow hosts to join only specific multicast groups. However, the hosts can still receive multicast data sent to other multicast groups.


#### Procedure

1. Run the [**display acl ipv6**](cmdqueryname=display+acl+ipv6) command to check whether the configured ACL6 rules match the multicast group policy.
2. Run the [**display mld snooping configuration**](cmdqueryname=display+mldsnooping+configuration) command to check whether the correct multicast group filtering policy is applied to the VLAN. If not, run the [**mld snooping group-policy**](cmdqueryname=mldsnooping+group-policy) command to apply the correct multicast group filtering policy.