Understanding SNMPv2c
=====================

SNMPv2c has been released as a recommended Internet standard.

Simplicity is the main reason for the success of SNMP. On a large and complex network with devices from multiple vendors, a management protocol is required to provide specific functions to simplify management. To remain simple, SNMP:

* Does not provide the batch access mechanism and has low access efficiency of bulk data.
* Is able to run only on TCP/IP networks.
* Does not provide a communication mechanism for managers and is therefore suitable for only centralized management, not distributed management.
* Is suitable for monitoring network devices, not a network.

In July 1992, SNMPv2 was introduced to enhance the security of SNMP. Then in 1996, the Internet Engineering Task Force (IETF) issued a series of SNMP-associated standards, defining SNMPv2c and abandoning the security standard in SNMPv2.

SNMPv2c enhances the following aspects of SNMPv1:

* Structure of management information (SMI)
* Communication between workstations
* Protocol control

#### SNMPv2c Security

The improvements made to the security in SNMPv2 are abandoned in SNMPv2c. SNMPv2c inherits the message mechanism and community concepts in SNMPv1.


#### New PDU Types in SNMPv2c

* Get-Bulk PDUs: A Get-Bulk PDU is generated on the workstation. The Get-Bulk operation (transmission of Get-Bulk PDUs) is implemented based on Get-Next operations. The Get-Bulk operation enables the workstation to query managed object group information. One Get-Bulk operation is equivalent to several consecutive Get-Next operations. You can set the number of recycle times for a Get-Bulk PDU on the workstation. The number of recycle times equals the number of times for performing Get-Next operations during a one-time message exchange on the host.
* Inform-Request PDUs: An Inform-Request PDU is generated on the agent. The Inform-Request operation (transmission of Inform-Request PDUs) provides a guarantee for the trap mechanism. After the agent sends an Inform-Request PDU, the workstation should return a message to the agent acknowledging successful receipt of the Inform-Request PDU. If the message is not returned within a specified period, the Inform-Request PDU is retransmitted until the number of retransmission times exceeds the threshold.