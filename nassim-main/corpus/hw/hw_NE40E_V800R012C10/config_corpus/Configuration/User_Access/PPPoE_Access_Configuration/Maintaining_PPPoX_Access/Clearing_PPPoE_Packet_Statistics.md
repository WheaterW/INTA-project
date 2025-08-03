Clearing PPPoE Packet Statistics
================================

If excessive user login and logout records exist, clear
PPPoE packet statistics.

#### Procedure

* Run the [**reset pppoe statistics**](cmdqueryname=reset+pppoe+statistics) { **slot** *slot-id* | **interface** *interface-type* *interface-number* } command to clear PPPoE packet statistics.
* Run the [**reset
  pppoe statistics online-fail-record**](cmdqueryname=reset+pppoe+statistics+online-fail-record) { **slot** *slot-id* } command to clear
  statistics about PPPoE user login failures due to the limit on the
  number of access users (configured using the **access-ip-limit** command).