Configuring the Limit on Incoming and Outgoing Calls for a VTY User Interface
=============================================================================

An access control list (ACL) can be configured to limit incoming and outgoing calls for a VTY user interface.

#### Context

An ACL can be configured to either allow or deny Telnet connections based on source or destination IP addresses:

* A basic ACL, with its number ranging from 2000 to 2999, controls Telnet connections based on source IP addresses.
* An advanced ACL, with its number ranging from 3000 to 3999, controls Telnet connections based on both source and destination IP addresses.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Compared to a basic ACL that filters packets based on source addresses, an advanced ACL supports richer filtering rules: not based only on packet source addresses but also based on packet destination address or priorities. Run either of the following commands:
   
   
   * For a basic ACL:
     
     To enter the ACL view, run the [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command.
     
     To enter the ACL6 view, run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ] command.
   * For an advanced ACL:
     
     To enter the ACL view, run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command.
     
     To enter the ACL6 view, run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *advance-acl6-name* [ **advance** | [ **advance** ] **number** *advance-acl6-number* ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ] command.
   
   The user interface supports the basic ACL ranging from 2000 to 2999 and the advanced ACL ranging from 3000 to 3999.
3. Run either of the following commands:
   
   
   * For a basic ACL:
     
     To configure a basic ACL rule, run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* command.
     
     To configure a basic ACL6 rule, run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* command.
   * For an advanced ACL:
     
     To configure an advanced ACL rule, run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **gre** | **ip** | **ipinip** | **igmp** | **ospf** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **ttl** *ttl-operation* *ttl-value* | **packet-length** *length-operation* *length-value* ] \* command.
     
     To configure an advanced ACL6 rule, run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **hoport** [ **option-code** *option-value* ] | **1** | **5** | *protocol* | **gre** | **ipv6** | **ipv6-frag** | **ipv6-ah** | **ipv6-esp** | **ospf** | *7-16* | *18-42* | { *43* | **ipv6-routing** } [ **routing-type** *routing-number* ] | *44-57* | *59* | { *60* | **ipv6-destination** } [ **option-code** *option-value* ] | *61-255* } [ **destination** { *destination-ipv6-address* *prefix-length* | *dest-ipv6-addr-prefix* | **any** } | **fragment** | { **source** { *source-ipv6-address* *prefix-length* | *src-ipv6-addr-prefix* | **any** } | **source-pool** *source-pool-name* } | **time-range** *time-name* | [ **dscp** *dscp* | [ **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } | **tos** { *tos* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } ] \* ] | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * By default, the deny action in an ACL rule is taken for all the login user packets. Only users whose source IP addresses match the ACL rule with a permit action can log in to the device.
     
     In the following example, two rules are configured to prohibit users with the IP address 10.1.1.10 from logging in to the device whereas allowing the other users to log in to the device:
     + **rule deny source 10.1.1.10 0**
     + **rule permit source any**If the **rule permit source any** command is not configured, users whose source IP addresses are not 10.1.1.10 will also be prohibited from logging in to the device.
   * If a user's source IP address does not match the ACL rule that allows login, the user is prohibited from logging in to the device.
   * If the ACL referenced by VTY does not contain any rules or does not exist, any user can log in to the device.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
5. Run [**user-interface**](cmdqueryname=user-interface) **vty** *first-ui-number* [ *last-ui-number* ]
   
   
   
   One or more VTY user interface views are displayed.
6. Run [**acl**](cmdqueryname=acl) [ **ipv6** ] { *acl-number* | *acl-name* }{ **inbound** | **outbound** }
   
   
   
   The limit on incoming and outgoing calls is set for the VTY user interfaces.
   
   
   
   * To limit the login of users at a specified IP address or within a specified address range to a router, specify **inbound**.
   * To limit the login of online users to other devices, specify **outbound**.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.