Security Defense Capabilities of the Control Plane
==================================================

To ensure the normal running of control protocols and services, the control plane of the NE40E provides the following security defense capabilities:

* Application layer association
* Defense against malformed packet attacks
* Routing protocol authentication and check
* Generalized TTL Security Mechanism (GTSM)
* Attack source tracking and alarm reporting
* Blacklist and whitelist
* Session-CAR
* Micro-segmentation CAR

#### Application Layer Association

Application layer association refers to the association between the protocol flag status on the control plane and the protocol packet sending of the FEs on the physical layer. After the association is established between the control layer and the physical layer, the protocol flag status is kept consistent. For service protocols disabled on a device, the bottom-layer hardware sends corresponding protocol packets at a low bandwidth by default or even does not send these packets. As a result, the attack scope is narrowed, attack cost is increased, and device security risks are reduced.


#### Defense Against Malformed Packet Attacks

Currently, NE40Es can detect and discard the following malformed packets:

* Null IP payload flooding attack
* IGMP null payload attack
* TCP illegal flags attack
* Duplicated fragment attack
* Fragment flooding
* Tear Drop
* Syndrop
* Nesta
* Fawx
* Bonk
* NewTear
* Rose
* Jolt
* Big offset
* Fraggle

#### Routing Protocol Authentication

Some routing protocols support security authentication. When exchanging packets, two communicating devices use a hash algorithm to calculate digests of the received packets and compare the two digests to identify modified packets promptly.

SHA2 is used for routing protocol authentication, unless the protocol does not support SHA2 to ensure that protocol packets are not modified.

AES256 is used for key storage to greatly enhance key strength and prevent a key leak.


#### Blacklist and Whitelist

The blacklist refers to groups of unauthorized users. Unauthorized users filtered by using ACLs can be blacklisted so that packets from these users are discarded or sent at a low rate.

The whitelist refers to groups of authorized users or high-priority users. It helps actively protect existing services and services of high-priority users. Authorized users or high-priority users can be whitelisted so that packets from these users are sent preferentially at a high rate.


#### GTSM

The Generalized TTL Security Mechanism (GTSM) checks whether the time to live (TTL) values carried in sent packets are valid to protect the CPU from CPU-utilization (CPU overload) attacks.

Based on the Router networking, the number of hops (network nodes) of packets bound for the control plane is limited. You can set the number of hops based on the networking to prevent malicious users from initiating attacks from a remote node.


#### Attack Source Tracking and Alarm Reporting

Attack source tracing is a security hardening method that enables you to analyze attack packets, so that you can extract attack information, including the attack source, severity, and cause. This method also allows a device to record logs and generate alarms for traced attack sources.

When the Router is under attacks, attack source tracking records information about attack packets to help locate faults and deploy attack defense.


#### Session-CAR

In protocol-specific multi-session scenarios, a bandwidth limit can be set for each session to send packets to the control plane. If a session is attacked, the other sessions can retain their connections and send their packets to the control plane.


#### Micro-segmentation CAR

When a protocol establishes sessions through different interfaces, a bandwidth limit can be set for each interface to send packets to the control plane. If an interface is attacked, protocol-specific sessions established on the other interfaces can retain their connections and send their packets to the control plane.