Verifying the RMON Configuration
================================

Verifying the RMON Configuration

#### Prerequisites

RMON configuration has been completed.


#### Procedure

* Run the [**display rmon statistics**](cmdqueryname=display+rmon+statistics) [ *interface-type* *interface-number* | *interface-name* ] command to check RMON statistics.
* Run the [**display rmon history**](cmdqueryname=display+rmon+history) [ *interface-type* *interface-number* | *interface-name* ] command to check RMON historical sampling information.
* Run the [**display rmon event**](cmdqueryname=display+rmon+event) [ *entry-number* ] command to check the RMON event processing mode (either recording a log or sending a trap message).
* Run the [**display rmon eventlog**](cmdqueryname=display+rmon+eventlog) [ *entry-number* ] command to check details about RMON logs.
* Run the [**display rmon alarm**](cmdqueryname=display+rmon+alarm) [ *entry-number* ] command to check RMON alarm configurations.