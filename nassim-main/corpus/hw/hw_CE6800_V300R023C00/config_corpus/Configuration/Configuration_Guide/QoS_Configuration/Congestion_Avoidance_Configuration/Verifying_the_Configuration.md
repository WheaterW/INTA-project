Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display drop-profile**](cmdqueryname=display+drop-profile) [ *drop-profile-name* | **brief** ] command to check the configuration of a WRED drop profile.
* Run the [**display qos configuration**](cmdqueryname=display+qos+configuration) **interface** [ { *interface-type* *interface-number* | *interface-name* } ] command to check all QoS configurations on an interface.
* Run the [**display qos queue statistics**](cmdqueryname=display+qos+queue+statistics) { **slot** *slotid* | **interface** { *interface-type* *interface-number* | *interface-name* } } command to check queue-based traffic statistics.
* Run the **[**display qos ecn statistics**](cmdqueryname=display+qos+ecn+statistics)** [ **interface**{ *interface-type* *interface-number* | *interface-name* } ] command to check statistics on packets with the ECN flag on an interface.
  
  
  
  Only the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ support the display of statistics on packets with the ECN flag on an interface.
* Run the **[**display qos ecn threshold**](cmdqueryname=display+qos+ecn+threshold)** [ **interface**{ *interface-type* *interface-number* | *interface-name* } ] command to check ECN threshold information.