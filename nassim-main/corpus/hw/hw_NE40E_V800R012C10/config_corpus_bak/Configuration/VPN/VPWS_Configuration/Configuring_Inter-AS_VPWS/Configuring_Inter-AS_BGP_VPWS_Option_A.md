Configuring Inter-AS BGP VPWS Option A
======================================

Inter-AS BGP VPWS Option A applies to scenarios where few inter-AS PWs are required. Compared with L3VPN, inter-AS BGP VPWS Option A requires more resources and configuration workload.

#### Procedure

1. Configure remote BGP VPWS connections on PEs and ASBRs in each AS. For configuration details, see [Configuring a Remote BGP VPWS Connection](dc_vrp_vpws_cfg_6056.html).
   
   
   
   An ASBR regards its peer ASBR as a local CE and the interface that connects the ASBR to its peer ASBR as an AC interface.