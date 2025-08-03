Verifying the Configuration of IPv6 Flexible Flow Statistics Collection
=======================================================================

After NetStream configurations are complete, you can run the display commands in any view to verify the running status of NetStream functions.

#### Prerequisites

NetStream IPv6 flow statistics have been collected.


#### Procedure

* Run the [**display ipv6 netstream statistics**](cmdqueryname=display+ipv6+netstream+statistics) **slot** *slot-id* command to check statistics about NetStream flows.
* Run the [**display ip netstream statistics interface**](cmdqueryname=display+ip+netstream+statistics+interface) { *interface-name* | *interface-type* *interface-number* } command to check statistics about sampled packets on an interface.
* Run the [**display netstream**](cmdqueryname=display+netstream) { **all** | **global** | **interface** *interface-type interface-number* } command to check NetStream configurations in different views.
* Run the [**display ipv6 netstream monitor**](cmdqueryname=display+ipv6+netstream+monitor) { **all** | *monitor-name* } command to check monitoring information about IPv6 flexible flows.