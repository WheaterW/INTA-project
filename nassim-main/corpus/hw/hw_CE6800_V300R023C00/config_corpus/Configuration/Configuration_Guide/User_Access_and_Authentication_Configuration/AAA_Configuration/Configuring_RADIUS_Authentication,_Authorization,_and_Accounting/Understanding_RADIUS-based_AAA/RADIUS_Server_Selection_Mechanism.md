RADIUS Server Selection Mechanism
=================================

Multiple RADIUS servers are typically deployed on a large network. If a server is faulty, user access will not be affected. In addition, when a large number of users access the network, load balancing can be implemented among these servers, preventing resources of a single server from being exhausted. If multiple RADIUS servers are configured in a RADIUS server template and a device needs to send packets to one of the servers, the device uses either of the following algorithms to select the RADIUS server based on the command configuration:

* RADIUS server primary/secondary algorithm (default)
* RADIUS server load balancing algorithm

If a RADIUS server functions as both an authentication server and an accounting server and is used in the authentication phase, an access device saves information about the authentication server and first sends accounting requests to this server in the accounting phase.

#### RADIUS Server Primary/Secondary Algorithm

The primary and secondary roles are determined based on the weights configured for RADIUS authentication servers or RADIUS accounting servers. The server with the largest weight is the primary server. If the servers have the same weight, the first configured server is the primary server. In [Figure 1](#EN-US_CONCEPT_0000001512836070__fig_dc_cfg_aaa_601701), the device first sends authentication or accounting packets to the primary server among all servers in up state. If the primary server does not respond, the device sends the packets to the secondary server.

**Figure 1** Diagram for the RADIUS server primary/secondary algorithm  
![](figure/en-us_image_0000001563995965.png)

#### RADIUS Server Load Balancing Algorithm

If this algorithm is used and a device needs to send authentication or accounting packets to a server, the device selects the server based on the weights configured for the RADIUS authentication servers or RADIUS accounting servers. As shown in [Figure 2](#EN-US_CONCEPT_0000001512836070__fig_dc_cfg_aaa_601702), RADIUS server1 is in up state and its weight is 80, and RADIUS server2 is also in up state and its weight is 20. The possibility for the device to send the packets to RADIUS server1 is 80%, which equals the weight of server1 (80) divided by the total weight of server1 and server2 (80 + 20), and that for RADIUS server2 is 20% accordingly.

**Figure 2** Diagram for the RADIUS server load balancing algorithm  
![](figure/en-us_image_0000001563875685.png)

If all the servers in up state do not respond to the packets sent by the device, the device retransmits the packets to a server among the servers that are originally set to down and to which the device has not sent authentication or accounting packets based on the server weight. If the device does not receive any response in the current authentication method, the backup authentication method is used, for example, local authentication. The backup authentication method must have been configured in the authentication scheme. Otherwise, the authentication process ends.