Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display qos buffer-usage**](cmdqueryname=display+qos+buffer-usage) command to check the buffer usage.
* Run the [**display qos buffer ingress-usage**](cmdqueryname=display+qos+buffer+ingress-usage) command to check the buffer usage of lossless queues in the inbound direction on an interface.
  
  
  
  The buffer usage of lossless queues in the inbound direction on an interface can be displayed only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.
* Run the [**display qos buffer egress-usage**](cmdqueryname=display+qos+buffer+egress-usage) command to check the buffer usage of queues in the outbound direction on an interface.
  
  
  
  The buffer usage in the outbound direction on an interface can be displayed only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.
* Run the [**display qos buffer ingress-statistics**](cmdqueryname=display+qos+buffer+ingress-statistics) command to check statistics on discarded incoming packets in the buffer.
  
  
  
  Statistics on discarded incoming packets in the buffer can be displayed only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.