Configuring IGMP Snooping and Proxy
===================================

To implement IGMP snooping over EVPN MPLS, you must configure basic IGMP snooping and proxy functions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
   
   
   
   IGMP snooping is enabled globally.
3. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The BD view is displayed.
4. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
   
   
   
   IGMP snooping is enabled in the BD.
5. (Optional) Run [**igmp-snooping version**](cmdqueryname=igmp-snooping+version) *number*
   
   
   
   IGMP versions for IGMP snooping are configured.
   
   
   
   IGMP snooping can process IGMPv1, IGMPv2, and IGMPv3 messages.
   * If *number* is set to 1, only IGMPv1 messages can be processed.
   * If *number* is set to 2, both IGMPv1 and IGMPv2 messages can be processed.
   * If *number* is set to 3, IGMPv1, IGMPv2, and IGMPv3 messages can all be processed.
6. Run [**igmp-snooping proxy**](cmdqueryname=igmp-snooping+proxy)
   
   
   
   IGMP snooping proxy is enabled in the BD.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.