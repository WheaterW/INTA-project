Understanding an IGMP Snooping over VXLAN Policy
================================================

An IGMP snooping over VXLAN policy restricts or extends IGMP snooping behaviors, without affecting the implementation of IGMP snooping over VXLAN. Such a policy can be configured for multicast group filtering, Report/Leave message filtering, Query message filtering, entry aging time configuration, and SSM group policy configuration.

#### IGMP snooping over VXLAN Multicast Group Filtering

For security or management purposes, it may be necessary to prevent a device from accepting Report messages or forwarding multicast data for certain multicast groups. In this case, you can configure the range of multicast groups that hosts can join on an IGMP snooping interface.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001155057052__fig10725741163116), HostA and HostB join multicast group G1 (225.1.1.1), and HostC and HostD join multicast group G2 (226.1.1.1). If DeviceA needs to accept and forward data only for G1, configure DeviceA to forward data only for G1.

**Figure 1** Range of multicast groups that hosts can join on an IGMP snooping interface  
![](figure/en-us_image_0000001217639857.png)

#### IGMP Snooping over VXLAN Report/Leave Message Filtering

Forged IGMP messages may be used to attack a multicast network, wasting bandwidth because traffic is forwarded to multicast groups that have no members. If no filtering policy is configured for Report/Leave messages in a BD, all user hosts can receive multicast services. To configure a device to process only the Report/Leave messages received from specified hosts and thereby improve multicast service security, configure a Report/Leave message filtering policy.

As shown in [Figure 2](#EN-US_CONCEPT_0000001155057052__fig4828206184314), DeviceA is a querier on the network. The source addresses of Report/Leave messages sent by HostA and HostB are 10.1.0.1 and 10.0.0.8, respectively. HostC and HostD do not order programs. If no ACL rule is specified, DeviceA processes messages from both HostA and HostB. Conversely, if an ACL rule is configured for DeviceA to accept only the Report/Leave messages with the source address 10.0.0.8, DeviceA processes only the messages from HostB and discards those from HostA.

**Figure 2** IGMP Snooping over VXLAN Report/Leave message filtering policy  
![](figure/en-us_image_0000001200900163.png)

#### IGMP Snooping over VXLAN Query Message Filtering

If an attacker sends Query messages with a smaller IP address than that of the real IGMP querier on the network, devices running IGMP snooping consider the attacker as a legitimate querier. As such, they forward IGMP Report/Leave messages to the network-side interface of the attacker, resulting in the incorrect transmission of multicast traffic. To prevent this problem, you can configure an IGMP Query message filtering policy that permits only IGMP Query messages with specified source IP addresses and rejects other IGMP Query messages. This improves the security of a Layer 2 multicast network.

In [Figure 3](#EN-US_CONCEPT_0000001155057052__fig18214181217297), assume that DeviceA is the querier on the network. If an attacker forges IGMP Query messages with a smaller IP address (for example, 10.0.0.1/24), the real querier DeviceA becomes invalid. As a result, DeviceA cannot respond to the Leave messages sent by hosts and continues to forward traffic to the hosts that have left the multicast group, wasting network resources. To address this problem, you can configure a Query message filtering policy. If you configure an ACL rule on DeviceA to deny the IGMP Query messages with the IP address 10.0.0.1/24, DeviceA discards such IGMP Query messages upon reception.

**Figure 3** IGMP Snooping over VXLAN Query message filtering policy  
![](figure/en-us_image_0000001201107797.png)

#### Aging Time of IGMP Snooping over VXLAN Entries

When a multicast source no longer sends multicast data to a multicast group, the device needs to delete the corresponding (S, G) or (\*, G) entry. In this case, the device continuously detects whether there is multicast traffic sent to the multicast group. To reduce the number of exchanged IGMP snooping messages and the volume of network traffic, set the aging time of entries triggered by multicast traffic in a BD on the querier. By default, the aging time of (S, G) or (\*, G) entries triggered by multicast traffic is 210s. You can set the aging time according to the number of multicast entries required on the network. If many multicast entries exist and the configured time is too short, some entries cannot be generated. Conversely, if the time is too long, unused entries cannot be promptly deleted and system resources cannot be released.

After an aging time is set for entries triggered by multicast traffic in a BD, the device deletes the corresponding (S, G) or (\*, G) entry if the device does not receive multicast traffic destined for the multicast group within the specified time. In this manner, multicast entries are updated and entry resources are released promptly.


#### IGMP Snooping over VXLAN SSM Group Policy

SSM requires a device to know the multicast source specified when hosts join a multicast group. By default, the SSM group address ranges from 232.0.0.0 to 232.255.255.255. If the address of the multicast group that a user joins is not in the SSM group address range, configure an SSM group policy in the BD to add the group address to the range.