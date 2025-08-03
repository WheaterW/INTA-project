Checking the Manual IPsec Configuration
=======================================

After configuring Internet Protocol Security, you can view the IPsec configurations.

#### Prerequisites

The security proposal and SA have been configured.


#### Procedure

1. Run the [**display ipsec sa**](cmdqueryname=display+ipsec+sa+manual+brief+name+brief) **manual** [ **brief** | **name** *sa-name* [ **brief** ] ] command to check information about SAs.
2. Run the [**display ipsec proposal**](cmdqueryname=display+ipsec+proposal+name+brief) [ **name** *proposal-name* | **brief** ] command to check information about a security proposal.
3. Run the [**display ipsec statistics**](cmdqueryname=display+ipsec+statistics+sa-name+slot) [ **sa-name** *sa-name* ] [ **slot** *slot-number* ] command to check statistics about protocol packets processed by IPsec.