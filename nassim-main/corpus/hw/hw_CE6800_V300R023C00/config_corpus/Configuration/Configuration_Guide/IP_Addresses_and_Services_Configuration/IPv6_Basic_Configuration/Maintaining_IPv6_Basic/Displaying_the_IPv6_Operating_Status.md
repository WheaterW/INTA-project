Displaying the IPv6 Operating Status
====================================

Displaying the IPv6 Operating Status

#### Procedure

During routine maintenance, you can run the following commands to check the IPv6 operating status.

**Table 1** Displaying the IPv6 operating status
| Operation | Command |
| --- | --- |
| Display IPv6 interface information. | [**display ipv6 interface**](cmdqueryname=display+ipv6+interface+brief) [ *interface-type interface-number* | **brief** ] |
| Display statistics about IPv6 packets. | [**display ipv6 statistics**](cmdqueryname=display+ipv6+statistics) |
| Display statistics about IPv6 UDP packets. | [**display udp ipv6 statistics**](cmdqueryname=display+udp+ipv6+statistics+verbose) [ **verbose** ] |
| Display statistics about IPv6 TCP packets. | [**display tcp ipv6 statistics**](cmdqueryname=display+tcp+ipv6+statistics+verbose) [ **verbose** ] |
| Display the status of all IPv6 TCP connections. | [**display tcp ipv6 status**](cmdqueryname=display+tcp+ipv6+status+local-ip+local-port+remote-ip) [ **local-ip** *local-ip* | **local-port** *local-port* | **remote-ip** *remote-ip* | **remote-port** *remote-port* ] \* [ **cid** *cid* ] [ **socket-id** *socket-id* ] |
| Display the status of all IPv6 UDP connections. | [**display udp ipv6 status**](cmdqueryname=display+udp+ipv6+status+local-ip+local-port+remote-ip) [ **local-ip** *l6address* | **local-port** *lport* | **remote-ip** *f6address* | **remote-port** *f*port** ] \* [ **cid** *taskid* ] [ *socket-id* *soFd* ] |
| Display ICMPv6 traffic statistics. | [**display icmpv6 statistics**](cmdqueryname=display+icmpv6+statistics+interface+interface) [ **interface** *interface-name* | **interface** *interface-type* *interface-number* ] |
| Display information about created IPv6 sockets. | [**display ipv6 socket**](cmdqueryname=display+ipv6+socket+socket-type+cid+socket-id) [ **socket-type** *socket-type* ] [ **cid** *cid* ] [ **socket-id** *socket-id* ] |