Configuring a Timestamp-Refresh Traffic Policy
==============================================

After a timestamp-refresh instance is created, you can configure a traffic behavior and bind it to the timestamp-refresh instance in the traffic behavior view. After the traffic policy is applied to the inbound interface of multicast streams, input multicast streams are associated with the timestamp-refresh instance.

#### Prerequisites

Before configuring a traffic policy for a timestamp-refresh instance, ensure that this instance has been created.


#### Context

To associate input multicast streams with a timestamp-refresh instance, you need to apply a traffic policy to the inbound interface of the multicast streams. You can configure a single-level or two-level traffic policy as required.

* Single-level traffic policy: matches the IP address and UDP port number of input multicast streams.
* Two-level traffic policy: The level-1 traffic policy matches the MAC address of input multicast streams, and the level-2 traffic policy matches the IP address and UDP port number of input multicast streams.

#### Procedure

* Configure a single-level traffic policy.
  1. Configure a traffic classification rule.
     
     
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command to create an advanced ACL and enter the corresponding ACL view.
     3. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | { **destination-port** *operator* *port-number* | **destination-port-pool** *destination-port-pool-name* } | **fragment-type** **fragment** | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | { **source-port** *operator* *port-number* | **source-port-pool** *source-port-pool-name* } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \* command to configure a rule for the advanced ACL to match the IP address and UDP port number of input multicast streams.
     4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  2. Configure a traffic classifier.
     
     
     1. Run the [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* command to define a traffic classifier and enter the traffic classifier view.
     2. Run the [**if-match acl**](cmdqueryname=if-match+acl) **name** *acl-name* command to configure an ACL-based matching rule for MF traffic classification.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  3. Configure a traffic behavior.
     
     
     1. Run the [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name* command to configure a traffic behavior and enter its view.
     2. Run the [**multicast timestamp-refresh bind instance**](cmdqueryname=multicast+timestamp-refresh+bind+instance)*i**nstance-name* command to bind the traffic behavior to the timestamp-refresh instance.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  4. Configure a traffic policy.
     
     
     1. Run the [**traffic policy**](cmdqueryname=traffic+policy) *policy-name* command to configure a traffic policy and enter the traffic policy view.
     2. Run the [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* command to specify the traffic behavior for the traffic classifier in the traffic policy.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a two-level traffic policy.
  1. Configure a level-1 traffic classification rule.
     
     
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**acl**](cmdqueryname=acl) { **name** *link-acl-name* { **link** | [ **link** ] **number** *link-acl-number* } | [ **number** ] *link-acl-number* } [ **match-order** { **config** | **auto** } ] command to create a Layer 2 ACL and enter the Layer 2 ACL view.
     3. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] **permit** **source-mac** *source-mac* *sourcemac-mask* command to configure a rule for the ACL to match the MAC address of input multicast streams.
     4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  2. Configure a level-1 traffic classifier.
     
     
     1. Run the [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* command to define a traffic classifier and enter the traffic classifier view.
     2. Run the [**if-match acl**](cmdqueryname=if-match+acl) **name** *acl-name* command to configure an ACL-based matching rule for MF traffic classification.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  3. Configure a level-2 traffic classification rule.
     
     
     1. Run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command to create an advanced ACL and enter the corresponding ACL view.
     2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | { **destination-port** *operator* *port-number* | **destination-port-pool** *destination-port-pool-name* } | **fragment-type** **fragment** | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | { **source-port** *operator* *port-number* | **source-port-pool** *source-port-pool-name* } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \* command to configure a rule for the advanced ACL to match the IP address and UDP port number of input multicast streams.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  4. Configure a level-2 traffic classifier.
     
     
     1. Run the [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* command to define a traffic classifier and enter the traffic classifier view.
     2. Run the [**if-match acl**](cmdqueryname=if-match+acl) **name** *acl-name* command to configure an ACL-based matching rule for MF traffic classification.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  5. Configure a level-2 traffic behavior.
     
     
     1. Run the [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name* command to configure a traffic behavior and enter its view.
     2. Run the [**multicast timestamp-refresh bind instance**](cmdqueryname=multicast+timestamp-refresh+bind+instance)*i**nstance-name* command to bind the traffic behavior to the timestamp-refresh instance.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  6. Configure a level-2 traffic policy.
     
     
     1. Run the [**traffic policy**](cmdqueryname=traffic+policy) *policy-name* command to configure a traffic policy and enter the traffic policy view.
     2. Run the [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* command to specify the traffic behavior for the traffic classifier in the traffic policy.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  7. Configure a level-1 traffic behavior.
     
     
     1. Run the [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name* command to configure a traffic behavior and enter its view.
     2. Run the [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* [ **ip-layer** ] command to associate this traffic behavior with the level-2 traffic policy.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  8. Configure a level-1 traffic policy.
     
     
     1. Run the [**traffic policy**](cmdqueryname=traffic+policy) *policy-name* command to configure a traffic policy and enter the traffic policy view.
     2. Run the [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* command to specify the traffic behavior for the traffic classifier in the traffic policy.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.