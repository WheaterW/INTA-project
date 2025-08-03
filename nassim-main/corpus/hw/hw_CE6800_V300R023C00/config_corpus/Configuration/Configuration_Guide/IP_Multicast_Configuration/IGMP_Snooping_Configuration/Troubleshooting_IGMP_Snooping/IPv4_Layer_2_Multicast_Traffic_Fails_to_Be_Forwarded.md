IPv4 Layer 2 Multicast Traffic Fails to Be Forwarded
====================================================

IPv4 Layer 2 Multicast Traffic Fails to Be Forwarded

#### Fault Symptom

Users fail to receive multicast data after IGMP snooping is configured.


#### Procedure

1. Check whether the device is running the correct IGMP snooping version.
   
   
   
   If the IGMP snooping version configured on the device is earlier than that running on user hosts, the device forwards IGMP Report messages to router ports but does not generate group member ports or forwarding entries.
   
   Run the [**display igmp snooping configuration**](cmdqueryname=display+igmpsnooping+configuration) command to check the IGMP snooping configuration. If the IGMP snooping version configured on the device is earlier than that running on user hosts, configure the device to use the same version used on user hosts by running the [**igmp snooping version**](cmdqueryname=igmpsnooping+version) *version* command.
2. Check whether the configured General Query intervals are inconsistent.
   
   
   
   If the General Query interval of the local IGMP snooping device is smaller than that used on the upstream IGMP querier or IGMP snooping device, the local device may often mistakenly age out some IGMP snooping entries that are still in use. As a result, multicast data matching these entries cannot be forwarded.
   
   Run the [**display igmp snooping**](cmdqueryname=display+igmpsnooping) command to check the IGMP snooping running parameters. If the General Query interval on the local device is smaller than that used on the upstream IGMP querier or IGMP snooping device, run the [**igmp snooping query interval**](cmdqueryname=igmpsnooping+query+interval) *query-interval* command to adjust the General Query interval. It is recommended that the upstream and downstream devices use the same General Query interval.
3. Check whether dynamic learning of router ports is disabled.
   
   
   
   If dynamic learning of router ports is disabled in a VLAN, the device does not listen to IGMP Query messages in the VLAN. In this case, the device cannot generate router ports.
   
   Run the [**display igmp snooping configuration**](cmdqueryname=display+igmpsnooping+configuration) command to check the configuration. If the command output contains "**igmp snooping router-learning disable**", run the [**undo igmp snooping router-learning disable**](cmdqueryname=undo+igmp+snooping+router-learning+disable) command in the VLAN to enable dynamic learning of router ports.
4. Check whether prompt leave is configured for member ports.
   
   
   
   Prompt leave can be configured only on an interface that is connected to only one host. If an interface is connected to multiple hosts and prompt leave is enabled for member ports in the VLAN, the device deletes the forwarding entry of a member port immediately after receiving an IGMP Leave message from the member port, without sending a Group-Specific Query message. In this case, traffic fails to be forwarded.
   
   Run the [**display igmp snooping configuration**](cmdqueryname=display+igmpsnooping+configuration) command to check the configuration. If the command output contains "**igmp** **snooping prompt-leave**", run the [**undo igmp snooping prompt-leave**](cmdqueryname=undo+igmpsnooping+prompt-leave) command in the VLAN view to disable prompt leave for member ports.
5. Check whether Router-Alert option checking is configured.
   
   
   
   If Router-Alert option checking is configured, the device checks the Option field of IGMP messages and discards those that do not contain the Router-Alert option.
   
   Run the [**display igmp snooping configuration**](cmdqueryname=display+igmpsnooping+configuration) command to check the configuration. If the command output contains "**igmp** **snooping require-router-alert**", run the [**undo igmp snooping require-router-alert**](cmdqueryname=undo+igmpsnooping+require-router-alert) command in the VLAN view to cancel the configuration.
6. Check whether a multicast group filtering policy is configured.
   
   
   
   If a multicast group filtering policy is configured, the multicast groups that hosts in a VLAN can join may be limited. Run the [**display igmp snooping configuration**](cmdqueryname=display+igmpsnooping+configuration) command to check the multicast group filtering policy configuration. If an ACL rule is configured, run the [**display acl**](cmdqueryname=display+acl) command to check whether the ACL rule configuration is correct.