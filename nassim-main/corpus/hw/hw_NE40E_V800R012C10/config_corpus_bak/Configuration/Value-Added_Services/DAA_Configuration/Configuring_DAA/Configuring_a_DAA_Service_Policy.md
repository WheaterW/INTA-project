Configuring a DAA Service Policy
================================

This section describes how to configure a DAA service policy.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Configure a DAA traffic policy and globally apply it.
   1. Run the [**acl**](cmdqueryname=acl) { **name** *ucl-acl-name* [ **ucl** | [ **ucl** ] **number** *ucl-acl-number* ] | [ **number** ] *ucl-acl-number* } [ **match-order** { **auto** | **config** } ] command to create an ACL and enter the ACL view.
   2. Run the corresponding command to create an ACL rule based on the protocol type.
      
      
      
      **Table 1** Creating an ACL rule
      | Protocol Type | Command |
      | --- | --- |
      | TCP | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **tcp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **source-port** *operator* *port-number* | **destination-port** *operator* *port-number* | **syn-flag** { *syn-flag* [ **mask** *mask-value* ] | { **bit-match** { **established** | **fin** | **syn** | **rst** | **psh** | **ack** | **urg** | **ece** | **crw** | **ns** } } } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **time-range** *time-name* | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \* |
      | UDP | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **source-port** *operator* *port-number* | **destination-port** *operator* *port-number* | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **time-range** *time-name* | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \* |
      | ICMP | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **icmp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **icmp-type** { *icmp-name* | *icmp-type* *icmp-code* } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **time-range** *time-name* | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \* |
      | Other protocols | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { **zero** | *protocol* | **gre** | **ip** | **ipinip** | **igmp** | **ospf** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **time-range** *time-name* | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \* |
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. (Optional) Run the [**acl ipv6**](cmdqueryname=acl+ipv6) **number** *ucl-acl6-number* [ **match-order** { **auto** | **config** } ] command to create an ACL6 and enter its view.
   6. (Optional) Run the corresponding command to create an ACL6 rule based on the protocol type.
      
      
      
      **Table 2** Creating an ACL6 rule
      | Protocol Type | Command |
      | --- | --- |
      | TCP | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { *protocol* | **tcp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **destination-port** *operator* *port* | **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } **source-pool** *source-pool-name* } | **source-port** *operator* *port* | **tcp-flag** { *tcp-flag* [ **mask** *mask-value* ] | **established** | { **ack** | **fin** | **psh** | **rst** | **syn** | **urg** } \* } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* |
      | UDP | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **destination-port** *operator* *port* | **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } **source-pool** *source-pool-name* } | **source-port** *operator* *port* | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* |
      | ICMPv6 | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { *protocol* | **icmpv6** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **fragment** | **icmp6-type** { *icmp6-type-name* | *icmp6-type* [ **to** *icmp6-type-end* ] [ *icmp6-code* ] } | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } **source-pool** *source-pool-name* } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* |
      | Other protocols | [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **hoport** [ **option-code** *option-value* ] | **1** | **5** | *protocol* | **gre** | **ipv6** | **ipv6-frag** | **ipv6-ah** | **ipv6-esp** | **ospf** | *7-16* | *18-42* | { *43* | **ipv6-routing** } [ **routing-type** *routing-number* ] | *44-57* | *59* | { *60* | **ipv6-destination** } [ **option-code** *option-value* ] | *61-255* } [ **destination** { *destination-ipv6-address* *prefix-length* | *dest-ipv6-addr-prefix* | **any** } | **fragment** | { **source** { *source-ipv6-address* *prefix-length* | *src-ipv6-addr-prefix* | **any** } | **source-pool** *source-pool-name* } | **time-range** *time-name* | [ **dscp** *dscp* | [ **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } | **tos** { *tos* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } ] \* ] | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* |
   7. (Optional) Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   8. (Optional) Run the [**quit**](cmdqueryname=quit) command to return to the system view.
3. Configure a traffic classifier.
   1. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is configured and the traffic classifier view is displayed.
   2. Run [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* }
      
      
      
      The traffic classifier references a specified ACL or ACL6.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Configure a traffic behavior.
   1. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
      
      
      
      A traffic behavior is configured and the traffic behavior view is displayed.
   2. Run the [**tariff-level**](cmdqueryname=tariff-level) *tariff-level* command to configure a DAA tariff level.
   3. Run the [**car**](cmdqueryname=car) command to configure DAA traffic policing for the traffic behavior.
   4. Run the [**traffic-statistic**](cmdqueryname=traffic-statistic) command to enable traffic statistics collection for DAA services.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
