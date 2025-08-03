Verifying the Configuration of IPv4 Flexible Flow Statistics Collection
=======================================================================

After NetStream configurations are complete, you can run the display commands in any view to verify the running status of NetStream functions.

#### Procedure

* Run the [**display ip netstream statistics**](cmdqueryname=display+ip+netstream+statistics) **slot** *slot-id* command to check NetStream packet statistics.
* Run the [**display ip netstream statistics interface**](cmdqueryname=display+ip+netstream+statistics+interface) { *interface-name* | *interface-type* *interface-number* } command to check statistics about sampled packets on an interface.
* Run the [**display netstream**](cmdqueryname=display+netstream) { **all** | **global** | **interface** *interface-type interface-number* } command to check NetStream configurations in different views.
* Run the [**display ip netstream monitor**](cmdqueryname=display+ip+netstream+monitor) { **all** | *monitor-name* } command to check monitoring information about IPv4 flexible flows.