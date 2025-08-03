Configuration Precautions for VS
================================

Configuration_Precautions_for_VS

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Patch loading, activation, and deletion can be performed only in the admin VS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The file system is operated in the Admin-VS. The file systems of different VSs cannot be isolated. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Timestamp-refresh does not support multiple VSs. Plan services properly. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| IFIT does not support multiple VSs and can be configured only in the admin-VS. VSn does not support IFIT. Plan services properly. Otherwise, no IFIT statistics are displayed. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| 1. Multiple VSs are supported. However, color-flag (coloring) can be configured only in the admin VS and is shared by all VSs. If the coloring bit conflicts with QoS and needs to be modified, the IP FPM function in VSn needs to use the coloring configuration of the admin VS.  (1) color-flagloss-measure{tos-bit<bit>|flags-bit0}delay-measure{tos-bit<bit>|flags-bit0};  (2) color-flagloss-measure{tos-bit<bit>|flags-bit0}delay-measurenone;  (3)undocolor-flag  2. Only the instance statistics in the admin VS can be sent to the PM, and the instance performance statistics in VSn cannot be sent to the PM. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| An ATM bundle interface can be created in the admin VS and VSn, but cannot be bound to VSn. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| BOD services do not support multiple VSs. BOD services can be deployed only in the admin VS. Otherwise, BOD services fail to be activated. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| BRAS services do not support multiple VSs (BRAS services can be deployed only in the admin VS). | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The controller interface can be configured only in the admin VS and cannot be allocated to VSn. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| A CPOS-Trunk interface can be created only in the admin VS. A CPOS-Trunk interface in the admin VS cannot be bound to VSn, and a CPOS-Trunk interface cannot be created in VSn. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| The cpu-defend-policy command needs to be configured in the slot view. Many device security functions can be configured only in the admin VS and take effect in all VSs, including CPCAR, attack source tracing, TCP/IP attack defense, application layer association, GTSM, and MA-defend.  MA-defend policies can be configured only in the admin VS. MA-defend policies can be applied to the entire system, a board, or an interface. MA-defend policies can be applied to the entire system or a board only in the admin VS. MA-defend policies can be applied to an interface in non-admin VSs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| DAA services do not support multiple VSs. DAA services can be deployed only in the admin VS. Otherwise, DAA services fail to be activated. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| EDSG services do not support multiple VSs. EDSG services can be deployed only in the admin VS. Otherwise, EDSG services fail to be activated. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| A FlexE logical interface can be created only in the admin VS, not VSn. | NE40E-M2 | NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| A global IMA-group interface can be created only in the admin VS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| A FlexE physical interface cannot be added to VSn. | NE40E-M2 | NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| A global MP-group interface can be created only in the admin VS, and cannot be created in VSn. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| Host-CAR does not support multiple VSs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| An IMA-group main interface can be created only in the admin VS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| IMA-group sub-interfaces can be created in the admin VS and VSn. The main interface must be in the VS. IMA-group sub-interfaces created in the admin VS cannot be bound to VSn. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| The group-mac of L2PT and BPDU tunnels can be configured only in the admin VS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| An MLPPP interface can be created only in the admin VS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| RADIUS services do not support multiple VSs. (RADIUS services can be deployed only in the admin VS.) | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| A serial main interface can be created only in the admin VS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| Serial sub-interfaces can be created in the admin VS and VSn. The corresponding main interface must be in the VS. Serial sub-interfaces created in the admin VS cannot be bound to VSn. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| A trunk serial main interface can be created only in the admin VS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| The destination IP address or UDP port number cannot be configured for the output NetStream flows in the view of a non-admin-VS.  The NetStream service processing board cannot be configured for an interface board in the view of a non-admin-VS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The SOC (including the command in the SOC view) can be configured only in the admin VS and takes effect in all VSs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After a standard Ethernet interface is added to VSn, the interface cannot be switched to the FlexE mode. | NE40E-M2 | NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After a standard Ethernet port is added to VSn, the port rate is automatically adapted based on the optical module type. | NE40E-M2 | NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Port-based 802.1x authentication does not support multiple VSs. (Port-based 802.1x authentication can be deployed only in the admin VS.) | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K |
| For a subcard that allows two 50G ports with consecutive port numbers to be switched to a 100G port, when the port with an odd port number is added to a service VS:  1. If the port with an even port number is configured to work in manual mode using the switch-mode manual command, the port-speed 100GE command cannot be run on the port to forcibly switch the port to 100GE.  2. If the port with an even port number is configured to work in auto-negotiation mode using the switch-mode auto command and a 100GE optical module is inserted into port 0, auto-negotiation fails. | NE40E-M2 | NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Layer 2 loop detection commands can be configured only in the admin VS and take effect in all VSs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Layer 3 loop detection can be configured only in the admin VS and takes effect in all VSs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After a pre-splitting 100GE interface or post-splitting 10GE interface is added to a VS (non-admin VS), interface splitting can be configured after the interface is removed from the VS. | NE40E-M2 | NE40E-M2K |
| Clock services (including synchronous Ethernet, 1588v2, and NTP) can be deployed only in the admin VS. The clock service function does not take effect in VSn. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The names or IDs of NAT instances, service-locations, and service-instance-groups created in different VSs cannot be the same . | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K |
| After invalid ARP packet filtering or ARP destination address detection is configured on a main interface, the corresponding configuration is also delivered to sub-interfaces in different VSs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When main interfaces and sub-interfaces are deployed in different VSs, ESI route negotiation is not supported on interfaces. Properly plan the configuration to prevent main interfaces and sub-interfaces from being deployed across VSs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The performance alarm and flow creation rate control on the forwarding plane are based on the board level and do not support the VS granularity. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Multicast NAT does not support multiple VSs. Plan services properly. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |