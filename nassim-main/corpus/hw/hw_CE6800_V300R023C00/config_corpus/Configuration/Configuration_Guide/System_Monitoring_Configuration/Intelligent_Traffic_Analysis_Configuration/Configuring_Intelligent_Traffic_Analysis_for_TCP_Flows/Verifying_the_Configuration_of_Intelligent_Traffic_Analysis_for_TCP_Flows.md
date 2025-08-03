Verifying the Configuration of Intelligent Traffic Analysis for TCP Flows
=========================================================================

Verifying the Configuration of Intelligent Traffic Analysis for TCP Flows

#### Context

After all configurations of intelligent traffic analysis for TCP flows are complete, you can check the configuration results.


#### Procedure

* Run the [**display traffic-analysis tcp ipv4 cache**](cmdqueryname=display+traffic-analysis+tcp+ipv4+cache) [ [ **client** **ip** *cip* | **client** **vni** *cvniid* | **client** **port** *cport* | { **client** **interface** *cifname* | **client** **interface** *ciftype* *cifnumber* } | **server** **ip** *sip* | **server** **vni** *svniid* | **server** **port** *sport* | { **server** **interface** *sifname* | **server** **interface** *siftype* *sifnumber* } ] \* ] **slot** *slot-id* command to check detailed information about intelligent traffic analysis results of IPv4 TCP flows.
* Run the [**display traffic-analysis tcp ipv6 cache**](cmdqueryname=display+traffic-analysis+tcp+ipv6+cache) [ [ **client** **ipv6** *cip-v6-address* | **client** **vni** *cvniid* | **client** **port** *cport* | { **client** **interface** *cifname* | **client** **interface** *ciftype* *cifnumber* } | **server** **ipv6** *sip-v6-address* | **server** **vni** *svniid* | **server** **port** *sport* | { **server** **interface** *sifname* | **server** **interface** *siftype* *sifnumber* } ] \* ] **slot** *slot-id* command to check detailed information about intelligent traffic analysis results of IPv6 TCP flows.