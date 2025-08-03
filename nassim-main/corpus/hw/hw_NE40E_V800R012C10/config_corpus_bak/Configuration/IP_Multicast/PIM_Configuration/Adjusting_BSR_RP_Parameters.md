Adjusting BSR RP Parameters
===========================

If a BSR RP is used, you can adjust parameters about C-RPs and C-BSRs and configure a BSR administrative domain.

#### Usage Scenario

Initially, each C-BSR considers itself as a BSR and sends Bootstrap messages carrying the C-BSR addresses and C-BSR priorities on the entire network. Each Router receives the Bootstrap messages sent by all C-BSRs. The Router then compares these messages and elects a BSR. All Routers use the same election rule and therefore the elected BSRs are the same.

All Routers on the network must know the BSR address. C-RPs send Advertisement messages to the BSR. An Advertisement message carries the C-RP address, the range of multicast groups the C-RP serves, and the C-RP priority. The BSR summarizes the information into an RP-Set, encapsulates the RP-Set in a Bootstrap message, and advertises the message to all the other Routers on the network. Based on the RP-Set, each Router calculates routes by using the same rule and elects the RP of this group from the multiple C-RPs to which a specific group corresponds.

The Router can work normally with default control parameters. You are allowed to adjust BSR RP parameters based on the specific networking environment.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If there is no special requirement, default parameter values are recommended.



#### Pre-configuration Tasks

Before adjusting BSR RP parameters, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure PIM-SM](dc_vrp_multicast_cfg_0006.html) and configure the system to use a BSR RP.


[Adjusting C-RP Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0016.html)

A Candidate-Rendezvous Point (C-RP) periodically sends BootStrap router (BSR) Advertisement messages that carry the C-RP's priority information. You can adjust the priority of a C-RP, interval for sending Advertisement messages, and timeout period of an Advertisement message sent by a Router that has C-RPs configured.

[Setting a Valid C-RP Address Range](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0017.html)

You can create ACL rules on all Candidate-BootStrap Routers (C-BSRs) for filtering Candidate-Rendezvous Point (C-RP) addresses and the addresses of groups that C-RPs serve. A BSR accepts the Advertisement messages and adds C-RP information to the RP-Set only when C-RP addresses and the addresses of the groups that C-RPs serve in the Advertisement messages are within the valid address range. Thus, the C-RP spoofing is prevented.

[Adjusting C-BSR Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0018.html)

At first, each Candidate-BootStrap Router (C-BSR) considers itself as a BootStrap router (BSR) and sends Bootstrap messages to all other Routers on the network. You can adjust the C-BSR hash mask length and Candidate-Rendezvous Point (C-RP) priority information carried by a Bootstrap message, interval for sending Bootstrap messages, and the holdtime of Bootstrap messages on a Router configured as a C-BSR.

[Setting a Valid BSR Address Range](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0019.html)

You can create ACL rules on all devices to filter BootStrap router (BSR) addresses. The devices then receive only the Bootstrap messages with the source addresses being in the valid BSR address range. Thus, BSR spoofing is prevented.

[Configuring a BSR Administrative Domain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0021.html)

By dividing a PIM-SM network into multiple BootStrap router (BSR) administrative domains and a global domain, the workload of a single BSR is reduced and private group addresses can be used for providing special services for users in specific domains.

[Verifying the Configuration of BSR RP Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0022.html)

After adjusting BootStrap router (BSR) Rendezvous Point (RP) parameters, verify BSR and RP information.