Verifying the Configuration
===========================

After configuring TCP6, verify the configuration.

#### Prerequisites

TCP6 has been configured.


#### Procedure

* Run the [**display tcp ipv6 status**](cmdqueryname=display+tcp+ipv6+status+local-ip+local-port+remote-ip) [ **local-ip** *local-ip* ] [ **local-port** *local-port* ] [ **remote-ip** *remote-ip* ] [ **remote-port** *remote-port* ] [ **cid** *cid* ] [ **socket-id** *socket-id* ] command to check the TCP6 connection status.
* Run the [**display tcp ipv6 statistics**](cmdqueryname=display+tcp+ipv6+statistics) command to check TCP6 traffic statistics.
* Run the [**display ipv6 socket**](cmdqueryname=display+ipv6+socket+socket-type+cid+socket-id) [ **socket-type** *socket-type* ] [ **cid** *cid* ] [ **socket-id** *socket-id* ] command to check socket configurations.