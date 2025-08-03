Specifying a NetStream Service Processing Mode
==============================================

After sampling packets, each NetStream-enabled interface board sends sampled packets to the NetStream service processing board for aggregation and output.

#### Context

NetStream services can be processed in the following mode:

* Distributed mode
  
  An interface board samples packets, aggregates flows, and outputs flows.

#### Procedure

* Configure the distributed NetStream service processing mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The view of the slot in which the interface board for NetStream sampling resides is displayed.
  3. Run [**ip netstream sampler to slot**](cmdqueryname=ip+netstream+sampler+to+slot) **self**
     
     
     
     The distributed NetStream service processing mode is specified.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.