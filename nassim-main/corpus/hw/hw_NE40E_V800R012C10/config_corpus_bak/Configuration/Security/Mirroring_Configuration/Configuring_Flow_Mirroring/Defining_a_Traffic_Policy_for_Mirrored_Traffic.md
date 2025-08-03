Defining a Traffic Policy for Mirrored Traffic
==============================================

This section describes how to define a traffic policy for mirrored traffic. It covers configuring a traffic classifier to define the traffic to be mirrored, specifying a traffic behavior, enabling flow mirroring, and defining a traffic policy to associate the traffic classifier with the traffic behavior.

#### Procedure

* Define a traffic classifier.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
     
     
     
     A traffic classifier is defined and its view is displayed.
     
     The classifier name specified by the *classifier-name* parameter cannot be any predefined classifier name in the system. For details about traffic classifiers, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - QoS*.
  3. Define a matching rule according to network requirements.
     
     
     + To define a matching rule for multi-field (MF) classification based on the 802.1p values of VLAN packets, run the [**if-match 8021p**](cmdqueryname=if-match+8021p) *8021p-value* command.
     + To define a matching rule for MF classification based on an IPv4 or IPv6 ACL list, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* } command.
     + To define a matching rule for MF classification of all IPv4 or IPv6 packets, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **any** command.
     + To define a matching rule for MF classification based on the destination MAC addresses of packets, run the [**if-match destination-mac**](cmdqueryname=if-match+destination-mac) *mac-address* command.
     + To define a matching rule for MF classification based on the destination IP addresses of IPv6 packets, run the [**if-match ipv6 destination-address**](cmdqueryname=if-match+ipv6+destination-address) *ipv6-address* *prefix-length* command.
     + To define a matching rule for MF classification based on the source IP addresses of IPv6 packets, run the [**if-match ipv6 source-address**](cmdqueryname=if-match+ipv6+source-address) *ipv6-address* *prefix-length* command.
     + To define a matching rule for MF classification based on the DSCP values of IPv4 or IPv6 packets, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **dscp** *dscp-value* command.
     + To define a matching rule for MF classification based on the EXP values of MPLS packets, run the [**if-match mpls-exp**](cmdqueryname=if-match+mpls-exp) *exp-value* command.
     + To define a matching rule for MF classification based on the preference values of IP packets, run the [**if-match ip-precedence**](cmdqueryname=if-match+ip-precedence) *ip-precedence* command.
     + To define a matching rule for MF classification based on the value of the next IPv6 header, run the [**if-match ipv6 next-header**](cmdqueryname=if-match+ipv6+next-header) *header-number* [**first-next-header**](cmdqueryname=first-next-header) command.
     + To define a matching rule for MF classification based on the source MAC addresses of packets, run the [**if-match source-mac**](cmdqueryname=if-match+source-mac) *mac-address* command.
     + To define a matching rule for MF classification based on the SYN Flag value in the TCP header, run the [**if-match tcp syn-flag**](cmdqueryname=if-match+tcp+syn-flag) { *tcpflag-value* [ **mask** *tcpflag-mask* ] | **bit-match** { **established** | **fin** | **syn** | **rst** | **psh** | **ack** | **urg** | **ece** | **cwr** | **ns** } } command.
     + To define a matching rule for MF classification based on the SYN Flag value in the IPv6 TCP header, run the [**if-match ipv6 tcp syn-flag**](cmdqueryname=if-match+ipv6+tcp+syn-flag) { *tcpflag-value* [ **mask** *tcpflag-mask* ] | **bit-match** { **established** | **fin** | **syn** | **rst** | **psh** | **ack** | **urg** } } command.You can configure one or more matching rules in Step 3 as needed.![](../../../../public_sys-resources/note_3.0-en-us.png) If the device functions as a PE, perform the following operations:
     + To perform MF classification based on the IP layer information of outbound packets on the public network, run the [**traffic-policy match-ip-layer mpls-pop**](cmdqueryname=traffic-policy+match-ip-layer+mpls-pop) command in the slot view.
     + To perform MF classification based on the IP layer information of inbound packets on the public network, run the [**traffic-policy match-ip-layer mpls-push**](cmdqueryname=traffic-policy+match-ip-layer+mpls-push) command in the slot view.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  5. Run [**return**](cmdqueryname=return)
     
     
     
     Return to the user view.
* Define a traffic behavior and enable flow mirroring.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
     
     
     
     A traffic behavior is defined and its view is displayed.
  3. Run [**port-mirroring enable**](cmdqueryname=port-mirroring+enable)
     
     
     
     Flow mirroring is enabled.
  4. (Optional) Run [**port-mirroring car**](cmdqueryname=port-mirroring+car) **cir** *cir-value* [ **pir** *pir-value* ] [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ]
     
     
     
     The CAR function is implemented for mirrored traffic.
  5. (Optional) Run [**port-mirroring slice-size**](cmdqueryname=port-mirroring+slice-size) *slice-size-value*
     
     
     
     The length of packet content to be mirrored is configured.
  6. (Optional) Run [**port-mirroring without-linklayer-header**](cmdqueryname=port-mirroring+without-linklayer-header)
     
     
     
     The mirrored port is configured to mirror packets from their Layer 3 headers.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  8. Run [**return**](cmdqueryname=return)
     
     
     
     Return to the user view.
* Define a traffic policy to associate the traffic classifier with the traffic behavior.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
     
     
     
     A traffic policy is defined and its view is displayed.
  3. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
     
     
     
     A traffic behavior is specified for the traffic classifier in the traffic policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.