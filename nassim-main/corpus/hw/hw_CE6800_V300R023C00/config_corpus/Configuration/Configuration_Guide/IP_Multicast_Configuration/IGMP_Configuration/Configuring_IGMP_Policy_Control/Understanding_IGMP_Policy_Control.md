Understanding IGMP Policy Control
=================================

IGMP policy control restricts or extends IGMP actions, without affecting IGMP implementation. IGMP policy control includes source address-based IGMP message filtering, range of multicast groups that hosts can join on an IGMP interface, maximum number of IGMP entries, IGMP entries that never time out, IGMP host tracking, and Router-Alert option for IGMP.

#### Source Address-based IGMP Message Filtering

On a multicast network, a device may be attacked by forged IGMP messages, causing it to forward traffic to multicast groups without members. If this is the case, bandwidth resources are wasted. Source address-based IGMP message filtering resolves this problem. The filtering function works as follows for IGMP Report or Leave messages and IGMP Query messages:

* Source address-based IGMP Report or Leave message filtering:
  + The device permits an IGMP Report or Leave message if the message's source address is 0.0.0.0 or an address on the same network segment as the interface that receives the message.
  + If an ACL rule is specified, the device filters out invalid IGMP Report or Leave messages based on the ACL rule.
* Source address-based IGMP Query message filtering: filters IGMP Query messages based on specified ACL rules.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130784216__fig8449353111210), DeviceA is the querier on the network segment, and DeviceA's interface (address 10.0.0.1/24) connects to the host network. HostA sends IGMP Report or Leave messages with the source address 10.1.0.1, HostB sends IGMP Report or Leave messages with the source address 10.0.0.8, and HostC sends IGMP Report or Leave messages with the source address 0.0.0.0. If an ACL rule is not configured, DeviceA permits messages from HostB and HostC, but drops messages from HostA. If an ACL rule is specified, the device forwards or discards IGMP Report or Leave messages based on the ACL rule. For example, if an ACL rule only permits IGMP Report or Leave messages with the source address 10.0.0.8, DeviceA permits such messages from HostB, but drops those from HostC.

**Figure 1** Network diagram of source address-based IGMP Report or Leave message filtering  
![](figure/en-us_image_0000001176663999.png)

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001130784216__fig6450165318127), DeviceA is the querier on the network segment and receives IGMP Report or Leave messages from hosts. If DeviceB constructs bogus IGMP Query messages that contain a smaller IP address (for example, 10.0.0.1/24), DeviceA will become a non-querier and fail to respond to IGMP Leave messages from hosts. In this case, DeviceA continues to forward multicast traffic to hosts who have left, which wastes network resources. To resolve this problem, you can configure an ACL rule on DeviceA to drop IGMP Query messages with the source IP address 10.0.0.1/24.

**Figure 2** Network diagram of source address-based filtering for IGMP Query messages  
![](figure/en-us_image_0000001176743907.png)

#### Range of Multicast Groups that Hosts Can Join on an IGMP Interface

For security or management requirements, a device may not want to receive Report messages or forward multicast data for certain multicast groups. To resolve this problem, you can configure the range of multicast groups that hosts can join on an IGMP interface.

