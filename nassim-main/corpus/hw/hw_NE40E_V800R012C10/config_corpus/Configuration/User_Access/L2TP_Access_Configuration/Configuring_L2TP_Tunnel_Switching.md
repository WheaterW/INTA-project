Configuring L2TP Tunnel Switching
=================================

Networking modes are diverse. If a user accesses an LNS across several tunnels, configure L2TP tunnel switching on the intermediate devices.

#### Context

When an NE40E functions as an LTS, you must configure two L2TP groups to function as the LAC and LNS, respectively. The L2TP group that functions as the LAC initiates tunnel connection requests to the LNS (or another LTS node) on the server side. The L2TP group that functions as the LNS responds to tunnel connection requests initiated by the LAC on the user side.

In a common L2TP scenario, if an address pool instead of an L2TP group is bound to the LTS domain, the LTS terminates the tunnel and assigns IP addresses to users. In an L2TP tunnel switching scenario, tunnel establishment can be triggered only when the L2TP group functioning as the LAC is bound to the LTS domain.

The configuration of the LTS functioning as the LNS is the same as that of the LNS. For details, see [Configuration an LNS](dc_ne_l2tp_cfg_013697.html).

The configuration of the LTS functioning as the LAC is the same as that of the LAC. For details, see [Configuration an LAC](dc_ne_l2tp_cfg_013689.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You must specify the LAC-side L2TP group for the LTS domain. The address pool, however, does not need to be specified.