5. Define a DAA traffic policy.
   1. Run the [**traffic policy**](cmdqueryname=traffic+policy) *policy-name* command to configure a DAA traffic policy and enter its view.
   2. Run the [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* ] command to specify a traffic behavior for the traffic classifier in the DAA traffic policy. *classifier-name* and *behavior-name* specify the configured traffic classifier and traffic behavior, respectively.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. Run the [**accounting-service-policy**](cmdqueryname=accounting-service-policy) *policy-name* command to globally apply the DAA traffic policy.
6. Configure a DAA service policy.
   
   
   
   **Table 3** Procedure for configuring a DAA service policy
   | Objective | Task | Description |
   | --- | --- | --- |
   | Create a DAA service policy and enter the DAA service policy view. | Run the [**value-added-service policy**](cmdqueryname=value-added-service+policy) *service-policy-name* **daa** command. | Mandatory.  Creating a DAA service policy and entering its view are the prerequisites for performing the following operations. |
   | Configure an accounting scheme for the DAA service policy | Run the [**accounting-scheme**](cmdqueryname=accounting-scheme) *accounting-scheme-name* command. | Mandatory.  After an accounting scheme template is referenced by a value-added service policy template, the service uses the accounting scheme in the accounting scheme template.  An accounting scheme can be configured either in a domain or in a DAA service policy template. The priority of an accounting scheme configured in a DAA service policy template is higher than that configured in a domain. |
   | Enable uniform accounting for DAA services. | Run the [**accounting-together enable**](cmdqueryname=accounting-together+enable) command. | Optional.  When users access network services with different bandwidth requirements, such as gaming, FTP, and VoD services, these network services are planned as different DAA services for rate limiting. Configure uniform accounting so that the device interacts with the accounting server to implement traffic reporting and service quota management. |
   | In non-uniform accounting mode, if the monitoring key delivered by the Diameter server is in string format, configure the mapping between the tariff level and the monitoring key in string format for DAA services. | Run the [**tariff-level**](cmdqueryname=tariff-level) *level* **monitor-key string** *monitor-key-string* command. | Optional.  In non-uniform accounting mode, different quotas are delivered for DAA services at different tariff levels. Therefore, different monitor keys must be configured for such services.  Before running this command, run the [**diameter monitor-key parse-mode**](cmdqueryname=diameter+monitor-key+parse-mode) **string** command in the system view to set the parsing mode of the Diameter monitor key to string. |
   | In uniform accounting mode, if the monitor key delivered by the Diameter server is in string format, configure a monitor key for the DAA service policy. | Run the [**diameter monitor-key string**](cmdqueryname=diameter+monitor-key+string) *monitor-key-string* command. | Optional.  In uniform accounting mode, accounting is performed for DAA services at different tariff levels in a uniform manner. As such, only one monitor key needs to be configured so that the corresponding quota takes effect.  Before running this command, run the [**diameter monitor-key parse-mode**](cmdqueryname=diameter+monitor-key+parse-mode) **string** command in the system view to set the parsing mode of the Diameter monitor key to string. |
   | Configure the QoS resource type requested by downstream DAA services. | Run the [**rate-limit-mode**](cmdqueryname=rate-limit-mode) command. | Optional.  If CAR is performed on DAA service traffic and then the traffic is re-marked with different priorities, the traffic enters the subscriber queue (SQ) for scheduling. When an eTM subcard is used, you need to run the [**rate-limit-mode**](cmdqueryname=rate-limit-mode) **car** **outbound** command to set the QoS rate limiting mode to CAR for downstream DAA services. |
   | Configure DAA user traffic to match a DAA service policy. | Run the [**accounting-service-policy**](cmdqueryname=accounting-service-policy) { **inbound** | **outbound** } { **auto** | **disable** | **enable** } command. | Optional.  To implement refined control on DAA services and save QoS resources, for example, to enable only downstream service matching for users, run the [**accounting-service-policy**](cmdqueryname=accounting-service-policy) **inbound** **disable** command in a DAA service policy to disable upstream service matching for DAA users who use this service policy. This prevents DAA users from applying for upstream QoS resources. |
   | Enable rate limit separation for DAA services. | Run the [**traffic-separate enable**](cmdqueryname=traffic-separate+enable) command. | Optional.  After rate limit separation is enabled for DAA services in a DAA service policy template, the service traffic bandwidth of DAA users using this template is no longer limited by the user bandwidth. |
   | Enable DAA service traffic to be counted into user traffic. | Run the [**user accounting-together enable**](cmdqueryname=user+accounting-together+enable) command. | Optional.  You can run this command to count DAA user service traffic into user traffic. |
   | Configure separate traffic statistics collection for dual-stack DAA users based on user queues. | Run the [**user accounting dual-stack separate user-queue**](cmdqueryname=user+accounting+dual-stack+separate+user-queue) command. | Optional.  When CAR-based rate limiting is performed for DAA services and SQs are configured to limit user rates, statistics based on count IDs are not performed for traffic after CAR-based rate limiting if the [**traffic-separate enable**](cmdqueryname=traffic-separate+enable) command is run to configure DAA service separation. In this situation, separate traffic statistics are collected for dual-stack DAA users. As a result, user service traffic cannot be counted into DAA service traffic. To collect separate traffic statistics for dual-stack DAA users based on user queues, run the [**user accounting dual-stack separate user-queue**](cmdqueryname=user+accounting+dual-stack+separate+user-queue) command. |
   | Configure the accounting status or IP type for a specified DAA tariff level. | Run the [**tariff-level-cfg**](cmdqueryname=tariff-level-cfg) *level* { **accounting off** | **ip-type ipv6** } command. | Optional.  DAA service traffic statistics are collected and reported based on the IP type configured for each level, which is irrelevant to the traffic type that actually matches the specific level. Therefore, when deploying dual-stack DAA services, you need to ensure that the ACL type of each service is consistent with the IP type configured for the DAA tariff level to prevent IPv4 and IPv6 traffic from matching the same level. |
   | Configure a tariff level and a QoS profile for DAA services | Run the [**tariff-level**](cmdqueryname=tariff-level) *level* **qos-profile** *qos-profile-name* command. | Mandatory.  To limit the rate of DAA users based on parameters in the QoS profile corresponding to a DAA tariff level, run this command. |
   | Configure the user group to be bound to a service policy. | Run the [**user-group**](cmdqueryname=user-group) *user-group-name* command. | Mandatory.  Reference an ACL user group to the value-added service template.  NOTE:  * You can configure a user group using any of the following methods:   + Configure a user group in a domain.   + Configure a user group using a DAA service policy template.   + Deliver a user group through the RADIUS server. The user group configured using a DAA service policy template has the highest priority, followed by the one delivered by the RADIUS server, and then the one configured in a domain. * The DAA service tariff level used by users must be the same as the DAA ACL tariff level planned for the user group to which the users belong. |
