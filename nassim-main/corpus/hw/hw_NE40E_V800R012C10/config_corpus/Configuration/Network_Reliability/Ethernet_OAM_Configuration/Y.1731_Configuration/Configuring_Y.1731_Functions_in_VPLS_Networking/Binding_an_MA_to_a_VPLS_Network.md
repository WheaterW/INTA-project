Binding an MA to a VPLS Network
===============================

Binding an MA to a VPLS network is a prerequisite for configuring single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, or two-way frame delay measurement in VPLS networking.

#### Context

VPLS-based performance monitoring function is VSI-specific. Therefore, when deploying Y.1731, bind an MA to a specified VSI, and then collect performance statistics about the MA. Then, performance statistics about a specified PW or AC will be available.

* To collect performance statistics about a PW, do as follows on the PEs at both ends of the PW on the VPLS network.
* To collect performance statistics about an AC between a PE and a CE, do as follows on the PE.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
   
   
   
   The MD view is displayed.
3. Run [**ma**](cmdqueryname=ma) *ma-name*
   
   
   
   The MA view is displayed.
4. Run [**map**](cmdqueryname=map) **vsi** *vsi-name*
   
   
   
   The MA is bound to a specified VSI.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.