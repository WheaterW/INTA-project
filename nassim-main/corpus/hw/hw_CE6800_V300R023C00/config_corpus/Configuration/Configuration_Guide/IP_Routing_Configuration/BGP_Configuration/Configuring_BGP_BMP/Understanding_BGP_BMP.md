Understanding BGP BMP
=====================

Understanding BGP BMP

#### Context

The BGP Monitoring Protocol (BMP) can monitor the BGP running status and trace data of BGP routes on network devices in real time. The BGP running status includes the establishment and termination of peer relationships and update of routing information. The trace data of BGP routes indicates how BGP routes on a device are processed; for example, processing of the routes that match an import or export route-policy.

With BMP, a device can report its BGP running statistics to a monitoring server. This significantly improves monitoring efficiency compared with manually querying the BGP running status if BMP is not used.


#### BMP Message Types

BMP sessions can be used to exchange Initiation, PU, RM, PD, SR, Termination, and ROFT messages. The reported information includes BGP routing information, BGP peer information, and device vendor and version information.

* Initiation message: reports to the monitoring server such information as the device vendor and software version.
* PU message: notifies the monitoring server that a BGP peer relationship has been established.
* RM message: sends to the monitoring server all routes received from BGP peers and notifies the server of route addition or deletion in real time.
* PD message: notifies the monitoring server that a BGP peer relationship has been disconnected.
* SR message: reports device running statistics to the monitoring server.
* Termination message: reports to the monitoring server the cause of BMP session termination.
* Route Policy and Attribute Trace (ROFT) message: used to report the trace data of routes to the monitoring server in real time.

![](public_sys-resources/note_3.0-en-us.png) 

BMP sessions are unidirectional. Devices send messages to the monitoring server but ignore messages sent by the server.



#### Implementation

In [Figure 1](#EN-US_CONCEPT_0000001176743555__fig_dc_vrp_bgp_feature_003701), TCP connections are established between the monitoring server and BGP devices. The BGP devices send unsolicited BMP messages to the monitoring server to report BGP running statistics. After receiving these BMP messages, the monitoring server parses them and displays the BGP running status in the monitoring view. By analyzing the headers in the BMP messages, the monitoring server can determine which BGP peers have advertised the routes carried in these messages.

When establishing a connection between a BGP device and a monitoring server, note the following guidelines:

* You can specify a port for the TCP connection between the BGP device and monitoring server.
* One BGP device can connect to multiple monitoring servers, and one monitoring server can connect to multiple BGP devices.
* A monitoring server can monitor all BGP peers or a specified one.
* In each BMP instance, one BGP device can connect to multiple monitoring servers so that the servers can back up each other, improving reliability. In addition, different servers can be used to monitor routes from the same BGP peer in different address families, allowing each BGP service to be monitored by a different server.

**Figure 1** Typical BMP networking  
![](figure/en-us_image_0000001130624180.png "Click to enlarge")

#### Benefits

BMP facilitates the monitoring of BGP running status and reports security threats in real time so that preventive measures can be taken promptly.