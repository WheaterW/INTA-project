Configuring a Static RP
=======================

To use a static Rendezvous Point (RP) in a PIM-SM domain, configure the same RP address and same address range of multicast groups that the RP serves on all routers in the PIM-SM domain. You need to configure the RP only if the PIM-SM mode is used on a private network. If the PIM-SSM mode is used, you do not need to configure the RP.

#### Context

If a network is divided into multiple PIM-SM domains and the static RP needs to be used, configure the same static RP address on all the CEs and PEs in one PIM-SM domain to specify the range of each PIM-SM domain.


#### Procedure

1. Configure a static RP to serve all routers in the PIM-SM domain. For configuration details, see [Configuring a Static RP](dc_vrp_cfg_ngmvpn_0028.html).