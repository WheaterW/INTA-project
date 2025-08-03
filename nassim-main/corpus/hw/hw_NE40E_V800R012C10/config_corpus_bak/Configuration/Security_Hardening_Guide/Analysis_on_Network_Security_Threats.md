Analysis on Network Security Threats
====================================

Analysis_on_Network_Security_Threats

#### DoS Attack

Universal Service Routers have powerful forwarding capabilities but limited control and management capabilities. In a denial of service (DoS) attack, attackers initiate mass request messages to a Router. As a result, the CPU of the Router fails to process messages in real time, and normal service flows and internal processing flows are interrupted. Consequently, services are denied.

DoS attacks constitute the greatest threat to Routers and must be considered in security hardening.


#### Information Disclosure

Information disclosure results from unauthorized access. Possible causes of unauthorized access are as follows:

* Negligence in system configurations: For the sake of convenience, Routers provide unauthorized login in certain scenarios. On the live network, unauthorized login, however, is still available.
* Negligence in management processes: For easy Router deployment, a configuration file is usually used as the deployment template. Unauthorized access occurs if the administrator does not change the password for the administrator account.
* Defects in openness of IP networks: By deploying sniffers and interception devices, malicious users intercept and parse IP packets in transmission.
* Storage media: Boards or storage devices of a Router are not encrypted when they are transferred.

#### Damage to Information Integrity

Due to the openness of IP networks, packets may be maliciously tampered with by transit nodes or modified by middlemen on purpose to initiate attacks during transmission.

Software and patches may be tampered with before being uploaded to a device. If the device runs software or a patch that has been tampered with, it will be controlled maliciously and attacked.


#### Unauthorized Access

Unauthorized access enables users to obtain the control right or higher right over a Router. Possible causes of unauthorized access are as follows:

* Inappropriate network configurations: Due to lack of a proper access control policy on the firewall, malicious users forcibly access the system from a public network by other means such as cracking.
* Unauthorized use of debugging means provided by the system: Routers provide access to information in internal information processing flows for locating faults. Malicious users obtain the information by using these diagnosis and debugging interfaces.
* Management and control based on roles instead of accounts: The command control mechanism of the Router completes management and control based on roles instead of accounts. As a result, users can use the commands beyond their authority to read communication data or steal system configurations.

#### Identity Spoofing

Due to the openness, the IP network has no authentication and authorization mechanism for MAC and IP addresses, which may easily cause ARP-/IP-based address spoofing attacks. As a result, the Router needs to continuously refresh address entries required for the forwarding process and process requests from spoofed addresses. Incorrect address entries may interrupt the forwarding, and insufficient entry learning capabilities may cause DoS attacks.


#### Replay Attack

Due to the openness, the IP network cannot authenticate the communication terminals at Layer 3 or lower layers. Taking advantage of this defect, hackers send the specified packets repeatedly to initiate DoS attacks.


#### Computer Viruses

In the network system, a Router functions not only as a forwarding node but also as a network unit that can be managed. When computers on the same network segment are infected with viruses, a large amount of spam traffic is generated and exhausts network bandwidth. In this case, the Router cannot obtain network resources as a network element (NE), and therefore services are unavailable.


#### Carelessness of Engineers

Policies that are configured specially for network construction are not cleared in a timely manner after service provisioning.

During network reconstruction, configurations are incorrect due to carelessness or skill shortage of engineers. For example, a loop exists because a network cable is incorrectly plugged, services are interrupted due to incorrect protocol configurations, unexpected blocking of traffic occurs due to configuration errors in the access control policy, and unnecessary access channels are activated.

Administrators share accounts and passwords with other persons.


#### Physical Intrusion

In general, Routers do not have strict restrictions on access of physical devices. High priority permissions can be obtained through physical connections. Malicious attackers access the Router after intruding protection facilities, such as door status control and monitoring system.