On the network shown in [Figure 3](#EN-US_CONCEPT_0000001130784216__fig_dc_vrp_multicast_feature_201102), HostA and HostB join multicast group G1 (225.1.1.1), and HostC joins multicast group G2 (226.1.1.1). To enable DeviceA to receive and forward data only from G1, configure the range of multicast groups that hosts can join on DeviceA.

**Figure 3** Range of multicast groups that hosts can join on an IGMP interface  
![](figure/en-us_image_0000001176664001.png)

#### Maximum Number of IGMP Entries

If a large number of users watch multiple programs simultaneously, a large amount of bandwidth resources are consumed. As a result, device performance will be degraded, deteriorating the service quality. To prevent this problem, you can configure the maximum number of IGMP entries on the device. When receiving an IGMP Report message from a user, the device first checks whether the number of IGMP entries exceeds the configured maximum number. If no, the device sets up a group membership and forwards data flows of the requested multicast group to the user. This improves the clarity and stability of programs for users who have joined multicast groups. On the network shown in [Figure 4](#EN-US_CONCEPT_0000001130784216__fig_dc_vrp_multicast_feature_201103), assume that the maximum number of IGMP entries configured on DeviceA's interface is 1. If HostA joins the multicast group first, IGMP entries can be created. However, IGMP entries cannot be created for HostB.

**Figure 4** Maximum number of IGMP entries  
![](figure/en-us_image_0000001176743905.png)The implementation mechanism for the maximum number of IGMP entries is as follows:

* IGMP-limit is configured on an interface. After receiving an IGMP Report message from the interface, the device limits the number of IGMP entries on the interface.
* You can configure an ACL rule to exclude certain multicast group ranges or source-specific group ranges from IGMP entry limiting, so that the corresponding IGMP entries are not counted as those on the interface.

The maximum number of IGMP entries complies with the following rules:

* Each (\*, G) entry is counted as one entry on an interface, and each (S, G) is counted as one entry on an interface.
* SSM-mapping (\*, G) entries are not counted as entries on an interface, and each (S, G) entry mapped using the SSM-mapping mechanism is counted as one entry on an interface.


#### IGMP On-Demand

In the standard IGMP working mechanism, a querier periodically sends Query messages and receives Report and Leave messages from members to obtain information about multicast group members. If group memberships on a network are stable, you can configure IGMP on-demand on the querier to reduce the number of exchanged IGMP messages and network traffic. After the function is configured, the querier maintains group memberships based on the requirements of hosts without proactively sending Query messages to collect member states. This reduces the number of IGMP messages exchanged between the querier and hosts.

After IGMP on-demand is configured on an interface:

* The interface does not send IGMP Query messages.
* Group entries are created after the interface receives Report messages, and they will never age out.
* After the interface receives an IGMP Leave message, it immediately deletes the corresponding group entry.

IGMP on-demand is applicable only to IGMPv2 and IGMPv3.


#### IGMP Host Tracking

When a host leaves a multicast group in Layer 3 multicast scenarios, an IGMP querier sends a Group-Specific Query message. If the querier does not receive any response from the host within the specified time, it considers that the host has left the multicast group. While the IGMP querier waits for a response from the host, the multicast device continues to forward multicast traffic to the host. This delays the switching of multicast programs and wastes bandwidth.

To solve this problem, configure the host tracking function. After this function takes effect, the multicast device records the join status of the host. When receiving a Leave message from the host, the multicast device considers that the host has left and does not send a Group-Specific Query message.

Before configuring the host tracking function, you must enable the IGMP function and configure IGMPv3. Host tracking applies only to IGMPv3-enabled interfaces that have IGMPv3 access users only.


#### Router-Alert Option for IGMP

Typically, a network device sends a message to the corresponding protocol module for processing only when the destination address of the message is a local interface address. Because the destination IP address of an IGMP message is usually a multicast address but not the address of an interface on a multicast device, the message may fail to be sent to the routing protocol layer for processing. The Router-Alert option can address such a problem.

Router-Alert is a special mechanism for identifying protocol messages. If a message contains the Router-Alert option, it needs to be sent to the routing protocol layer for processing. In practice, the destination addresses of some protocol messages are multicast addresses or other special addresses. If the messages do not carry the Router-Alert option, they may not be sent to the routing protocol layer.

If a multicast device is not configured to check the Router-Alert option, it sends received IGMP messages to the routing protocol layer for processing, regardless of whether these messages contain the Router-Alert option. If a multicast device is configured to check the Router-Alert option, it sends only the IGMP messages with the Router-Alert option to the routing protocol layer for processing.