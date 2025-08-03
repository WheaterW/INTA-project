Maintaining URPF
================

Before collecting statistics on the packets that fail the URPF check and are discarded, you need to delete the existing statistics.

#### Procedure

1. Run the [**reset**](cmdqueryname=reset) **ip** **urpf** **discard** **statistics** **interface** { *interface-type* *interface-number* | **all** } command to clear statistics on the packets that fail the URPF check and are discarded on interfaces.
2. Run the [**reset**](cmdqueryname=reset) { **ip** | **ipv6** } **urpf discard statistics** [ **slot** *slot-id* ] command to clear the statistics on the packets that fail the URPF check and are discarded on an interface board.