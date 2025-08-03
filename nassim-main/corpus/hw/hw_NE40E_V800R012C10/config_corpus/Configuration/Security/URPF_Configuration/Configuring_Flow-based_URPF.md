Configuring Flow-based URPF
===========================

By configuring flow-based URPF, you can perform URPF check for flows of certain types on an interface. This helps prevent source address spoofing attacks initiated using the packets of these types.

#### Usage Scenario

To prevent source address spoofing attacks, you can configure URPF to determine whether the source address of a packet matches the inbound interface of the packet. If the source address matches the inbound interface, the source address is considered valid and the packet is permitted; otherwise, the source address is considered faked and the packet is discarded.

If you want to prevent source address spoofing attacks initiated using flows of certain types, configure flow-based URPF.


#### Pre-configuration Tasks

Before configuring flow-based URPF, complete the following task:

Configure link layer protocol parameters and IP addresses for interfaces to ensure that the link layer protocol status of the interfaces is up.


[Configuring a Traffic Classifier](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_urpf_cfg_0006.html)

To classify traffic on a network, you need to define traffic classifiers based on information such as ACL rules, IP precedence, MAC addresses, and protocol addresses.

[Configuring a Traffic Behavior](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_urpf_cfg_0007.html)

If the routes between the interface where URPF check is performed and the source address of packets are symmetrical, you must perform strict URPF check. In other cases, you can perform loose URPF check.

[Configuring a Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_urpf_cfg_0008.html)

After being classified, the traffic must be associated with the traffic behavior. In this manner, a traffic policy can be formed.

[Applying the Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_urpf_cfg_0009.html)

The traffic policy must be applied to an interface for the configured traffic behavior to take effect on the traffic passing through the interface.