Binding an MA to a BD
=====================

Binding an MA to a BD is a prerequisite for configuring single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, two-way frame delay measurement in BD EVPN networking.

#### Context

BD EVPN-based performance monitoring is BD EVPN-specific. Therefore, when deploying performance monitoring defined in Y.1731 in BD EVPN networking, bind an MA to a specified BD, and then collect performance statistics about the MA. Then, performance statistics about a specified PW or AC will be available. Perform the following steps on each PE:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
   
   
   
   The MD view is displayed.
3. Run [**ma**](cmdqueryname=ma) *ma-name*
   
   
   
   The MA view is displayed.
4. Run [**map**](cmdqueryname=map) **bridge-domain**  *bd-id*
   
   
   
   The MA is bound to a BD instance.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.