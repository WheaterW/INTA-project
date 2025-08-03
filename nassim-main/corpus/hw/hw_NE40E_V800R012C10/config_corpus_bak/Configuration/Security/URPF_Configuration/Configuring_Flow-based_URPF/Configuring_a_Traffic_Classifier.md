Configuring a Traffic Classifier
================================

To classify traffic on a network, you need to define traffic classifiers based on information such as ACL rules, IP precedence, MAC addresses, and protocol addresses.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
   
   
   
   A traffic classifier is defined and its view is displayed.
   
   
   
   The traffic classifier specified by *classifier-name* cannot be a pre-defined one in the system. You can directly use the pre-defined traffic classifiers when defining traffic policies. For details about traffic classifiers, see HUAWEI NE40E-M2 series Universal Service Router Configuration > QoS.
3. Configure matching rules based on the actual networking.
   
   
   * To define a matching rule to classify traffic based on the 802.1p priority in a VLAN packet, run the [**if-match 8021p**](cmdqueryname=if-match+8021p) *8021p-value* command.
   * To define ACL rules, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* } command.
   * To define rules for matching all packets, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **any** command.
   * To define a matching rule to classify traffic based on the destination MAC address of packets, run the [**if-match destination-mac**](cmdqueryname=if-match+destination-mac) *mac-address* command.
   * To define a matching rule to classify traffic based on the destination IPv6 address, run the [**if-match ipv6 destination-address**](cmdqueryname=if-match+ipv6+destination-address) *ipv6-address* *prefix-length* command.
   * To define a rule to match traffic with a specified DSCP value, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **dscp** *dscp-value* command.
   * To define a matching rule to classify traffic based on the MPLS EXP value, run the [**if-match mpls-exp**](cmdqueryname=if-match+mpls-exp) *exp-value* command.
   * To define a matching rule to classify traffic based on the IP precedence, run the [**if-match ip-precedence**](cmdqueryname=if-match+ip-precedence) *ip-precedence* command.
   * To define a matching rule to classify traffic based on the source MAC address of packets, run the [**if-match source-mac**](cmdqueryname=if-match+source-mac) *mac-address* command.
   * To define a matching rule to classify traffic based on the IPv4 TCP flag value, run the [**if-match tcp syn-flag**](cmdqueryname=if-match+tcp+syn-flag) { *tcpflag-value* [ **mask** *tcpflag-mask* ] | **bit-match** { **established** | **fin** | **syn** | **rst** | **psh** | **ack** | **urg** | **ece** | **cwr** | **ns** } } command.
   * To define a matching rule for MF classification based on the SYN Flag value in the IPv6 TCP header, run the [**if-match ipv6 tcp syn-flag**](cmdqueryname=if-match+ipv6+tcp+syn-flag) { *tcpflag-value* [ **mask** *tcpflag-mask* ] | **bit-match** { **established** | **fin** | **syn** | **rst** | **psh** | **ack** | **urg** } } command.
   
   For details about traffic classifiers, see HUAWEI NE40E-M2 series Universal Service Router Configuration > QoS. You can select one or more matching rules as required.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.