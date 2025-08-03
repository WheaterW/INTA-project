Monitoring the Operating Status of an Eth-Trunk Interface
=========================================================

Monitoring the Operating Status of an Eth-Trunk Interface

#### Context

During routine maintenance, run the following commands in any view to check the operating status of an Eth-Trunk interface.


#### Procedure

[Table 1](#EN-US_TASK_0000001176661263__table883518595186) lists the commands for monitoring the operating status of an Eth-Trunk interface.

**Table 1** Monitoring the operating status of an Eth-Trunk interface
| **Operation** | Command |
| --- | --- |
| Check the LACP system priority and system ID when no Eth-Trunk in static LACP mode is configured. | **display lacp brief** |
| Check the Eth-Trunk interface configuration after an Eth-Trunk in static LACP mode is configured. | [**display eth-trunk**](cmdqueryname=display+eth-trunk) [ *trunk-id* [ **interface** *interface-type* *interface-number* | **verbose** ] | **brief** ] |
| Check the status of an Eth-Trunk interface. | [**display interface eth-trunk**](cmdqueryname=display+interface+eth-trunk) [ **trunk-id** [ *.*subnumber** ] | ****main**** ] |
| Check the forwarding table of an Eth-Trunk interface. | **[**display interface eth-trunk**](cmdqueryname=display+interface+eth-trunk+forwarding-table)** *trunk-id* **[**forwarding-table**](cmdqueryname=forwarding-table)** |
| Check information about an Eth-Trunk interface and member interfaces of the Eth-Trunk interface. | [**display eth-trunk membership**](cmdqueryname=display+eth-trunk+membership) *trunk-id* |
| Check the statistics about LACPDUs sent and received in LACP mode. | [**display lacp statistics eth-trunk**](cmdqueryname=display+lacp+statistics+eth-trunk) [ *trunk-id* [ **interface** *interface-type* *interface-number* ] ] |
| Check the management status table of an Eth-Trunk interface. | [**display fwm eth-trunk ifmstate**](cmdqueryname=display+fwm+eth-trunk+ifmstate) **interface** *interface-type* *interface-number* |
| Check the Eth-Trunk ID of the forwarding plane and control plane. | [**display fwm eth-trunk**](cmdqueryname=display+fwm+eth-trunk) *trunk-id* **local-id** [ **slot** *slot-id* ] |
| Check the LACP enablement data table. | [**display fwm eth-trunk lacpenable**](cmdqueryname=display+fwm+eth-trunk+lacpenable) *trunk-id* |
| Check information about member interfaces of an Eth-Trunk interface. | [**display fwm eth-trunk member**](cmdqueryname=display+fwm+eth-trunk+member) *trunk-id* |
| Check the status of an Eth-Trunk interface. | [**display fwm eth-trunk status**](cmdqueryname=display+fwm+eth-trunk+status) *trunk-id* |
| Check the data table of the Eth-Trunk load balancing profile. | [**display fwm eth-trunk profile**](cmdqueryname=display+fwm+eth-trunk+profile) *trunk-id* |