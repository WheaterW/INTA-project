Configuring an LNS
==================

To establish an L2TP tunnel between a LAC and an LNS, you
need to configure an L2TP connection and set tunnel parameters and
an authentication mode on the LNS.

#### Usage Scenario

An NE40E functioning as an LNS provides tunnel boards to process
the tunnel service, responds to the tunnel setup request from a LAC,
authenticates users, and assigns IP addresses to them.

An NE40E manages LNS services using LNS groups. When LNS groups
are configured on an NE40E, the device functions like multiple LNSs. You can configure
an IP address for each LNS group and specify a tunnel board for it.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* When an NE40E functions as an LNS, it is recommended that the IP address
  of the device's loopback interface be used as the IP address of the
  LNS.
* An LNS cannot use a DHCP server to allocate IP addresses to
  users because the LNS does not know users' MAC addresses. An LNS can
  only allocate IP address in its local address pool to users.
* When an LNS interconnects with a LAC, the LNS must have a route
  to the LAC. For example, when an NE40E functioning as a LAC is configured with a source interface
  on the tunnel, the route to the source interface must be configured
  on the LNS.


#### Pre-configuration Task

Before
configuring an LNS, complete the following tasks:

* [Configure
  AAA schemes](dc_ne_aaa_cfg_0515.html).
* Configure a local address pool that is used to allocate IP
  addresses to L2TP users and specify this address pool in the AAA domain.


[Enabling the L2TP Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_0136877.html)

To set up an L2TP tunnel between a LAC and an LNS, L2TP must be first enabled.

[Configuring an L2TP Connection on the LNS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013699.html)

To allow a tunnel to be set up through negotiation after an LNS receives a tunnel setup request from a LAC, you need to configure a virtual template (VT) and user authentication domain in the L2TP group view on the LNS.

[Configuring L2TP Tunnel Authentication](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013481.html)

An L2TP tunnel can be successfully established only after L2TP tunnel authentication succeeds.

[(Optional) Configuring User Authentication on the LNS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013700.html)

Generally, access L2TP users are authenticated on a LAC and do not need to be authenticated on an LNS again. However, if the LNS does not trust the LAC, the users need to be authenticated again on the LNS after the connections between the users and the LNS are established.

[(Optional) Configuring URPF for L2TP Users](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_0137001.html)

To prevent source address spoofing attacks, enable URPF for L2TP users.

[Configuring an LNS Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013482.html)

This section describes how to configure tunnel parameters on the LNS side, such as the source interface for tunnel setup, tunnel board, maximum number of L2TP tunnels, and priority re-marking after CAR.

[(Optional) Configuring a CPE to Use the IP Address Obtained by the LNS User to Establish a BGP Connection with a BRAS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013701.html)

A client connects to the LNS through a CPE and LAC. The CPE obtains an IP address through L2TP user access. In this way, the CPE's downstream devices or other IP addresses can communicate with the LNS.

[Verifying the LNS Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013483.html)

This section describes how to verify the configurations of the L2TP group, session information, and the tunnel on the LNS after the LNS is configured and users go online.