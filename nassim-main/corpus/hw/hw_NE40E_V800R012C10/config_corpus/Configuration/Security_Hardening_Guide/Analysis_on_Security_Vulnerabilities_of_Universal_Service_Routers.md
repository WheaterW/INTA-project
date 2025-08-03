Analysis on Security Vulnerabilities of Universal Service Routers
=================================================================

Analysis on Security Vulnerabilities of Universal Service Routers

#### Limited Processing Capabilities of Control and Management Planes

As technologies develop and the network bandwidth requirements quickly increase, the forwarding capabilities of Routers increase greatly. In recent 10 years, the network bandwidth increases to 100 Gbit/s from 10 Mbit/s and the processing capabilities of the forwarding plane increase abruptly.

Because the control and management planes of the Router run on the CPU, the improvement of software processing capabilities is limited. In the ultra-wideband era, channels between terminals and network elements (NEs) are greatly enhanced, which may easily cause denial of service (DoS) attacks based on traffic flooding.


#### Existence of Insecure Access Channels

As industry standards ever change, Routers may be designed with access channels using protocols (such as SNMPv1/v2 and Telnet) only for purposes of convenient management and inheritance. These access channels lack security, but are not replaced with SNMPv3- or SSH-based access channels. Here, SNMP is short for Simple Network Management Protocol, and SSH is short for Secure Shell. As a result, inappropriate use of these insecure access channels may lead to information disclosure or unauthorized access.

In addition, these insecure protocols do not perform any integrity check, and attackers can tamper with protocol messages on intermediate nodes to mount attacks.


#### Potential Security Risks Caused by the Openness of IP Networks

An open IP network has clear network architecture but also causes great potential security risks.

The IP network does not provide an authentication and authorization mechanism for terminal access, and therefore any terminal can access the IP network at will. Attackers can easily access the IP network and probe the IP address of a Router, and then initiate attacks. In addition, they can easily simulate mass source IP addresses through address spoofing to initiate attacks on the Router.

In the Transmission Control Protocol/Internet Protocol (TCP/IP) suite, Layer 3 and lower layers have no security defense capabilities. Therefore, the application layer needs to ensure message integrity, authentication and authorization, and protocol consistency. As a result, attacks at Layer 4 or a lower layer usually target at the Router.

The Ethernet network itself lacks identity authentication capabilities, which may easily cause MAC address spoofing attacks.

The IP stack is not designed with a security policy structure and therefore is susceptible to attacks.

The preceding potential security risks may expose networks to a variety of attacks, such as address spoofing attacks, replay attacks, malformed packet attacks, network viruses, message tampering, and traffic flooding, and therefore cause security problems.


#### Management Challenge from Complexity of Telecom Networks

A telecom network is huge and complex in structure, involving many network nodes, flexible and complex access channels, and diversified communication protocols.

It is difficult to manage a telecom network. You are required to consider the service provisioning, service flexibility, and ease of management and maintenance while designing the security of a network. Resolution of these contradictions varies according to the technical capabilities and management levels of carriers.

As a result, telecom networks cannot be consistently designed with effective security policies and therefore leave security loopholes to virus infection, unauthorized access, and penetration attacks based on a network element (NE).


#### Challenge from Complexity of Universal Service Routers

The configuration model of the route is complex. Administrators often pursue service availability and neglect security defense capabilities of Routers. As a result, security features of Routers are not configured properly and Routers cannot defend attacks as they are designed to.

The security configuration model of the Router is complex and needs to be configured by well-trained engineers. With insufficient skills, some engineers may implement service availability at the cost of security.