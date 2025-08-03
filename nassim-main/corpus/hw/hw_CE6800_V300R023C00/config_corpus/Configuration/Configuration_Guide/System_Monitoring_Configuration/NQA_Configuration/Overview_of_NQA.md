Overview of NQA
===============

Overview of NQA

#### Definition

Network Quality Analysis (NQA) is a tool for measuring network performance and detecting network faults. By sending packets from one network endpoint to another, the tool tests network reachability and collects performance statistics such as the delay, packet loss rate, and jitter about communication between the two endpoints. Such functions help users monitor network quality and detect network faults.


#### Purpose

As networks continue to offer higher speeds and easier access, the services they carry also become more diverse. Supporting such services, including VoIP and video conferencing, requires network providers to monitor the network quality in real time to learn about the network status and performance, as well as effectively diagnose and locate network faults. As well as this, users on the network also need to be able to check the network quality to determine whether the network complies with the network service protocol.

Network quality is most commonly reflected by indicators such as reachability, delay, packet loss rate, jitter, and service response time. In addition, network fault diagnosis and locating are implemented through a destination reachability test and hop-based network path test. Given this, a tool that can be used to collect network quality indicators and test network reachability and paths is required.

The ping and tracert operations are traditional methods that are only able to test end-to-end reachability and network paths. Obtaining more network quality data requires probes. However, as the network scale expands, the number of required probes increases. As a consequence, the network construction and maintenance costs increase.

To meet such requirements, NQA is introduced. It enables users to obtain network quality data without deploying probes, as well as proactively sending test packets between nodes or on paths based on configurations to collect network quality data in real time. Then, network providers can analyze the collected network quality data to get a clear picture of the network status and performance in real time, and diagnose and locate network faults. Network users, on the other hand, can use NQA to check whether the network quality meets requirements or whether network services are available.


#### Benefits

NQA enables network providers to accurately test the network operating status and collect statistics about network quality indicators. This helps network providers provision users with differentiated network services and charge users accordingly. In addition, NQA helps network providers effectively diagnose and locate network faults. With NQA deployed, network providers no longer need dedicated probes, significantly reducing their deployment and maintenance costs. Network users can use NQA to check whether the network quality and service meet requirements.