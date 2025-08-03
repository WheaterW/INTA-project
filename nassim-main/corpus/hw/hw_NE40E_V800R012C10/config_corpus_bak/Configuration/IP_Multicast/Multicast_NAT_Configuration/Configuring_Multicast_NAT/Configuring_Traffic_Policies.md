Configuring Traffic Policies
============================

To implement multicast NAT, you must configure traffic policies to match input multicast streams.

#### Context

In multicast NAT, input and output multicast streams are associated through a multicast NAT instance. To associate input multicast streams with a multicast NAT instance, traffic policies need to be applied on the inbound interface of multicast streams. You can configure a single-level or two-level traffic policy as required.

* Single-level traffic policy: matches the IP address and UDP port number of input multicast streams.
* Two-level traffic policy: The level-1 traffic policy matches the MAC address of input multicast streams, and the level-2 traffic policy matches the IP address and UDP port number of input multicast streams.

#### Procedure

* Configure a single-level traffic policy.
  1. Configure a traffic classification rule.
     
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        An advanced ACL is created, and the ACL view is displayed.
     3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | { **destination-port** *operator* *port-number* | **destination-port-pool** *destination-port-pool-name* } | **fragment-type** **fragment** | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | { **source-port** *operator* *port-number* | **source-port-pool** *source-port-pool-name* } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
        
        A rule is configured for the advanced ACL to match the IP address and UDP port number of input multicast streams.
     4. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  2. Configure a traffic classifier.
     
     
     1. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name*
        
        A traffic classifier is configured, and the traffic classifier view is displayed.
     2. Run [**if-match acl**](cmdqueryname=if-match+acl) **name** *acl-name*
        
        An ACL-based matching rule for MF traffic classification is configured.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  3. Configure a traffic behavior.
     
     
     1. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
        
        A traffic behavior is configured, and its view is displayed.
     2. Run [**multicast-nat bind instance**](cmdqueryname=multicast-nat+bind+instance) **id** *instance-id* [ **name** *instance-name* ]
        
        The traffic behavior is bound to the multicast NAT instance.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  4. Configure a traffic policy.
     
     
     1. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
        
        A traffic policy is configured and its view is displayed.
     2. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
        
        The traffic behavior is specified for the traffic classifier in the traffic policy.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
* Configure a two-level traffic policy.
  1. Configure a level-1 traffic classification rule.
     
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**acl**](cmdqueryname=acl) { **name** *link-acl-name* { **link** | [ **link** ] **number** *link-acl-number* } | [ **number** ] *link-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        A Layer 2 ACL is created, and the Layer 2 ACL view is displayed.
     3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] **permit** **source-mac** *source-mac* *sourcemac-mask*
        
        An ACL rule is configured to match a specified MAC address of input multicast streams.
     4. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  2. Configure a level-1 traffic classifier.
     
     
     1. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name*
        
        A traffic classifier is configured, and the traffic classifier view is displayed.
     2. Run [**if-match acl**](cmdqueryname=if-match+acl) **name** *acl-name*
        
        An ACL-based matching rule for MF traffic classification is configured.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  3. Configure a level-2 traffic classification rule.
     
     
     1. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        An advanced ACL is created, and the ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | { **destination-port** *operator* *port-number* | **destination-port-pool** *destination-port-pool-name* } | **fragment-type** **fragment** | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | { **source-port** *operator* *port-number* | **source-port-pool** *source-port-pool-name* } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
        
        A rule is configured for the advanced ACL to match the IP address and UDP port number of input multicast streams.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  4. Configure a level-2 traffic classifier.
     
     
     1. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name*
        
        A traffic classifier is configured, and the traffic classifier view is displayed.
     2. Run [**if-match acl**](cmdqueryname=if-match+acl) **name** *acl-name*
        
        An ACL-based matching rule for MF traffic classification is configured.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  5. Configure a level-2 traffic behavior.
     
     
     1. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
        
        A traffic behavior is configured, and its view is displayed.
     2. Run [**multicast-nat bind instance**](cmdqueryname=multicast-nat+bind+instance) **id** *instance-id* [ **name** *instance-name* ]
        
        The traffic behavior is bound to the multicast NAT instance.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  6. Configure a level-2 traffic policy.
     
     
     1. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
        
        A traffic policy is configured and its view is displayed.
     2. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
        
        The traffic behavior is specified for the traffic classifier in the traffic policy.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  7. Configure a level-1 traffic behavior.
     
     
     1. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
        
        A traffic behavior is configured, and its view is displayed.
     2. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* [ **ip-layer** ]
        
        The traffic behavior is associated with the level-2 traffic policy.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  8. Configure a level-1 traffic policy.
     
     
     1. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
        
        A traffic policy is configured and its view is displayed.
     2. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
        
        The traffic behavior is specified for the traffic classifier in the traffic policy.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.