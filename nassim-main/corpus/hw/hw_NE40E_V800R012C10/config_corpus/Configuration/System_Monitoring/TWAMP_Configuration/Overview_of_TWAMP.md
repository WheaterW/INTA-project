Overview of TWAMP
=================

The Two-Way Active Measurement Protocol (TWAMP) is a technology that measures the round-trip performance of an IP link.TWAMP uses UDP packets as probes to collect statistics about the round-trip delay, jitter, and packet loss rate. In addition, TWAMP separates session control and traffic measurement to provide high security. TWAMP-capable network devices work with each other to obtain statistics about IP network performance.

#### Background

As networks develop rapidly and applications become diversified, various services have been deployed to meet service requirements in different scenarios. This poses higher requirements on network performance. As such, a tool that quickly and flexibly provides statistics about IP network performance is urgently needed.

Traditionally, network elements (NEs) themselves generate and maintain statistics about the IP network performance. To display statistics about the performance of an entire network, a network management system (NMS) is required to manage multiple NEs and collect statistics about these NEs. However, there may be no NMS deployed or the NMS may be incapable of collecting statistics.

TWAMP is therefore introduced. NEs themselves no longer need to generate or maintain statistics about the IP network performance. The performance management system manages only the TWAMP client and easily obtains statistics about the entire network.


#### Advantages

TWAMP has the following advantages over the traditional tools that collect statistics about IP network performance:

* TWAMP is a standard protocol that has a unified measurement model and packet format, facilitating deployment.
* Multiprotocol Label Switching Transport Profile (MPLS-TP) Operation, Administration and Maintenance (OAM) can be deployed only on MPLS-TP networks, whereas TWAMP can be deployed on IP networks, MPLS networks, and Layer 3 virtual private networks (L3VPNs).
* Compared with IP Flow Performance Measurement (IP FPM), TWAMP boasts stronger availability and easier deployment and requires no clock synchronization.


#### Models

TWAMP uses the client/server mode and defines four logical entities, as shown in [Figure 1](#EN-US_CONCEPT_0172373241__fig_dc_vrp_twamp_cfg_000301).

* Control-Client: establishes, starts, and stops a test session and collects statistics.
* Session-Sender: proactively sends probes for performance measurement after being notified by the Control-Client.
* Server: responds to the Control-Client's request for establishing, starting, or stopping a test session.
* Session-Reflector: replies to the probes sent by the Session-Sender with response probes after being notified by the Server.

TWAMP uses TCP packets as control signaling packets and UDP packets as probe packets. Control signals are exchanged between the Control-Client and Server through a TCP connection; probes are exchanged between the Session-Sender and Session-Reflector through a UDP connection.
**Figure 1** Logical architecture of TWAMP  
![](images/fig_dc_vrp_twamp_cfg_000301.png)