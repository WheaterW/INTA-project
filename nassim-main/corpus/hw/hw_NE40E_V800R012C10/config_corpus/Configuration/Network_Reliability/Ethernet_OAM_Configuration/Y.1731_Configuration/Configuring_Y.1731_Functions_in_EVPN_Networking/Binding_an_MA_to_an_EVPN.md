Binding an MA to an EVPN
========================

Binding an MA to an EVPN is a prerequisite for configuring one-way frame delay measurement, two-way frame delay measurement.

#### Context

EVPN-based performance monitoring is EVPN instance-specific. Therefore, when deploying performance monitoring defined in Y.1731 on an EVPN, bind an MA to an EVPN instance, and then collect performance statistics about the MA. Then, performance statistics about a specified PW or AC will be available. Perform the following steps on PEs:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
   
   
   
   The MD view is displayed.
3. Run [**ma**](cmdqueryname=ma) *ma-name*
   
   
   
   The MA view is displayed.
4. Run [**map**](cmdqueryname=map) **evpn vpn-instance** *evpn-instance-name*
   
   
   
   The MA is bound to an EVPN instance.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.