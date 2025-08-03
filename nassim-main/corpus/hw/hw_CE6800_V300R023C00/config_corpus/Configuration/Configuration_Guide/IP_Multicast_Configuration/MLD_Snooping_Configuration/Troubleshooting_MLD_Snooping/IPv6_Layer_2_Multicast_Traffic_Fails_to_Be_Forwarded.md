IPv6 Layer 2 Multicast Traffic Fails to Be Forwarded
====================================================

IPv6 Layer 2 Multicast Traffic Fails to Be Forwarded

#### Fault Symptom

After Multicast Listener Discovery (MLD) snooping is configured, users cannot receive multicast data.


#### Procedure

1. Check whether the MLD snooping version meets requirements.
   
   
   
   If the MLD snooping version configured on the device is earlier than the MLD version running on user hosts, the device only forwards received MLD Report messages to router ports and does not generate group member ports or forwarding entries.
   
   Run the [**display mld snooping configuration**](cmdqueryname=display+mldsnooping+configuration) command to check the configuration. If the MLD snooping version running on the device is earlier than the MLD version running on user hosts, run the [**mld snooping version**](cmdqueryname=mldsnooping+version) *version* command to change the version to keep version consistency.
2. Check whether the configured General Query intervals are inconsistent.
   
   
   
   If the General Query interval of the local MLD snooping device is smaller than that used on the upstream MLD querier or MLD snooping device, the local device may mistakenly age out some MLD snooping entries that are still in use. As a result, multicast data from the upstream device cannot be forwarded.
   
   Run the [**display mld snooping**](cmdqueryname=display+mldsnooping) command to check MLD snooping running parameters. If the General Query interval is smaller than that on the upstream querier or MLD snooping device, run the [**mld snooping query interval**](cmdqueryname=mldsnooping+query+interval) *query-interval* command to adjust the General Query interval. It is recommended that the upstream and downstream devices use the same interval.
3. Check whether dynamic learning of router ports is disabled.
   
   
   
   If dynamic learning of router ports is disabled in a VLAN, the device does not listen to MLD Query messages in the VLAN. In this case, the device cannot generate router ports.
   
   Run the [**display mld snooping configuration**](cmdqueryname=display+mldsnooping+configuration) command to check the configuration. If the command output contains "mld snooping router-learning disable", run the [**undo mld snooping router-learning disable**](cmdqueryname=undo+mld+snooping+router-learning+disable) command in the VLAN to enable dynamic learning of router ports.
4. Check whether prompt leave is configured for member ports.
   
   
   
   Prompt leave can be configured only on an interface that is connected to only one host. If an interface is connected to multiple hosts and prompt leave is enabled for member ports in the VLAN, the device deletes the forwarding entry of a member port immediately after receiving an MLD Done message from the member port, without sending a Group-Specific Query message. In this case, traffic fails to be forwarded.
   
   Run the [**display mld snooping configuration**](cmdqueryname=display+mldsnooping+configuration) command to check the configuration. If "mld   snooping prompt-leave" is displayed, run the [**undo mld snooping prompt-leave**](cmdqueryname=undo+mldsnooping+prompt-leave) command in the VLAN view to disable the prompt leave function.
5. Check whether Router-Alert option checking is configured.
   
   
   
   If Router-Alert option checking is configured, the device checks the Option field of MLD messages and discards those that do not contain the Router-Alert option.
   
   Run the [**display mld snooping configuration**](cmdqueryname=display+mldsnooping+configuration) command to check the configuration. If "mld   snooping require-router-alert" is displayed, run the [**undo mld snooping require-router-alert**](cmdqueryname=undo+mldsnooping+require-router-alert) command in the VLAN view to cancel the configuration.
6. Check whether a multicast group filtering policy is configured.
   
   
   
   If a multicast group filtering policy is configured, the multicast groups that hosts in a VLAN can join may be limited. Run the [**display mld snooping configuration**](cmdqueryname=display+mldsnooping+configuration) command to check the multicast group filtering policy configuration. If ACL6 rules are configured, run the [**display acl ipv6**](cmdqueryname=display+acl+ipv6) command to check whether the ACL6 rules are correct.