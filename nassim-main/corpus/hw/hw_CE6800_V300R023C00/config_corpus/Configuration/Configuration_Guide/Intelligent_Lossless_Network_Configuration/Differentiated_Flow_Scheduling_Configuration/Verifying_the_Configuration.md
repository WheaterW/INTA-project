Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display mice-elephant-flow configuration**](cmdqueryname=display+mice-elephant-flow+configuration) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] command to check the configuration of differentiated flow scheduling.
* For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855: Run the [**display mice-elephant-flow statistics**](cmdqueryname=display+mice-elephant-flow+statistics) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] command to check the statistics about mice flows on an interface where differentiated flow scheduling is enabled.
* For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855: Run the **[**display mice-elephant-flow flow-cache**](cmdqueryname=display+mice-elephant-flow+flow-cache)** command to check the flow table statistics in differentiated flow scheduling.
* For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855: Run the **[**display mice-elephant-flow flow-cache resource**](cmdqueryname=display+mice-elephant-flow+flow-cache+resource)** [ **slot** *slot-id* ] command to check the hardware flow table resource information in differentiated flow scheduling.