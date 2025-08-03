(Optional) Configuring the Cell Loopback Function
=================================================

After cell loopback is configured, the system checks loopback cells to detect and locate link faults.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [.*subinterface* ]
   
   
   
   The ATM interface view is displayed.
3. Run [**oam**](cmdqueryname=oam)
   
   
   
   The OAM interface view is displayed.
4. Run [**attribute**](cmdqueryname=attribute) *vpi/start-vci* [ *vpi/end-vci* ] { **end-point** | **seg-point** }
   
   
   
   When IPoA services are configured on a PVC, the PVC attribute can be configured only as end-point.
   
   When the PVC attribute is end-point, the PVC can respond to the OAM F5 loopback cells.
5. Run [**loopback**](cmdqueryname=loopback) { *vpi* | *vpi*/*vci* } { **end-loopback** | **seg-loopback** } *times*
   
   
   
   The cell loopback function is configured.
   
   OAM provides loopback tests to facilitate fault locating. In tests, a loopback cell is inserted to the VC/VP of a connection point and is looped back by the other connection point. The system detects and locates link faults through the received loopback cells.
   
   The loopbacks can be classified as segment loopbacks and end loopbacks.
   
   * Before configuring the segment loopback, configure the peer loopback point as the segment point.
   * Before configuring the end loopback, configure the peer loopback point as the end point.
   * The loopback in one board fails.