Maintaining VRRP
================

Maintaining VRRP

#### Context

During routine maintenance, you can run the following commands in any view to check the VRRP operating status and related VRRP information.

**Table 1** Checking the VRRP operating status and related information
| Operation | Command |
| --- | --- |
| Check VRRP information. | **[**display vrrp protocol-information**](cmdqueryname=display+vrrp+protocol-information)** |
| Check all the configured mVRRP groups and their states. | **[**display vrrp admin-vrrp**](cmdqueryname=display+vrrp+admin-vrrp)** |
| Check the status and configurations of the current VRRP group. | [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] |
| Check information about all LBRGs and their member groups or a specific one. | [**display vrrp load-balance**](cmdqueryname=display+vrrp+load-balance) [ **interface** *interface-type* *interface-number* **vrid** *virtual-router-id* ] [ **member-vrrp** [ **vrid** *member-vrrp-virtual-router-id* ] ] |

To delete unneeded statistics about VRRP Advertisement packets or improve new statistics lookup efficiency, run the [**reset vrrp statistics**](cmdqueryname=reset+vrrp+statistics) command to clear existing statistics.

![](public_sys-resources/notice_3.0-en-us.png) 

Deleted statistics about sent and received VRRP Advertisement packets cannot be restored. Exercise caution when running the [**reset vrrp statistics**](cmdqueryname=reset+vrrp+statistics) command.


**Table 2** Clearing statistics about VRRP Advertisement packets
| Operation | Command |
| --- | --- |
| Clear statistics about sent and received VRRP Advertisement packets. | [**reset vrrp**](cmdqueryname=reset+vrrp) [ **interface** { *interface-type* *interface-number* } ] [ **vrid** *virtual-router-id* ] **statistics** |