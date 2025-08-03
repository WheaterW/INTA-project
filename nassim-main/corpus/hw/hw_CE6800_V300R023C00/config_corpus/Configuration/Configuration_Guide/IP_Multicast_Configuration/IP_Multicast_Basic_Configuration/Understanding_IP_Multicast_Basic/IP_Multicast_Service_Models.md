IP Multicast Service Models
===========================

Multicast service models are classified for receiver hosts. A multicast source sends multicast messages by using its own IP address as the source address and a multicast group address as the destination address. Receiver hosts can select multicast sources when receiving data. There are two service models: any-source multicast (ASM) and source-specific multicast (SSM). The two service models use different multicast group address ranges. In the ASM model, the range of multicast group addresses is 224.0.1.0â231.255.255.255 or 233.0.0.0â238.255.255.255. In the SSM model, the range of multicast group addresses is 232.0.0.0â232.255.255.255.

#### ASM Model

The ASM model distributes multicast data based on group addresses. A group address identifies a collection of network services, and data sent from any source to this address obtains the same services. After joining a multicast group, a receiver host can receive data sent from any source to the group.

In the ASM model, each group address must be unique on the entire multicast network. "Unique" here means that one ASM group address can be used by only one multicast application at a time. If two different applications use the same ASM group address to send data, their receiver hosts receive data from both sources. This may cause network traffic congestion and adversely affect the receiver hosts. In the ASM model, receiver hosts cannot obtain the location of a multicast source in advance and can join or leave a multicast group at any time.

In the ASM model, there is a special multicast model â source-filtered multicast (SFM). Based on the ASM model, SFM adds a multicast source filtering policy to improve security. In the SFM model, you can configure a filtering policy for multicast sources to permit or deny the messages from certain multicast sources. For the sender, the multicast group memberships are the same; for the receiver, the data is filtered.


#### SSM Model

The SSM model provides service for data flows from specific sources to a specific group. Receiver hosts can specify the sources from which they want to receive data when they join a multicast group. After joining the group, the hosts receive only the data sent from the specified sources to the group.

The SSM model does not require globally unique group addresses, but each group address must be unique to a multicast source. "Unique" here means that different multicast applications on the same source must use different SSM group addresses. Different multicast applications on different sources can use the same SSM group address, because an (S, G) entry is generated for each source-group pair in the SSM model. This saves multicast group addresses and prevents network congestion.