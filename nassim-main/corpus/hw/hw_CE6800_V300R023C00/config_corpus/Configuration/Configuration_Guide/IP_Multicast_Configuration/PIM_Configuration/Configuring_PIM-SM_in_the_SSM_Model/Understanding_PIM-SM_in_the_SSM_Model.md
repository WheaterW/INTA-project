Understanding PIM-SM in the SSM Model
=====================================

When PIM-SM is used to transmit multicast data, RPs need to be maintained on the network. If receivers on the network know the location of the multicast source and want to request multicast data from the multicast source, PIM-SM in the SSM model can be used to implement fast joining of multicast group members. With PIM-SM in the SSM model, an SPT is set up between the multicast source and group members, and no RP needs to be maintained.

Compared with the ASM model, the SSM model does not need to maintain RPs, construct RPTs, or register multicast sources.

The SSM model is implemented based on some PIM-SM technologies and IGMPv3, and its procedure for setting up an MDT is similar to the procedure for setting up an SPT in the ASM model. The receiver DR, which knows the multicast source address, sends Join messages directly to the source to divert multicast data to receivers.

In the SSM model, multicast traffic forwarding is based on (S, G) channels (similar to TV channels). Multicast users must first join a channel before receiving its multicast traffic. A multicast user can join or leave a multicast channel by subscribing to or unsubscribing from the channel. Currently, only IGMPv3 can be used for channel subscription. To complete a channel subscription, a receiver needs to specify both a multicast group and multicast source.

#### Related Concepts

PIM-SM in the SSM model is implemented based on some technologies of PIM-SM in the ASM model. Concepts related to PIM-SM in the SSM model are the same as those in PIM-SM in the ASM model. For details, see [Related Concepts](vrp_pim_cfg_0011.html#EN-US_CONCEPT_0000001176743279__section_dc_vrp_multicast_feature_300101).


#### Implementation

The multicast data forwarding process in a PIM-SM (in the SSM model) domain is as follows:

1. [Neighbor Discovery](vrp_pim_cfg_0011.html#EN-US_CONCEPT_0000001176743279__section_dc_vrp_multicast_feature_300104): Each PIM device in a PIM-SM (in the SSM model) domain periodically sends [Hello messages](vrp_pim_cfg_0004.html#EN-US_CONCEPT_0000001130783604__section_dc_vrp_multicast_feature_300502) to all other PIM devices to discover PIM neighbors and maintain PIM neighbor relationships. By default, a PIM device permits other PIM control messages or multicast packets received from a neighbor, regardless of whether the PIM device has received [Hello messages](vrp_pim_cfg_0004.html#EN-US_CONCEPT_0000001130783604__section_dc_vrp_multicast_feature_300502) from the neighbor before. However, if the neighbor check function is configured on a PIM device, the PIM device permits other PIM control messages or multicast packets received from a neighbor only after the PIM device receives Hello messages from the neighbor.
2. [DR Election](vrp_pim_cfg_0011.html#EN-US_CONCEPT_0000001176743279__section_dc_vrp_multicast_feature_300105): PIM devices exchange Hello messages to elect a DR on a shared network. The receiver DR is the only multicast data forwarder on the shared network.
3. [Switchover to an SPT](vrp_pim_cfg_0011.html#EN-US_CONCEPT_0000001176743279__section_dc_vrp_multicast_feature_300108): On a PIM-SM network using the SSM model, users can know the location of the multicast source in advance. When users join a multicast group, they can specify the source from which they want to receive data. After receiving a join request from a user, the receiver DR sends a [Join message](vrp_pim_cfg_0004.html#EN-US_CONCEPT_0000001130783604__section_dc_vrp_multicast_feature_300505) towards the multicast source to establish an SPT between the source and the user. Multicast data is then sent by the multicast source to the user along the SPT. A PIM-SM network using the SSM model has the following characteristics:
   * SPT establishment can be triggered by user join requests (both dynamic and static) and SSM-mapping.
   * The DR in an SSM scenario is valid only in the shared network segment connected to group members. The receiver DR sends [Join messages](vrp_pim_cfg_0004.html#EN-US_CONCEPT_0000001130783604__section_dc_vrp_multicast_feature_300505) towards the multicast source so that an (S, G) entry is generated on each hop along the way and then an SPT is set up.
   * PIM-SM in the SSM model supports the PIM DR switchover delay, PIM silent, and BFD for PIM.