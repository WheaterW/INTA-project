Maintaining VRRP6
=================

Maintaining VRRP6

#### Context

By maintaining a VRRP6 group, you can clear the statistics about VRRP6 Advertisement packets sent and received by the VRRP6 group and monitor the operating status of the VRRP6 group. During routine maintenance, you can run the following commands in any view to check the VRRP6 operating status.

**Table 1** Checking the VRRP6 operating status
| Operation | Command |
| --- | --- |
| Check statistics about the VRRP6 Advertisement packets sent and received by a VRRP6 group. | [**display vrrp6**](cmdqueryname=display+vrrp6) [ **interface** *interface-type* *interface-number* ] [ *virtual-router-id* ] **statistics** |
| Check information about all LBRGs and their member groups or a specific one when VRRP6 works in single-gateway load balancing mode. | [**display vrrp6 load-balance**](cmdqueryname=display+vrrp6+load-balance) [ **interface** *interface-type* *interface-number* **vrid** *virtual-router-id* ] [ **member-vrrp** [ **vrid** *member-vrrp-virtual-router-id* ] ] |
| Check the bindings between all mVRRP6 groups and service VRRP6 groups or the binding between a specific mVRRP6 group and service VRRP6 group. | [**display vrrp6 binding**](cmdqueryname=display+vrrp6+binding) [ **interface** *interface-type1* *interface-number1* ] [ **vrid** *virtual-router-id1* ] [ **member-vrrp** [ **interface** *interface-type2* *interface-number2* ] [ **vrid** *virtual-router-id2* ] ] |

To delete unneeded statistics about VRRP6 packets or improve new statistics lookup efficiency, run the [**reset vrrp6 statistics**](cmdqueryname=reset+vrrp6+statistics) command to clear existing statistics.

![](public_sys-resources/notice_3.0-en-us.png) 

Deleted statistics about sent and received VRRP6 packets cannot be restored. Exercise caution when running the [**reset vrrp6 statistics**](cmdqueryname=reset+vrrp6+statistics) command.


**Table 2** Clearing statistics about VRRP6 packets
| Operation | Command |
| --- | --- |
| Clear statistics about sent and received VRRP6 packets. | [**reset vrrp6**](cmdqueryname=reset+vrrp6) [ **interface** *interface-type* *interface-number* ] [ **vrid** *virtual-router-id* ] **statistics** |