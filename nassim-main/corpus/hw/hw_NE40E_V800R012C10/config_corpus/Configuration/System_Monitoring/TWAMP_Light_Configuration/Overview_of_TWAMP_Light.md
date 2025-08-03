Overview of TWAMP Light
=======================

TWAMP Light, as a light version of TWAMP, simplifies the control protocol used to establish test sessions and measures the round-trip performance of IP networks.

#### Background

TWAMP is an IP network performance measurement protocol defined by the IPPM working group. It defines a standard cross-network performance measurement method. Different from standard TWAMP, TWAMP Light moves the control plane from the Responder to the Controller so that TWAMP control modules can be simply deployed on the Controller. Therefore, TWAMP Light greatly relaxes its requirements on the Responder performance, allowing the Responder to be rapidly deployed.


#### Characteristic

TWAMP Light integrates the Control-Client and Session-Sender on the Controller. The Responder functions merely as the Session-Reflector.

The Controller creates test sessions, collects performance statistics, and reports statistics to the NMS using Performance Management (PM) or MIBs. After that, the Controller parses NMS information and sends the results to the Responder through private channels. The Responder merely responds to TWAMP-Test packets received over test sessions.


#### Models

**Figure 1** TWAMP Light models  
![](images/fig_dc_vrp_cfg_twamp-light_010301.png)

In [Figure 1](#EN-US_CONCEPT_0172373262__fig_dc_vrp_cfg_twamp-light_000301), TWAMP-Test packets function as probes and carry the IP address and UDP port number, and fixed TTL value 255 that are predefined for the test session between the Controller and Responder. The Controller sends a TWAMP-Test packet to the Responder, and the Responder replies to it. The Controller collects TWAMP statistics.

TWAMP Light defines two types of TWAMP-Test packets: Test-request packets and Test-response packets.

* Session-Sender test packets are sent from the Controller to the Responder.
* Session-Reflector test packets are replied by the Responder to the Controller.

The Controller collects performance statistics based on TWAMP-Test packets and reports the results to the NMS, which provides the statistics to users.