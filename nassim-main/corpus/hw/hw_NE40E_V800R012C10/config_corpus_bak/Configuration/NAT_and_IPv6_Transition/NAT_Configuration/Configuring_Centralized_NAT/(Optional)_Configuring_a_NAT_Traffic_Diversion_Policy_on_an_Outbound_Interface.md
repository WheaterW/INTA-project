(Optional) Configuring a NAT Traffic Diversion Policy on an Outbound Interface
==============================================================================

You can configure a NAT traffic diversion policy on an outbound interface so that traffic destined for the public network matches the NAT policy.

#### Context

The Router is deployed on the egress of an enterprise network, whereas NAT does not need to be performed for a great amount of traffic transmitted within the enterprise network. To prevent an inbound interface from enforcing a NAT traffic policy that directs intra-enterprise network traffic to a NAT service board for NAT processing, the NAT traffic policy can be configured on an outbound interface connected to a public network. This enables the device to match traffic only destined for a public network against the NAT traffic policy.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a traffic classification rule.
   1. Run either of the following commands to create an ACL and enter the ACL view:
      
      
      * For a basic ACL (numbered from 2000 to 2999), run the [**acl**](cmdqueryname=acl+name+basic+basic+number+number+match-order+config+auto) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command.
      * For an advanced ACL (numbered from 3000 to 3999), run the [**acl**](cmdqueryname=acl+name+advance+advance+number+number+match-order+config+auto) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command.
   2. Run either of the following commands to create an ACL rule:
      
      
      * For a basic ACL (numbered from 2000 to 2999), run the following command:
        
        [**rule**](cmdqueryname=rule+name+deny+permit+fragment-type+fragment+non-fragment) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **logging** ] \*
      * For an advanced ACL (numbered from 3000 to 3999), run the following command as required by the protocol type:
        
        [**rule**](cmdqueryname=rule+name+deny+permit+tcp+dscp+precedence+tos+destination+0+any) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **tcp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | { **destination-port** *operator* *port-number* | **destination-port-pool** *destination-port-pool-name* } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | { **source-port** *operator* *port-number* | **source-port-pool** *source-port-pool-name* } | { **tcp-flag** | **syn-flag** } { *tcp-flag* [ **mask** *mask-value* ] | **established** |{ **ack** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **fin** [ **ack** | **psh** | **rst** | **syn** | **urg** ] \* } | { **psh** [ **fin** | **ack** | **rst** | **syn** | **urg** ] \* } | { **rst** [ **fin** | **psh** | **ack** | **syn** | **urg** ] \* } | { **syn** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **urg** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } } | **time-range** *time-name* | **ttl** *ttl-operation* *ttl-value* | **packet-length** *length-operation* *length-value* ] \*
        
        The preceding configuration uses TCP as the example protocol. The configurations of the other protocols are similar. For details, see the **rule (Advanced ACL view) (UDP)**, **rule (advanced ACL view) (ICMP)**, and **rule (Advanced ACL view) (gre-igmp-ip-ipinip-ospf)** commands.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      ACL rules usually match against source IP addresses. In each ACL rule, a protocol number, source IP address, destination IP address, source port number, destination port number, VPN instance name, and fragment flag can be specified for matching data flows. The ACL rule requires the consecutive subnet masks whose 0s or 1s must be consecutive, for example, 255.255.255.0.
      
      An ACL configured in the NAT traffic diversion policy on an outbound interface contains multiple ACL rules. The ACL rules are used in ascending order by sequence number to match packets.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Apply the traffic policy to an interface.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The following interfaces are supported: GE main interface and its sub-interfaces; POS interface; Eth-Trunk main interface and its sub-interfaces; Ethernet main interface and its sub-interfaces; IP-Trunk interface; VLANIF interface; serial interfaces, including Trunk-serial interfaces; MP-group interface; tunnel interfaces.
   2. Run [**nat bind acl**](cmdqueryname=nat+bind+acl) { *acl-index* | **name** *acl-name* } [ **mode** **deny-forward** ] **instance** *instance-name*
      
      
      
      The ACL is bound to the NAT instance.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.