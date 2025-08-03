Layer 2 Multicast
=================

This section describes security policies, attack methods, configuration and maintenance methods, and configuration and maintenance suggestions for Layer 2 multicast.

#### Security Policy Overview

* In Layer 2 multicast, group policies can be set to restrict the access of multicast groups (multicast source groups) to a VLAN or an interface.
* In Layer 2 multicast, IP policies can be set based on the source IP address to restrict the access of source IP addresses to a VLAN or VSI. Here the source IP address refers to the one carried in the IP header, that is, the host IP address.
* In Layer 2 multicast, you can configure ports not to be learned through protocol messages.

#### Attack Methods

A network can be attacked by forged IGMP/MLD messages. You can configure a multicast group policy or source policy to discard forged IGMP/MLD messages. The possible attack methods are as follows:

* Malicious users send join requests with changed multicast group addresses over invalid multicast group channels. Consequently, many invalid entries are generated on the device, consuming a large number of system resources. As a result, program requests of authorized users cannot succeed. In this case, you can set a multicast group policy to specify the range of multicast groups that users can join.
* Attacks are launched through packets with changed user source IP addresses. In this case, a source IP address-based policy can be set to limit the range of valid source IP addresses.
* Attacks are conducted through Query messages. A multicast port is configured on the device to receive traffic from all multicast groups. As a result, a large amount of traffic is sent over this port and this consumes interface bandwidth. To resolve this problem, configure static ports and configure ports not to be learned through protocol messages.

#### Configuration and Maintenance Methods

* To set a multicast group policy for a VLAN or VSI, run the [**igmp-snooping group-policy**](cmdqueryname=igmp-snooping+group-policy) command.
* To set a source IP address-based policy for a VLAN or VSI, run the [**igmp-snooping ip-policy**](cmdqueryname=igmp-snooping+ip-policy) command.
* To prevent Router ports from being learned through protocol messages for a VLAN or VSI, run the [**undo igmp-snooping router-learning**](cmdqueryname=undo+igmp-snooping+router-learning) command.
* To set an IPv6 multicast group policy for a VLAN or VSI, run the [**mld-snooping group-policy**](cmdqueryname=mld-snooping+group-policy) command.
* To set an IPv6 source IP address-based policy for a VLAN or VSI, run the [**mld-snooping ip-policy**](cmdqueryname=mld-snooping+ip-policy) command.
* To disable IPv6 Router port learning for a VLAN or VSI, run the [**undo mld-snooping router-learning**](cmdqueryname=undo+mld-snooping+router-learning) command.

#### Configuration and Maintenance Suggestions

Based on service deployment, you are recommended to configure group policies for VLANs or VSIs based on the IPTV multicast group address range.

* Configure an IGMP snooping group policy in the VLAN or VSI view using the [**igmp-snooping group-policy**](cmdqueryname=igmp-snooping+group-policy) *acl-number* command.
* Specify the IPTV group range in the ACL 2000 view using the [**rule**](cmdqueryname=rule) [ *rule-id* ] { **deny** | **permit** } **source** *source-ip-address* *source-wildcard* command.
* For IPv6 Layer 2 multicast, run the [**mld-snooping group-policy**](cmdqueryname=mld-snooping+group-policy) *acl6-number* command in the VLAN or VSI view.
* For IPv6 Layer 2 multicast, configure the IPTV group range in the ACL6 2000 view, run the [**rule**](cmdqueryname=rule) [ *rule-id* ] { **deny** | **permit** } **source** *source-ipv6-address* *source-wildcard* command.

#### Verifying the Security Hardening Result

* Run the [**display igmp-snooping**](cmdqueryname=display+igmp-snooping) [ **vlan** [ *vlan-id* ] | **vsi** [ *vsi-name* ] ] **configuration** command to check the IGMP snooping configuration.
* Run the [**display igmp-snooping**](cmdqueryname=display+igmp-snooping) [ **vlan** [ *vlan-id* ] | **vsi** [ *vsi-name* ] ] command to check IGMP snooping running parameters.
* Run the [**display igmp-snooping router-port**](cmdqueryname=display+igmp-snooping+router-port) [ **vlan** [ *vlan-id* ] | **vsi** [ *vsi-name* ] ] command to check port information of the IGMP snooping device.
* Run the [**display mld-snooping**](cmdqueryname=display+mld-snooping) [ **vlan** [  *vlan-id* ] | **vsi** [  *vsi-name* ]] **configuration** command to check the MLD snooping configuration.
* Run the [**display mld-snooping**](cmdqueryname=display+mld-snooping) [ **vlan** [  *vlan-id* ] | **vsi** [  *vsi-name* ]] command to check MLD snooping running parameters.
* Run the [**display mld-snooping router-port**](cmdqueryname=display+mld-snooping+router-port) [ **vlan** [  *vlan-id* ] | **vsi** [  *vsi-name* ]] command to check port information of the MLD snooping device.