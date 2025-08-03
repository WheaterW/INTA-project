Specifying a NetStream Service Processing Mode
==============================================

After sampling packets, each NetStream-enabled interface board sends sampled packets to the NetStream service processing board for aggregation and output. If the NE40E has more than one NetStream service processing board, these NetStream services boards work in redundancy mode to back up each other and balance traffic, which improves system reliability.

#### Context

NetStream services can be processed in the following modes:

* Distributed mode
  
  An interface board samples packets, aggregates flows, and outputs flows.

The [**ip netstream sampler to slot**](cmdqueryname=ip+netstream+sampler+to+slot) command has the same function as the [**ipv6 netstream sampler to slot**](cmdqueryname=ipv6+netstream+sampler+to+slot) command.

* The execution of either command takes effect on all packets, and there is no need to configure both of them. If it is required to configure both of them, ensure that NetStream service processing modes are the same. A mode inconsistency causes an error.

#### Procedure

* Specify the distributed NetStream service processing mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The view of the slot in which the interface board for NetStream sampling resides is displayed.
  3. Run [**ip netstream sampler to slot**](cmdqueryname=ip+netstream+sampler+to+slot) **self**
     
     
     
     The distributed NetStream service processing mode is specified.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.