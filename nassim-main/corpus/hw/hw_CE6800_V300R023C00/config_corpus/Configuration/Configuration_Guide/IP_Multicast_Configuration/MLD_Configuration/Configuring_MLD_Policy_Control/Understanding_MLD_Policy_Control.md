Understanding MLD Policy Control
================================

MLD policy control restricts or extends MLD actions, without affecting MLD implementation. It includes source address-based MLD message filtering, range of multicast groups that hosts can join on an MLD interface, maximum number of MLD entries, MLD entries that never time out, and Router-Alert option for MLD.

#### Source Address-based MLD Message Filtering

On a multicast network, a device may be attacked by forged MLD messages, causing it to forward traffic to multicast groups without members. If this is the case, bandwidth resources are wasted. Source address-based MLD message filtering resolves this problem. The filtering function works as follows for MLD Report or Done messages and MLD Query messages:

* Source address-based MLD Report or Done message filtering: filters invalid MLD Report or Done messages based on specified ACL6 rules.
* Source address-based MLD Query message filtering: filters MLD Query messages based on specified ACL6 rules.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001538416574__fig8449353111210), DeviceA is the querier on the network segment, and DeviceA's interface (address 2001:db8:1::1/64) connects to the host network. The source addresses of the MLD Report or Done messages sent by HostA, HostB, and HostC are 2001:db8:2::1/64, 2001:db8:1::5/64, and 2001:db8:1::8/64, respectively. If source address-based MLD message filtering is not configured, DeviceA permits messages from HostB and HostC, but drops messages from HostA. If such filtering is configured, the device forwards or discards MLD Report or Done messages based on an ACL6 rule. For example, if an ACL6 rule only permits MLD Report or Done messages with the source address 2001:db8:1::5/64, DeviceA permits such messages from HostB, but drops those from HostC.

**Figure 1** Network diagram of source address-based MLD Report or Done message filtering  
![](figure/en-us_image_0000001589336525.png)

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001538416574__fig6450165318127), DeviceA is the querier on the network segment and receives MLD Report or Done messages from hosts. If DeviceB constructs bogus MLD Query messages that contain a smaller IPv6 address (for example, 2001:db8:1::1/64), DeviceA will become a non-querier and fail to respond to MLD Done messages from hosts. In this case, DeviceA continues to forward multicast traffic to hosts who have left, wasting network resources. To resolve this problem, you can configure an ACL6 rule on DeviceA to drop MLD Query messages with the source IPv6 address 2001:db8:1::1/64.

**Figure 2** Network diagram of source address-based filtering for MLD Query messages  
![](figure/en-us_image_0000001538736418.png)

#### Range of Multicast Groups that Hosts Can Join on an MLD Interface

For security or management purposes, a device may not want to receive Report messages or forward multicast data for certain multicast groups. To meet this requirement, you can configure the range of multicast groups that hosts can join on an MLD interface.

On the network shown in [Figure 3](#EN-US_CONCEPT_0000001538416574__fig_dc_vrp_multicast_feature_201102), HostA and HostB join multicast group G1 (FF11::101), and HostC joins multicast group G2 (FF13::101). To enable DeviceA to receive and forward data only from G1, configure the range of multicast groups that hosts can join on DeviceA.

**Figure 3** Range of multicast groups that hosts can join on an MLD interface  
![](figure/en-us_image_0000001589496289.png)

#### Maximum Number of MLD Entries

If a large number of users watch multiple programs simultaneously, a large amount of bandwidth resources are consumed. As a result, device performance will be degraded, deteriorating the service quality. To prevent this problem, you can configure the maximum number of MLD entries on the device. When receiving an MLD Report message from a user, the device first checks whether the number of MLD entries exceeds the configured maximum number. If the number does not exceed the maximum, the device sets up a group membership and forwards data flows of the requested multicast group to the user. This improves the clarity and stability of programs for users who have joined multicast groups. On the network shown in [Figure 4](#EN-US_CONCEPT_0000001538416574__fig_dc_vrp_multicast_feature_201103), assume that the maximum number of MLD entries configured on DeviceA's interface is 1. If HostA joins the multicast group first, MLD entries can be created. However, MLD entries cannot be created for HostB.

**Figure 4** Maximum number of MLD entries  
![](figure/en-us_image_0000001538257270.png)The implementation mechanism for the maximum number of MLD entries is as follows:

* MLD-limit is configured on an interface. After receiving an MLD Report message from the interface, the device limits the number of MLD entries on the interface.
* You can configure an ACL6 rule to exclude certain multicast group ranges or source-specific group ranges from MLD entry limiting, so that the corresponding MLD entries are not counted as those on the interface.

The maximum number of MLD entries complies with the following rules:

* (\*, G) and (S, G) entries are each counted as one entry on an interface.
* SSM-mapping (\*, G) entries are not counted as entries on an interface, but each (S, G) entry mapped using the SSM-mapping mechanism is counted as one entry on an interface.


#### MLD On-Demand

In the standard MLD working mechanism, a querier periodically sends Query messages and receives Report and Done messages from members to obtain information about multicast group members. If group memberships on a network are stable, you can configure MLD on-demand on the querier to reduce the number of exchanged MLD messages and network traffic. After this function is configured, the querier maintains group memberships based on the requirements of hosts without proactively sending Query messages to collect member states. This reduces the number of MLD messages exchanged between the querier and hosts.

After MLD on-demand is configured on an interface:

* The interface does not send MLD Query messages.
* Group entries are created after the interface receives Report messages, and they will never age out.
* After the interface receives an MLD Done message, it immediately deletes the corresponding group entry.

#### Router-Alert Option for MLD

Typically, a network device sends a message to the corresponding protocol module for processing only when the destination address of the message is a local interface address. Because the destination address of an MLD message is usually a multicast address (not the address of an interface on a multicast device), the message may fail to be sent to the routing protocol layer for processing. The Router-Alert option can address this problem.

Router-Alert is a special mechanism for identifying protocol messages. If a message contains the Router-Alert option, it needs to be sent to the routing protocol layer for processing. In practice, the destination addresses of some protocol messages are multicast addresses or other special addresses. If the messages do not carry the Router-Alert option, they may not be sent to the routing protocol layer.

If a multicast device is not configured to check the Router-Alert option, it sends received MLD messages to the routing protocol layer for processing, regardless of whether these messages contain the Router-Alert option. If a multicast device is configured to check the Router-Alert option, it sends only the MLD messages with the Router-Alert option to the routing protocol layer for processing.