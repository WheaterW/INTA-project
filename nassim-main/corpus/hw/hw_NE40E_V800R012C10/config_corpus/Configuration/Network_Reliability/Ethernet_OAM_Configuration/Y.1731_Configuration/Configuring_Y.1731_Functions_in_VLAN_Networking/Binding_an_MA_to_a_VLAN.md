Binding an MA to a VLAN
=======================

Binding an MA to a VLAN is a prerequisite for configuring single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, or two-way frame delay measurement in VLAN networking.

#### Context

Do as follows on the devices configured with MEPs at two ends of a link:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
   
   
   
   The MD view is displayed.
3. Run [**ma**](cmdqueryname=ma) *ma-name*
   
   
   
   The MA view is displayed.
4. Run [**map**](cmdqueryname=map) **vlan** *vlan-id*
   
   
   
   The MA is bound to a VLAN.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.