7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
8. (Optional) Run the [**radius-server coa-request hw-policy-name daa same-policy reply-ack**](cmdqueryname=radius-server+coa-request+hw-policy-name+daa+same-policy+reply-ack) command to enable the device to respond with an ACK message when the RADIUS server delivers the same DAA service policy as that in the domain using the HW-Policy-Name (26-95) attribute in a CoA message in uniform accounting scenarios.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command can take effect only after the [**accounting-together enable**](cmdqueryname=accounting-together+enable) command is run.
9. (Optional) Run the [**radius-server coa-request hw-policy-name daa coexist-with-user**](cmdqueryname=radius-server+coa-request+hw-policy-name+daa+coexist-with-user) command to allow both the HW-Policy-Name (26â95) attribute (DAA value-added service attribute) and other user attributes in a CoA message to take effect at the same time.
10. (Optional) Run the **[**value-added-service tariff-queue-mapping**](cmdqueryname=value-added-service+tariff-queue-mapping)** { [ **cs7** ] | [ **cs6** ] | [ **ef** ] | [ **af4** ] | [ **af3** ] | [ **af1** ] | [ **be** ] | [ **af2** ] } #*8-8* command to configure the mapping between DAA tariff levels and flow queues.
11. (Optional) Run the [**value-added-service quota-out**](cmdqueryname=value-added-service+quota-out) { **online** | **offline** } command to configure a policy for the scenario where the real-time accounting response packet sent after the DAA accounting service quota is exhausted does not carry a new quota.
12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.