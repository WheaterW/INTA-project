Maintaining Interfaces
======================

Maintaining Interfaces

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

Interface statistics cannot be restored after they are cleared. Confirm your action before you clear interface statistics.



#### Procedure

To perform interface maintenance operations, run the corresponding commands listed in [Table 1](#EN-US_TASK_0000001130781988__table141227425571) in the user view.

**Table 1** Interface maintenance operations
| Operation | Command | Description |
| --- | --- | --- |
| Display diagnostic information of an interface. | [**display interface troubleshooting**](cmdqueryname=display+interface+troubleshooting) [ *interface-name* | *interface-type* *interface-number* ] | If an interface fault occurs, you can check diagnostic information about all faulty interfaces or a specified interface (including alarms and causes of interface down events, up/down transitions, and error packets) to rapidly locate the fault. |
| Display error packet statistics on all service interfaces. | [**display interface counters errors**](cmdqueryname=display+interface+counters+errors) [ **slot** *slotid* ] | None. |
| Display the default configuration of an interface. | [**display default-parameter interface**](cmdqueryname=display+default-parameter+interface) [ *interface-name* | *interface-type* *interface-number* ] | When an interface is present or its default configuration is modified, you can check its default configuration information. Such information includes the interface status, MTU, interval for sending request packets to the peer, interval for collecting traffic statistics, alarm threshold, interface description, and whether to send a trap to the NMS when the interface status changes. |
| Display brief information about a specified type of interface on a device. | ****display interface**** *interface-type* **brief** **main** **non-unicast** | When monitoring the status of an interface or locating the cause of an interface fault, you can check brief information about all interfaces of a specified type. Such information includes the physical status, protocol status, inbound and outbound bandwidth usage in a recent period of time, number of received error packets, and number of sent error packets. |
| Display brief information about all interfaces according to the sequence in which they are located on the panel. | **display interface brief panel-order** | To diagnose faults or collect traffic statistics on interfaces, you can check brief information about all interfaces according to the sequence in which they are located on the panel. Such information includes the physical status, protocol status, inbound and outbound bandwidth usage in a recent period of time, number of received error packets, and number of sent error packets. |
| Display brief information and descriptions of IP-related interfaces. | **display ip interface description** | None. |
| Display IPv6 interface information. | **display ipv6 interface brief** | None. |
| Display the index of an interface in the management information base (MIB). | ****display mib-index interface**** [ **interface-type** [ **interface-number** ] | *i*nterface-name** ] | You can run this command as an NMS user to check the index of an interface. |
| Monitor detailed information about a specified interface, including the running status and statistics. | [**monitor interface counters**](cmdqueryname=monitor+interface+counters) [ **rate** ] { *interface-name* | *interface-type* *interface-number* } | Monitoring interface statistics helps you analyze network status based on the traffic and rate. |
| Monitor the current traffic statistics on an interface. | [**monitor interface-statistics interface**](cmdqueryname=monitor+interface-statistics+interface) { *interface-name* | *interface-type* *interface-number* } &<1-5> |
| Monitor the current traffic statistics on interfaces. | [**monitor interface-statistics batch**](cmdqueryname=monitor+interface-statistics+batch) [ **interface** *interface-type* [ *interface-number-begin* [ **to** *interface-number-end* ] ] ] |
| Monitor the number of packets or packet rate on an interface. | [**monitor interface-information interface**](cmdqueryname=monitor+interface-information+interface) { *interface-name* | *interface-type* *interface-number* } |
| Clear statistics on an interface. | [**reset interface counters**](cmdqueryname=reset+interface+counters) [ *interface-name* | *interface-type* [ *interface-number* ] ] | To monitor the status of an interface or locate faults on an interface, collect traffic statistics on the interface. Before collecting traffic statistics on an interface within a period, clear the existing traffic statistics on this interface. |
| Clear the displayed peak rates and peak rate times of interfaces. | [**reset counters peak-rate interface**](cmdqueryname=reset+counters+peak-rate+interface) { all | *interface-name* | *interface-type* [ *interface-number* ] } | The device saves the historical peak rates of interfaces and updates them only if subsequent peak rates are higher than the saved ones. To obtain subsequent peak rates, clear the saved ones. |