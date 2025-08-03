Clearing PCEP Session Statistics
================================

This section describes how to manually clear PCEP session statistics.

#### Prerequisites

To collect accurate PCEP session statistics, run the [**reset**](cmdqueryname=reset) command to clear existing statistics and then the corresponding [**display**](cmdqueryname=display) command to check the latest statistics.


#### Procedure

* Run the [**reset pce protocol statistics**](cmdqueryname=reset+pce+protocol+statistics) { *ip-address* | **all** } command to clear PCEPv4 session statistics.