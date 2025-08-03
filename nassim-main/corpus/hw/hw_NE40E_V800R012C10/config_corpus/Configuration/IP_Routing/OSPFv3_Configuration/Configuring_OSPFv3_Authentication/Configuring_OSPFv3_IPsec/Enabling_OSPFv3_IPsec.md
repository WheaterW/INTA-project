Enabling OSPFv3 IPsec
=====================

A Security Association (SA) configured in an OSPFv3 process or OSPFv3 area is used to authenticate packets of the process.

#### Context

Perform the following steps on the router that runs OSPFv3:


#### Procedure

* Enable IPsec in an OSPFv3 process.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
     
     
     
     The OSPFv3 view is displayed.
  3. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
     
     
     
     An SA is configured in the process.
     
     An OSPFv3 process can be associated with multiple OSPFv3 areas. An SA applied in the OSPFv3 process can be used in the associated areas.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable IPsec in an OSPFv3 area.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
     
     
     
     The OSPFv3 view is displayed.
  3. Run [**area**](cmdqueryname=area) *area-id*
     
     
     
     The OSPFv3 area view is displayed.
  4. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
     
     
     
     An SA is configured in the OSPFv3 area.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The SA configured on an OSPFv3 area takes precedence over that configured in an OSPFv3 process.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable IPsec in an OSPFv3 area.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ospfv3 ipsec sa**](cmdqueryname=ospfv3+ipsec+sa) *sa-name*
     
     
     
     An SA in the view of an OSPFv3 interface is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The SA configured in the interface view takes precedence over that configured in the OSPFv3 area view or the OSPFv3 process view.
     + The [**ospfv3 ipsec sa**](cmdqueryname=ospfv3+ipsec+sa) command can be used on all the OSPFv3 instances of an interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.