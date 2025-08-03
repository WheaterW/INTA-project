Monitoring Interface Information
================================

Monitoring interface statistics helps you analyze network information based on traffic statistics and rates.

#### Procedure

* Run the [**monitor interface-statistics interface**](cmdqueryname=monitor+interface-statistics+interface) { *interface-name* | *interface-type* *interface-number* } &<1-5> [ [ **interval** *interval-value* ] [ **times** { *times-value* | **infinity** } ] | [ **times** { *times-value* | **infinity** } ] [ **interval** *interval-value* ] ] command in any view to monitor the current traffic statistics on an interface.
* Run the [**monitor interface-statistics batch**](cmdqueryname=monitor+interface-statistics+batch) [ **interface** *interface-type* [ *interface-number-begin* [ **to** *interface-number-end* ] ] ] [ [ **interval** *interval-value* ] [ **times** { *times-value* | **infinity** } ] | [ **times** { *times-value* | **infinity** } ] [ **interval** *interval-value* ] ] [ **main** ] command in any view to monitor traffic statistics on interfaces in batches.
* Run the [**monitor interface-information**](cmdqueryname=monitor+interface-information) **interface** *interface-type* *interface-number* [ **interval** *interval-value* | **times** { *times-value* | **infinity** } ] \* command in any view to check detailed information, including the running status and traffic statistics, on a specified interface.
* Run the [**monitor counters**](cmdqueryname=monitor+counters) **bit** [ **rate** ] **interface** *interface-type* *interface-number* [ **interval** *interval-value* | **times** { *times-value* | **infinity** } ] \* command in any view to monitor traffic statistics on an interface. The traffic statistics include the number of unicast, multicast, and broadcast packets sent or received by the interface and the packet transmission rate.