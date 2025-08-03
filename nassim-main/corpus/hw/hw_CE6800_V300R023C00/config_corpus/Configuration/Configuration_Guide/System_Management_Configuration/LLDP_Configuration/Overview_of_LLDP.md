Overview of LLDP
================

Overview of LLDP

#### Definition

The Link Layer Discovery Protocol (LLDP) is a Layer 2 discovery protocol as defined in IEEE 802.1ab, and provides a standard link-layer discovery method to encapsulate information about the capabilities, management address, device ID, and interface ID of a local device into LLDP frames. These packets are sent to neighboring devices, which save received information in standard Management Information Bases (MIBs) to help the NMS query and determine the communication status of links.


#### Purpose

Ever-expanding networks and diversifying network devices complicate network and device configurations and pose increasingly higher requirements on network management. Most of conventional NMSs can detect Layer 3 network topologies but cannot detect detailed topology information of network devices or configuration conflicts. Therefore, a standard protocol is needed to exchange Layer 2 information between network devices.

The LLDP protocol provides a standard link-layer discovery method. Layer 2 information obtained through LLDP allows NMSs to discover the topology of connected network devices, and display paths between clients, switches, routers, application servers, and network servers. NMSs can also detect configuration conflicts between network devices and identify causes of network failures. Users can use an NMS to monitor the link status on devices running LLDP and quickly locate network faults.


#### Benefits

LLDP allows users to obtain detailed information about the network topology and topology changes and to detect inappropriate configurations that exist on the network in a timely manner. Such information helps users monitor network status in real time to keep the network secure and stable.