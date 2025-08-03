Introduction
============

FR allows user devices, such as routers and hosts, to exchange data on an FR-capable network.

A conventional wide area network (WAN) uses X.25, frame relay (FR), or ATM. Any of these link-layer protocols can transmit data from one local area network (LAN) over a WAN to another LAN. As terminals become intelligent and the quality of physical links improves, the functions of error control and flow control for data at the data link layer on X.25 networks are no longer required. In addition, limited bandwidth resources on X.25 networks cannot meet requirements for services. Due to expensive ATM-capable devices and complicated compatibility, ATM networks are unsuitable for large-scale deployment. Although the bandwidth provided by FR-capable networks is lower than that provided by ATM networks, FR-capable networks boast of short delays and low costs, and thereby are preferentially used to upgrade X.25 networks.

FR simplifies Layer 3 functions of X.25. As a statistics multiplexing protocol, FR provides multiple VCs over a single physical link. VCs are differentiated by data link connection identifiers (DLCIs). On each PVC, the Local Management Interface (LMI) protocol uses status enquiry messages and state messages to maintain link and PVC status.

#### DLCI

A DLCI identifies a VC and is valid only on the local interface and its directly connected interface at the remote end. Therefore, the same DLCI on different physical interfaces does not identify the same VC on an FR-capable network.


#### DTE, DCE, UNI, and NNI

FR-capable networks allow devices to exchange data. Roles of devices and interfaces on FR-capable networks are as follows:

* DTE: data terminal equipment
* DCE: data communication equipment, providing access services for DTEs
* UNI: user-network interface, interconnecting a DTE and a DCE
* NNI: network-network interface, interconnecting DCEs


#### LMI

After a PVC is set up, both the DCE and DTE need to know the PVC status. The LMI protocol uses status enquiry messages and state messages to maintain link and PVC status. For example, LMI adds PVC status information, deletes information about disconnected PVCs, monitors PVC status changes, and checks ink integrity. LMI is defined in the following documents:

* ITU-T Q.933 Appendix A
* ANSI T1.617 Appendix D
* Non-standard compatible protocol


#### Parameters for LMI Packet Exchange

The parameters for LMI packet exchange can be configured to optimize device performance.

**Table 1** Description of parameters for LMI packet exchange
| Device | Parameter | Parameter Description | Description |
| --- | --- | --- | --- |
| DTE | N391 | Specifies the Full status (status of all PVCs) polling counter. | The DTE sends a full status report or a link integrity verification only report at an interval specified by T391. The number of full status reports and link integrity verification only reports to be sent is determined using the formula: Number of link integrity verification only reports: Number of full status reports = (N391 - 1):1. |
| N392 | Specifies the error threshold. | Specifies the threshold at which an error is recorded. |
| N393 | Specifies the monitored event counter. | Specifies the total number of monitored events. |
| T391 | Specifies the polling timer at the user side. | Specifies the interval at which the DTE sends status enquiry messages. |
| DCE | N392 | Specifies the error threshold. | N392 on the DCE has similar functions as N392 on the DTE. However, they differ in that the interval at which status enquiry messages are sent is specified by T392 on the DCE (which, in turn, is specified by T391 on the DTE). |
| N393 | Specifies the monitored event counter. | N393 on the DCE has similar functions as N393 on the DTE. However, they differ in that the interval at which status enquiry messages are sent is specified by T392 on the DCE (which, in turn, is specified by T391 on the DTE). |
| T392 | Specifies the polling timer at the network side. | Specifies the period for which the DCE waits for a status enquiry message from the DTE. The value of T392 must be greater than that of T391. |



#### VC

A VC is a channel or circuit established between two points on a data communications network with packet switching.

VCs can be PVCs or switched virtual circuits (SVCs).

* PVCs are manually configured.
* SVCs are automatically created and deleted through protocol negotiations.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, PVCs are more common than SVCs on FR-capable networks.