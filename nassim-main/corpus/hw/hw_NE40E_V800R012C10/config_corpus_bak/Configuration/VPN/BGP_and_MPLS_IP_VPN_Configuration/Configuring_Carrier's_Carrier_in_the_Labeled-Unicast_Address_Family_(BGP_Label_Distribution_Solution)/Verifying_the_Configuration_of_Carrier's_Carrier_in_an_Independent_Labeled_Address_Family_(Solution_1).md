Verifying the Configuration of Carrier's Carrier in an Independent Labeled Address Family (Solution 1)
======================================================================================================

After configuring carrier's carrier, you can view information
about public network routes on PEs and CEs of carriers with different
levels, and VPN routes on the PEs.

#### Context

The Carrier's Carrier function has been configured.
#### Procedure

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check the public routing tables on the CEs and
  PEs of the Level 1 carrier and the Level 2 carrier.
* Run the [**display
  ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check the private routing tables on the PEs of the Level
  1 carrier and the Level 2 carrier.