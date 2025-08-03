Displaying the IPv4 Operating Status
====================================

Displaying the IPv4 Operating Status

#### Procedure

During routine maintenance, you can run the following commands to check the IPv4 operating status.

**Table 1** Displaying the IPv4 operating status
| Operation | Command |
| --- | --- |
| Display the status of IPv4 RawIP connections. | [**display rawip status**](cmdqueryname=display+rawip+status+cid+socket-id+local-ip+remote-ip) [ **cid** *cid* ] [ **socket-id** *socket-id* ] [ **local-ip** *local-ip* ] [ **remote-ip** *remote-ip* ] |
| Display the status of IPv4 RawLink connections. | [**display rawlink status**](cmdqueryname=display+rawlink+status+cid+socket-id) [ **cid** *pidval* ] [ **socket-id** *fd* ] |
| Display the current TCP connection status. | [**display tcp status**](cmdqueryname=display+tcp+status+local-ip+local-port+remote-ip+remote-port+cid) [ **local-ip** *ipv4-address* | **local-port** *local-port-number* | **remote-ip** *ipv4-address* | **remote-port** *remote-port-number* ] \* [ **cid** *cid* ] [ **socket-id** *socket-id* ] |
| Display the status of all IPv4 UDP connections. | [**display udp status**](cmdqueryname=display+udp+status+local-ip+local-port+remote-ip+remote-port+cid) [ **local-ip** *laddress* | **local-port** *lport* | **remote-ip** *faddress* | **remote-port** *fport* ] \* [ **cid** *taskid* ] [ **socket-id** *soFd* ] |
| Display information about created IPv4 sockets. If no optional parameter is specified, this command displays information about all types of sockets. | [**display ip socket**](cmdqueryname=display+ip+socket+socket-type+cid+socket-id) [ **socket-type** *socket-type* ] [ **cid** *cid* ] [ **socket-id** *socket-id* ] |
| Display statistics about RawIP packets. | [**display rawip statistics**](cmdqueryname=display+rawip+statistics+verbose) [ **verbose** ] |
| Display statistics about RawLink packets. | [**display rawlink statistics**](cmdqueryname=display+rawlink+statistics) |
| Display statistics about TCP packets. | [**display tcp statistics**](cmdqueryname=display+tcp+statistics+verbose) [ **verbose** ] |
| Display statistics about UDP packets. | [**display udp statistics**](cmdqueryname=display+udp+statistics+verbose) [ **verbose** ] |
| Display detailed IP traffic statistics. | **display ip statistics verbose** [ **protocol** { *protocol-id* | **icmp** | **igmp** | **ospf** | **pim** | **rsvp** | **tcp** | **udp** | **vrrp** } ] |