Verifying the RMON Configuration
================================

After configuring RMON, you can view the traffic statistics collected by RMON.

#### Prerequisites

RMON configuration has been completed.


#### Procedure

* Run the [**display
  rmon statistics**](cmdqueryname=display+rmon+statistics) [ **interface-type** *interface-number* ] command to check RMON statistics.
* Run the [**display
  rmon history**](cmdqueryname=display+rmon+history) [ **interface-type** *interface-number* ] command to check RMON historical sampling information.
* Run the [**display
  rmon event**](cmdqueryname=display+rmon+event) [ *entry-number* ] command to check the RMON event processing mode: recording a log or sending a trap.
* Run the [**display
  rmon eventlog**](cmdqueryname=display+rmon+eventlog) [ *entry-number* ] command to check details about RMON logs.
* Run the [**display
  rmon alarm**](cmdqueryname=display+rmon+alarm) [ *entry-number* ] command to check RMON alarm configurations.