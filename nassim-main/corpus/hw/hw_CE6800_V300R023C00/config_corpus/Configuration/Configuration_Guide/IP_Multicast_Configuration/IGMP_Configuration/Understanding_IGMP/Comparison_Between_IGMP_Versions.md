Comparison Between IGMP Versions
================================

Comparison Between IGMP Versions

#### IGMP Compatibility

IGMP compatibility enables a multicast device running a later IGMP version to be compatible with the hosts running an earlier IGMP version. For example, a multicast device running IGMPv2 can correctly process IGMPv1 hosts' Report messages, and a multicast device running IGMPv3 can correctly process IGMPv1 and IGMPv2 hosts' join requests. After a device running a later IGMP version receives IGMP Report messages from hosts running an earlier IGMP version, it automatically changes the version of the corresponding multicast group to be the same as that of the hosts and then runs the earlier IGMP version.

* When an IGMPv2 multicast device receives IGMPv1 Report messages from a multicast group, it automatically sets the IGMP version of the group to IGMPv1. In this case, the device ignores the IGMPv2 Leave messages for the group.
* When an IGMPv3 multicast device receives IGMPv2 Report messages from a multicast group, it automatically sets the IGMP version of the group to IGMPv2. In this case, the device ignores IGMPv3 BLOCK messages and the source lists in IGMPv3 TO\_EX messages, meaning that the multicast source selection function of IGMPv3 is suppressed.
* When an IGMPv3 multicast device receives IGMPv1 Report messages from a multicast group, it automatically sets the IGMP version of the group to IGMPv1. In this case, the device ignores IGMPv2 Leave messages, IGMPv3 BLOCK messages, and the source lists in IGMPv3 TO\_IN and IGMPv3 TO\_EX messages.

If you manually change the IGMP version of a multicast device to a later version, the multicast device still operates in the original version if group members of that version exist. The multicast device upgrades its IGMP version only after all group members of the original version leave.


#### Comparison Between IGMP Versions

[Table 1](#EN-US_CONCEPT_0000001130624426__tab_01) compares the three IGMP versions.

**Table 1** Comparison between the three IGMP versions
| Item | IGMPv1 | IGMPv2 | IGMPv3 |
| --- | --- | --- | --- |
| Querier election mode | Through PIM | Through competition among multicast devices on the same network segment | Through competition among multicast devices on the same network segment |
| General Query message | Supported | Supported | Supported |
| Report message | Supported | Supported | Supported |
| Group-Specific Query message | Not supported | Supported | Supported |
| Leave message | Not supported | Supported | No specific Leave message is defined. Instead, group members send a specified type of Report message to notify multicast devices that they are leaving a group. |
| Group-and-Source-Specific Query message | Not supported | Not supported | Supported |
| Specifying a multicast source | Not supported | Not supported | Supported |
| Protocol message versions supported | IGMPv1 | IGMPv1 and IGMPv2 | IGMPv1, IGMPv2, and IGMPv3 |
| ASM model | Supported | Supported | Supported |
| SSM model | IGMP SSM mapping required | IGMP SSM mapping required | Supported |