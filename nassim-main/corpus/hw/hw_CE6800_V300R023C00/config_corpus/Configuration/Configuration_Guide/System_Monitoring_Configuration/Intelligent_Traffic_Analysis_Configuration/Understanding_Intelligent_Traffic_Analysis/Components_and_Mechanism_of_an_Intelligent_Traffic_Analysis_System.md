Components and Mechanism of an Intelligent Traffic Analysis System
==================================================================

Components and Mechanism of an Intelligent Traffic Analysis System

#### System Components

A typical intelligent traffic analysis system consists of the traffic-analysis data exporter (TDE), traffic-analysis processor (TAP), and traffic-analysis data analyzer (TDA).

* The TDE determines which service flows are to be detected and sends them to the TAP.
* The TAP is a chip on the CPU of a device. It processes and analyzes the service flows received from the TDE, and exports analysis results to the TDA.
* The TDA is a network traffic analysis tool that provides a graphical user interface (GUI) to make it convenient for users to obtain, view, and analyze collected data. Currently, only iMaster NCE-FabricInsight can function as the TDA.

In actual applications, the TDE and TAP are deployed on the same device enabled with the intelligent traffic analysis function. In [Figure 1](#EN-US_CONCEPT_0000001564133041__fig122711237128), packets in a service flow between Host1 and Host4 traverse the same path in both directions. As such, each device on this path can obtain the bidirectional traffic of the flow. You can analyze indicators such as the packet loss rate and latency of the flow on these devices.

**Figure 1** Intelligent traffic analysis system  
![](figure/en-us_image_0000001513053002.png)

#### Mechanism of the Intelligent Traffic Analysis System

**Figure 2** Mechanism of the intelligent traffic analysis system  
![](figure/en-us_image_0000001564013205.png)

As shown in [Figure 2](#EN-US_CONCEPT_0000001564133041__fig_dc_fd_traffic-analysis_000402), the mechanism of the intelligent traffic analysis system is as follows:

1. A service flow to be detected is specified on the TDE and an ACL rule is delivered to match the service flow. The TDE then sends the received service flow matching this ACL rule to the TAP through the forwarding chip.
2. The TAP processes the received flow. If the flow meets certain requirements, the TAP creates a flow table and analyzes the flow. If the flow does not meet the requirements or exceeds the processing capability of the TAP, the TAP discards the packets.
3. The TAP encapsulates the packet with the analysis result and the TDA's IP address as the destination address, and sends the packet to the forwarding chip for route-based forwarding. When receiving the packet, the TDA then performs further analysis and display.