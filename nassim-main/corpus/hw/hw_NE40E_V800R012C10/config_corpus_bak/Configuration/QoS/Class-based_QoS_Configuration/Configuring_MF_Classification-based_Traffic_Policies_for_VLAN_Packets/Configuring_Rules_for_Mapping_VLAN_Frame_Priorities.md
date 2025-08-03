Configuring Rules for Mapping VLAN Frame Priorities
===================================================

This section describes how to configure the rule for mapping VLAN frame priorities.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
   
   
   
   A traffic classifier is created and the traffic classifier view is displayed.
3. Run [**if-match 8021p**](cmdqueryname=if-match+8021p) *8021p-value*
   
   
   
   A rule for mapping the 802.1p values of VLAN packets is defined.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.