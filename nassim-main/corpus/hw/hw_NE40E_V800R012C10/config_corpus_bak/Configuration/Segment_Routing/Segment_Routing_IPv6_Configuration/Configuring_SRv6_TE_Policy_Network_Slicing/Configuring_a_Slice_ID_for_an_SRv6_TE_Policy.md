Configuring a Slice ID for an SRv6 TE Policy
============================================

You can configure a slice ID for an SRv6 TE Policy to associate services and forwarding resources.

#### Prerequisites

Before configuring a slice ID for an SRv6 TE Policy, complete the following task:

* Configure an SRv6 TE Policy. For configuration details, see [Configuring an SRv6 TE Policy (Manual Configuration + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0110.html) or [Configuring an SRv6 TE Policy (Dynamic Delivery by a Controller + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0116.html).

#### Context

A slice ID connects the control and forwarding planes. After a slice ID is configured for a candidate path of an SRv6 TE Policy, if services are forwarded over the candidate path, the ingress inserts SRH information into packets to encapsulate the SID list of the SRv6 TE Policy, encapsulates the HBH Options header (which carriers a slice ID), and finally encapsulates the IPv6 basic header. The ingress then determines the network slice interface based on the slice ID and forwards the packets over this interface.

If the active SID on the egress of the SRv6 TE Policy is a service SID advertised by the egress, the egress executes the service SID's instructions to decapsulate the packet and remove the SRH, HBH header (only in the HBH mode), and IPv6 basic header.

An SRv6 TE Policy can be statically configured or delivered by a controller. In cases of the latter, the controller delivers a BGP Update message to a forwarder through a BGP IPv6 SR Policy peer relationship. The BGP Update message carries the slice ID of the SRv6 TE Policy's candidate path.

This section describes how to configure a slice ID for a statically configured SRv6 TE Policy.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Perform slice ID association using either of the following methods.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If both of the following methods are used, 5-tuple-based ACL matching for slice ID association takes precedence.
   
   
   
   * Associate a candidate path of an SRv6 TE Policy with a slice ID.
     1. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6 and enter its view.
     2. Run the [**srv6-te policy**](cmdqueryname=srv6-te+policy) *name-value* command to enter the SRv6 TE Policy view.
     3. Run the [**candidate-path preference**](cmdqueryname=candidate-path+preference) *preference* command to configure a candidate path and its preference for the SRv6 TE Policy.
        
        A larger preference value indicates a higher priority of a candidate path.
        
        In the same SRv6 TE Policy, the valid candidate path with the highest preference is used as the primary path, while that with the second highest preference is used as the backup path.
     4. Run the [**network-slice**](cmdqueryname=network-slice) *slice-id* **data-plane** command to configure a slice ID for the candidate path of the SRv6 TE Policy.
        
        Different slice IDs can be configured for different candidate paths of an SRv6 TE Policy.
     5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Configure 5-tuple-based ACL matching for slice ID association.
     1. Configure a traffic classification rule.
        1. Run either of the following commands to create an ACL and enter its view:
           + For a basic ACL (numbered from 2000 to 2999), run the [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command.
           + For an advanced ACL (numbered from 3000 to 3999), run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command.
        2. Run either of the following commands to create an ACL rule:
           + For a basic ACL (numbered from 2000 to 2999), run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **logging** ] \* command.
           + For an advanced ACL (numbered from 3000 to 3999), run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **tcp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | { **destination-port** *operator* *port-number* | **destination-port-pool** *destination-port-pool-name* } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | { **source-port** *operator* *port-number* | **source-port-pool** *source-port-pool-name* } | { **tcp-flag** | **syn-flag** } { *tcp-flag* [ **mask** *mask-value* ] | **established** |{ **ack** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **fin** [ **ack** | **psh** | **rst** | **syn** | **urg** ] \* } | { **psh** [ **fin** | **ack** | **rst** | **syn** | **urg** ] \* } | { **rst** [ **fin** | **psh** | **ack** | **syn** | **urg** ] \* } | { **syn** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **urg** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **ttl** *ttl-operation* *ttl-value* | **packet-length** *length-operation* *length-value* ] \* command as required by the protocol. The preceding configuration uses TCP as the example protocol. The configurations of the other protocols are similar. For details, see the **rule (Advanced ACL view) (UDP)**, **rule (Advanced ACL view) (gre-igmp-ip-ipinip-ospf)** and **rule (Advanced ACL view) (ICMP)** commands.![](../../../../public_sys-resources/note_3.0-en-us.png) 
             
             Generally, source IP addresses are matched against in ACL rules. To specify multiple ACL rules, repeat Step [2.b](#EN-US_TASK_0317488797__li6412727123917).
             
             Rules in an ACL are used based on the depth first principle (with **auto** configured) or based on the configuration order (with **config** configured).
             
             When you associate an ACL rule with an instance, the address wildcard of the rule must use a subnet mask that has consecutive 1s and then consecutive 0s (e.g., 255.255.255.0). Do not use a subnet mask that has 0s and 1s mixed up, like 255.0.255.0.
        3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
        4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     2. Configure a traffic classifier.
        1. Run the [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ] command to configure a traffic classifier and enter its view.
        2. Run the [**if-match acl**](cmdqueryname=if-match+acl) *acl-number* command to configure an ACL-based matching rule for MF traffic classification.
           
           To configure multiple ACL-based matching rules, repeat this step.
        3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
        4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     3. Configure a traffic behavior.
        1. Run the [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name* command to configure a traffic behavior and enter its view.
        2. Run the [**remark network-slice**](cmdqueryname=remark+network-slice) *sliceld* command to configure 5-tuple-based ACL matching for slice ID association.
        3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
        4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Apply the traffic policy.
        1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
        2. Run the [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound** command to apply the traffic policy to the interface.
        3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.