Configuring PIM over PPPoE
==========================

PIM over PPPoE can be configured to implement authentication and accounting for users to access multicast services.

#### Usage Scenario

Unlike family users, enterprise users cannot use IGMP for multicast access, because enterprise users have Layer 3 networks. Instead, enterprise users can send PIM messages for multicast service access. However, this access mode does not support user authentication or accounting. To resolve this issue, configure PIM over PPPoE. PIM over PPPoE uses the security, accounting, and authentication functions of PPPoE to enable enterprise users to exchange PIM messages through BAS interfaces, implementing authentication and accounting management for enterprise users.


#### Pre-configuration Tasks

Before configuring PIM over PPPoE, complete the following tasks:

* Configure a unicast routing protocol to ensure that devices are reachable.
* [Configure basic PIM-SM functions](dc_vrp_multicast_cfg_0006.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
4. Run [**bas**](cmdqueryname=bas)
   
   
   
   A BAS interface is created, and the BAS interface view is displayed.
5. Run **[**access-type**](cmdqueryname=access-type)** ****layer2-subscriber****
   
   
   
   The user access type is set to Layer 2 access.
6. Run [**multicast copy by-session**](cmdqueryname=multicast+copy+by-session)
   
   
   
   Multicast replication by session is enabled on the BAS interface.
   
   
   
   This command is supported only by the admin VS.
7. Run [**pim snooping enable**](cmdqueryname=pim+snooping+enable)
   
   
   
   PIM over PPPoE is enabled on the BAS interface.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.