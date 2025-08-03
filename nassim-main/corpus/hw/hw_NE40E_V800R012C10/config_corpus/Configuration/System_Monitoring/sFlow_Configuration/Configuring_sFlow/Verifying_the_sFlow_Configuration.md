Verifying the sFlow Configuration
=================================

Verifying the sFlow Configuration

#### Prerequisites

sFlow has been configured.


#### Procedure

1. Run the [**display sflow configuration**](cmdqueryname=display+sflow+configuration) command to check global sFlow configurations.
2. Run the [**display sflow interface**](cmdqueryname=display+sflow+interface) *interface-type* *interface-number* command to check the sFlow configuration
   on a specified interface.
3. Run the [**display sflow packet statistics**](cmdqueryname=display+sflow+packet+statistics) [ **interface** *interface-type* *interface-number* ] **slot** *slot-id* command to check statistics about sFlow packets sent on a specified interface or sFlow packets sent and received on a specified board.