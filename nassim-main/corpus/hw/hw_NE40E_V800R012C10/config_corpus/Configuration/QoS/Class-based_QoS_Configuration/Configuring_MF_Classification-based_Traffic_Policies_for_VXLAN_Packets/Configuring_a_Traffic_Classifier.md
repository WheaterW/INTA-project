Configuring a Traffic Classifier
================================

You need to configure a traffic classifier before configuring class-based QoS. The traffic classifier can be configured based on the ACL rule, IP precedence, and so on.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
   
   
   
   A traffic classifier is defined and its view is displayed.
   
   
   
   If you define multiple matching rules in a traffic classifier, you can set the logical relationship between the matching rules by specifying the **operator** parameter.
   
   * **and**: A packet belongs to the classifier only when it matches all the rules.
   * **or**: A packet belongs to the classifier if it matches any one of the rules.
3. Define matching rules for the traffic classifier as required.
   
   
   * To define a matching rule based on an ACL, run the [**if-match**](cmdqueryname=if-match) **acl** { *acl-number* | **name** *acl-name* } [ **precedence** *precedence-value* ] command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the [**rule**](cmdqueryname=rule) [ *rule-id* ] { **deny** | **permit** } { *protocol* | **udp** } **vxlan** **vni** *vni* and [**rule**](cmdqueryname=rule) [ *rule-id* ] { **deny** | **permit** } *protocol* [ **packet-length** *length-operation length-value* ] commands are configured for an advanced ACL, the rules that can be configured will be reduced.
     
     ACL rules can be defined based on different parameters, such as the protocol type, source address, destination address, and the precedence field in packets. Packets are matched against rules configured using the **rule** command in the **if-match acl** configuration, and traffic behaviors are performed for the matching packets.
   * To define a matching rule based on a DSCP value, run the [**if-match**](cmdqueryname=if-match) **dscp** { *dscp-value* | **af11** | **af12** | **af13** | **af21** | **af22** | **af23** | **af31** | **af32** | **af33** | **af41** | **af42** | **af43** | **cs1** | **cs2** | **cs3** | **cs4** | **cs5** | **cs6** | **cs7** | **ef** | **default** } command.
   * To define a matching rule based on an IP precedence, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **ip-precedence** *ip-precedence* command.
   * To define a matching rule to match all packets, run the [**if-match**](cmdqueryname=if-match) **any** command.