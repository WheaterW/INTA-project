Understanding SA Messages
=========================

Understanding SA Messages

#### SA Message

MSDP peers share (S, G) information by exchanging SA messages. Transmitted among multiple RPs, an SA message carries multiple groups of (S, G) information, including the IP address of the source RP, number of (S, G) entries contained in the message, and active (S, G) list in the domain.

A device does not send SA Request messages to its remote MSDP peer if the peer has a larger SA cache capacity than its own or if a new receiver joins a group. Instead, the device waits for the SA message sent by its remote MSDP peer in the next period, which delays the receiver from obtaining the multicast source information. For the new receiver to quickly learn the information about active multicast sources, the local RP needs to send an SA Request message to the MSDP peer to request the (S, G) list of a specified group.

After receiving the SA Request message, the remote MSDP peer immediately responds with an SA Response message carrying the required (S, G) information. If an SA Request message filtering rule is configured on the remote MSDP peer, the remote MSDP peer responds only to the SA Request messages permitted by the rule.


#### RPF Check Rules for SA Messages

To prevent SA messages from being repeatedly forwarded between MSDP peers, MSDP peers perform RPF checks on the received SA messages, strictly controlling the incoming ones. The SA messages that do not comply with the RPF rules are discarded.

When forwarding an SA message, an MSDP-enabled device complies with the following RPF check rules:

* Rule 1: If the SA message is sent by the RPF peer, the message is accepted and forwarded to other MSDP peers.
* Rule 2: If the peer that sends an SA message is the source RP, the SA message is accepted and forwarded to other peers.
* Rule 3: A multicast device can set up MSDP peer relationships with several other multicast devices. You can configure one or more remote peers as static RPF peers to allow the local device to accept SA messages from them.
* Rule 4: If a multicast device has only one remote MSDP peer, the peer automatically becomes the RPF peer, and the device accepts the SA messages sent from this peer.
* Rule 5: If a peer that sends an SA message is in the same mesh group as the local multicast device, the SA message is accepted. However, the SA message is not forwarded to other members in the mesh group, but is forwarded to all peers outside the mesh group. If the SA message is sent by a certain MSDP peer outside the mesh group, an RPF check is performed on the SA message. If the SA message passes the check, it is forwarded to all other members of the mesh group. You are advised to add all MSDP peers in the same or different ASs to the same mesh group on a live network that encounters SA message RPF check failures. This prevents SA messages from being discarded due to RPF check failures.
* Rule 6: If the route to the source RP spans multiple ASs, only the SA messages sent from a peer in the next-hop AS are accepted. If this AS has multiple remote MSDP peers, the SA message sent from the peer with the highest IP address is accepted.
* Rule 7: If an SA message is sent from an MSDP peer that is a route advertiser or the next hop of a source RP, the device accepts the SA message. If a network has multiple equal-cost routes to a source RP, the multicast device accepts SA messages sent from all MSDP peers on the equal-cost routes.

The application of rules 6 and 7 depends on route selection. For details, see [Table 1](#EN-US_CONCEPT_0000001130623928__table119671359191016).

**Table 1** Application of RPF check rules 6 and 7
| Whether the Route to the Source RP Is a BGP Route | Scenario | Processing Rule |
| --- | --- | --- |
| Yes | MSDP peers are EBGP peers. | Apply rule 6. |
| MSDP peers are not BGP peers, and the route to the source RP spans multiple ASs. |
| MSDP peers are IBGP peers. | Apply rule 7. |
| MSDP peers are not BGP peers, and the route to the source RP does not span multiple ASs. |
| No | IGP routes or multicast static routes exist. |
| No route is available. | The SA message sent by the MSDP peer is discarded. |



#### Filtering SA Messages

MSDP peers do not filter SA messages by default. SA messages sent from a domain can be transmitted to all MSDP peers on the network. However, (S, G) entries in some PIM-SM domains can guide packet forwarding only in the local domains. For example, some local multicast applications use global multicast group addresses or some multicast sources use private addresses 10.x.x.x. If SA messages are not filtered, these (S, G) entries are transmitted to other MSDP peers. To solve this problem, configure SA message filtering rules (usually ACL rules) and apply them to enable MSDP peers to filter the SA messages they create, forward, and receive. In this way, the transmission of messages sent by multicast sources can be controlled.