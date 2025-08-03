Adjusting BSR RP Parameters (IPv6)
==================================

If a BootStrap router (BSR) Rendezvous Point (RP) is used, you can adjust parameters about Candidate-Rendezvous Points (C-RPs) and Candidate-BootStrap Routers (C-BSRs)

#### Usage Scenario

Initially, each C-BSR considers itself as a BSR and sends a Bootstrap message to the entire network. Each Router receives the Bootstrap messages sent by all C-BSRs. By comparing the information carried by the Bootstrap messages, the Routers elect a BSR.

All Routers know the BSR address. The C-RPs send Advertisement messages to the BSR. An Advertisement message sent by a C-RP carries the address of the C-RP, the range of multicast groups that the C-RP serves, and the priority of the C-RP. The BSR collects C-RP information and summarizes information into an RP-Set, encapsulates the RP-Set in a Bootstrap message, and advertises the Bootstrap message to each Router. Based on the RP-Set, each Router performs the RP calculation by using the same rule and elects the RP for a specific group from multiple C-RPs to which this group corresponds.

The Router can work normally by using default parameter values. The NE40E allows you to adjust BSR RP parameters as needed.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If there is no special requirement, default parameter values are recommended.



#### Pre-configuration Tasks

Before adjusting dynamic RP parameters, complete the following tasks:

* Configure an IPv6 unicast routing protocol to ensure that IPv6 unicast routes are reachable.
* [Configure IPv6 PIM-SM](dc_vrp_multicast_cfg_2005.html) and configure the system to use a BSR RP.


[Adjusting C-RP Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2017.html)

A Candidate-Rendezvous Point (C-RP) periodically sends BootStrap router (BSR) Advertisement messages that carry the C-RP's priority information. You can adjust the priority of a C-RP, interval for sending Advertisement messages, and timeout period of an Advertisement message sent by a device that has C-RPs configured.

[Setting the Range of Valid C-RP Addresses](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2018.html)

The range of valid Candidate-Rendezvous Point (C-RP) addresses and range of IPv6 multicast groups that each C-RP serves can be configured to filter packets on all Candidate-BootStrap Routers (C-BSRs) by using an IPv6 ACL. The BSR adds the C-RP information contained in an Advertisement message received from a C-RP to the RP-Set only when the address of the C-RP and IPv6 multicast groups that the C-RP serves are within the configured ranges respectively. This prevents C-RP spoofing.

[Adjusting C-BSR Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2019.html)

At first, each Candidate-BootStrap Router (C-BSR) considers itself as a BSR and sends a Bootstrap message to all other Routers on the network. You can adjust the C-BSR hash mask length and Candidate-Rendezvous Point (C-RP) priority information carried by a Bootstrap message, interval for sending Bootstrap messages, and timeout period of a Bootstrap message on the Router configured as a C-BSR.

[Setting a Valid BSR Address Range](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2020.html)

You can create IPv6 ACL rules on all devices to filter BootStrap router (BSR) addresses. The devices then receive only the Bootstrap messages with the source addresses being in the valid BSR address range. Thus, BSR spoofing is prevented.

[Verifying the Dynamic RP Parameter Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2022.html)

After adjusting dynamic Rendezvous Point (RP) parameters, verify BootStrap router (BSR) and RP information.