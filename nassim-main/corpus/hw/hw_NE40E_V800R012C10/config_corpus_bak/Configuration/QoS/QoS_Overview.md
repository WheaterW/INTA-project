QoS Overview
============

This chapter describes what the quality of service (QoS) is and introduces some QoS solutions, such as RSVP and DiffServ Model.

#### What Is QoS

The quality of service (QoS) uses a policy to manage traffic congestion at a low cost has been deployed. QoS aims to provide end-to-end service guarantees for differentiated services. It is important to note that QoS does not increase the network bandwidth. Instead, it improves network resource utilization and allows different types of traffic to compete for network resources based on their priorities, so that voice, video, and important data applications are processed preferentially on network devices.

As networks rapidly develop, services on the Internet become increasingly diversified. Apart from traditional applications such as WWW, email, and File Transfer Protocol (FTP), the Internet has expanded to encompass other services such as IP phones, e-commerce, multimedia games, e-learning, telemedicine, videophones, videoconferencing, video on demand (VoD), and online movies. In addition, enterprise users use virtual private network (VPN) technologies to connect their branches in different areas so that they can access each other's corporate databases or manage remote devices through Telnet. **Figure 1** Internet services  
![](figure/en-us_image_0267698262.png)  

Diversified services enrich users' lives but also increase the risk of traffic congestion on the Internet. In the case of traffic congestion, services can encounter long delays or even packet loss. As a result, services deteriorate or even become unavailable. Therefore, a solution to resolve traffic congestion on the IP network is urgently needed.

The best way to resolve traffic congestion is actually to increase network bandwidths. However, increasing network bandwidths is not practical in terms of operation and maintenance costs.

The quality of service (QoS) that uses a policy to manage traffic congestion at a low cost has been deployed. QoS aims to provide end-to-end service guarantees for differentiated services and has played an overwhelmingly important role on the Internet. Without QoS, service quality cannot be guaranteed.


#### Four Components in the DiffServ Model

The DiffServ model consists of four QoS components. Traffic classification and re-marking provide a basis for differentiated services. Traffic policing and shaping, congestion management, and congestion avoidance control network traffic and resource allocation in different ways and allow the system to provide differentiated services.

* **Classification and Marking**: classification classifies packets while keeping the packets unchanged. Traffic marking sets different priorities for packets and therefore changes the packets.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Traffic marking refers to external re-marking, which is implemented on outgoing packets. Re-marking modifies the priority field of packets to relay QoS information to the next-hop device.
  
  Internal marking is used for internal processing and does not modify packets. Internal marking is implemented on incoming packets for the device to process the packets based on the marks before forwarding them. The concept of internal marking is discussed later in this document.
* **Policing and Shaping**: restricts the traffic rate to a specific value. When traffic exceeds the specified rate, traffic policing drops excess traffic, and traffic shaping buffers excess traffic.
* **Congestion management**: places packets in queues for buffering when traffic congestion occurs and determines the forwarding order based on a specific scheduling algorithm.
* **Congestion avoidance**: monitors network resources. When network congestion intensifies, the device proactively drops packets to regulate traffic so that the network is not overloaded.

The four QoS components are performed in a specific order, as shown in the following figure.**Figure 2** QoS implementation  
![](images/fig_feature_image_0021871452.png "Click to enlarge")  


As shown in the [Figure 3](#EN-US_CONCEPT_0172371133__en-us_concept_0172356765_fig_qos_feature_01602), the QoS components are performed at different locations on the network, as shown in the following figure. In principle, traffic classification, traffic re-marking, and traffic policing are implemented on the inbound user-side interface, and traffic shaping is implemented on the outbound user-side interface (if packets of various levels are involved, queue scheduling and a packet drop policy must be configured on the outbound user-side interface). Congestion management and congestion avoidance are configured on the outbound network-side interface.**Figure 3** QoS Components  
![](images/fig_feature_image_0021871474.png "Click to enlarge")