Overview
========

The following figure shows the security defense architecture of NE40Es.

**Figure 1** Security defense architecture of NE40Es  
![](figure/en-us_image_0000001134623514.png "Click to enlarge")

On Routers, the security defense architecture comprises the following parts:

#### Security Defense of Forwarding Engines

The forwarding engines (FEs) of Routers provide high performance. Therefore, the best network security solution is to implement security check on the forwarding plane to identify and process invalid packets.

Most FEs, however, are implemented based on hardware, and are less flexible than software. FEs can detect only invalid packets that have deterministic characteristics and do not require complex computing or processing. They are designed with simple security mechanism using fixed processes.

For example:

In malformed packet check, FEs detect and discard packets that violate protocol rules.

In broadcast storm suppression, FEs track the source of a broadcast storm, and discard broadcast packets or limit the rate of broadcast packets by using dynamic access control lists (ACLs) on the forwarding plane.

URPF directly searches for an entry that matches the port and source address on the forwarding plane. If such an entry is found, the packets are discarded.

In fragmented packet flooding, the forwarding plane limits the rate of fragmented packets.

For simple packets, such as ARP, Internet Control Message Protocol (ICMP), and Point-to-Point Protocol (PPP) Keepalive packets, sent from clients, the forwarding plane responds to these packets.

With high performance, FEs can effectively handle traffic flooding attacks. In this way, the CPU does not need to process flooded packets, and the Router reliability is ensured.


#### Security Defense for Channels Between the Forwarding Plane and the Control Plane

Compared with the control plane, the forwarding plane provides infinite processing capabilities. Therefore, the forwarding plane can easily send mass packets, which may cause overload of the control plane.

The packet rates on the channels between the forwarding plane and the control plane must be limited to prevent the forwarding plane from sending too many packets to the control plane. In addition, normal service packets that have high priorities and pass the security check must be permitted to ensure normal service provisioning. In consideration of security and availability, the following mechanisms are used to ensure reliable running of Routers while improving the service processing capabilities of the Routers:

* Central processing unit-committed access rate (CP-CAR): A bandwidth for sending packets to the control plane is configured for each protocol. Different CP-CARs may be configured for typical packets of a protocol, such as ARP Request and ARP Reply packets.
* Dynamic/static blacklist: When attack events are dynamically detected or a static blacklist is configured, all blacklisted packets are rejected to prevent attacks by invalid packets.
* Dynamic/static whitelist: When sessions on the control plane pass the security check or trusted access objects are statically configured, the packets of these objects are free from rate limitation.
* Session-CAR: A bandwidth limit is set for packets to be sent to the control plane for each session neighbor of a specific protocol to prevent mutual impact between session neighbors.
* Micro-segmentation CAR: A bandwidth limit is set for packets to be sent to the control plane for a protocol session established on each specific interface to prevent mutual impact between protocol sessions on different interfaces.

The preceding measures ensure that packets sent from the forwarding plane to the control plane do not cause CPU overload and that the CPU provide services to the maximum.


#### Security Check and Defense of Application Layer Services

The forwarding plane cannot detect or control complex and in-depth attacks because it lacks the capability of perceiving the structure of every protocol.

The security defense on the channels between the forwarding and control planes only protects the CPU against overload, but does not check whether sent packets are secure.

In this case, security check engines need to be embedded into modules at the application layer. Each protocol stack module must be able to dynamically check the validity of packets and sessions and discard invalid packets or sessions in a timely manner to protect the protocol stacks.