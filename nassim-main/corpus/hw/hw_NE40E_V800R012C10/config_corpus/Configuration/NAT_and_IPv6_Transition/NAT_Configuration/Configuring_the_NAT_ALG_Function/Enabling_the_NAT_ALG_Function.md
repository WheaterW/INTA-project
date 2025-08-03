Enabling the NAT ALG Function
=============================

Packets of some protocols, such as FTP and ICMP, contain IP addresses and port numbers in the Data field. To translate the IP addresses and port numbers contained in data, enable the NAT ALG function.

#### Context

Most application layer protocol packets carry user IP addresses and port numbers. NAT translates only network layer addresses and transport layer ports. Therefore, an ALG can be configured to translate IP addresses and port numbers carried in the Data field of application layer packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. Run [**nat alg**](cmdqueryname=nat+alg) { **dns** | **ftp** [ **rate-threshold** *rate-threshold-value* ] | **pptp** | **rtsp** | **all** | **sip** [ **separate-translation** ] }
   
   
   
   The NAT ALG function is enabled for one or more application layer protocols.
   
   
   
   To configure NAT separately for the SIP control channel and data channel, run the [**nat alg**](cmdqueryname=nat+alg) **sip** **separate-translation** command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.