Comparison Between MLD Versions
===============================

Comparison Between MLD Versions

#### MLD Group Compatibility

MLD group compatibility enables a multicast device running a later MLD version to be compatible with the hosts running an earlier MLD version. For example, MLD group compatibility allows a multicast device running MLDv2 to correctly process MLDv1 hosts' Multicast Listener Report messages. In MLD group compatibility mode, if a multicast device receives MLD Multicast Listener Report messages from hosts running an earlier MLD version, it automatically changes the version of the corresponding multicast group to be the same as that of the hosts and then runs the earlier MLD version.

When an MLDv2 multicast device receives MLDv1 Multicast Listener Report messages from a multicast group, it automatically sets the MLD version of the group to MLDv1. In this case, the device ignores MLDv2 BLOCK messages and the source lists in MLDv2 TO\_EX messages, meaning that the multicast source selection function of MLDv2 is suppressed.

If you manually change the MLD version of a multicast device to a later version and group members of the original version exist, the multicast device continues to operate in the original version. The multicast device upgrades its MLD version only after all group members of the original version leave.


#### Comparison Between MLD Versions

[Table 1](#EN-US_CONCEPT_0000001589161425__tab_dc_vrp_multicast_feature_203101) compares MLDv1 and MLDv2.

**Table 1** Comparison between MLD versions
| Item | MLDv1 | MLDv2 | Advantages of MLDv2 over MLDv1 |
| --- | --- | --- | --- |
| Specifying a multicast source | Not supported | Supported | MLDv2 allows hosts to select multicast sources, whereas MLDv1 does not. |
| Group record | An MLDv1 message contains the record of only one multicast group. | An MLDv2 message contains records of multiple multicast groups. | MLDv2 reduces the number of MLD messages on a network segment. |
| Retransmission mechanism | Not supported | Supported | MLDv2 ensures multicast information consistency between a non-querier and a querier. |