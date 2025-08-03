Maintaining NTP
===============

Maintaining NTP

#### Monitoring the NTP Operating Status

During routine maintenance, you can run the following commands in any view to monitor the NTP operating status.

**Table 1** Monitoring the NTP operating status
| Operation | Command |
| --- | --- |
| Check the status of dynamic sessions maintained by the NTP service. | [**display ntp sessions**](cmdqueryname=display+ntp+sessions) [ **verbose** ] |
| Check the status of the NTP service. | [**display ntp status**](cmdqueryname=display+ntp+status) |
| Check the tracing path from the local device to the reference IPv4 clock source. | [**display ntp trace**](cmdqueryname=display+ntp+trace) |
| Check the system time. | [**display clock**](cmdqueryname=display+clock) |
| Check the reasons of the latest 10 clock synchronization failures. | [**display ntp event clock-unsync**](cmdqueryname=display+ntp+event+clock-unsync) |
| Check statistics about NTP packets or peers. | [**display ntp statistics packet**](cmdqueryname=display+ntp+statistics+packet) [ **ipv6** ]  [**display ntp statistics packet**](cmdqueryname=display+ntp+statistics+packet) [ **ipv6** ] **interface** { *ifname* | *interface\_type* *interface\_num* | **all** }  [**display ntp statistics packet**](cmdqueryname=display+ntp+statistics+packet) **peer** [ [ *ipv4Addr* [ **vpn-instance** *vpnName* ] ] | **ipv6** [ *ipv6Addr* [ **vpn-instance** *vpnName* ] ] | **domain** [ *domainName* [ **vpn-instance** *vpnName* ] ] ] |



#### Clearing NTP Statistics

During routine maintenance, you can run the following commands in the user view to clear NTP statistics.

![](public_sys-resources/notice_3.0-en-us.png) 

The cleared statistics cannot be restored. Therefore, exercise caution when performing this operation.


**Table 2** Clearing NTP statistics
| Operation | Command |
| --- | --- |
| Clear statistics about all the NTP packets sent and received on the local device. | [**reset ntp statistics packet**](cmdqueryname=reset+ntp+statistics+packet) [ **ipv6** ] |
| Clear statistics about the NTP packets sent and received on a specified interface. | [**reset ntp statistics packet**](cmdqueryname=reset+ntp+statistics+packet) [ **ipv6** ] **interface** { *interface-name* | *interface-type* *interface-number* | **all** } |
| Clear statistics about a specified peer. | [**reset ntp statistics packet peer**](cmdqueryname=reset+ntp+statistics+packet+peer) [ [ *ip-address* [ **vpn-instance** *vpn-instance-name* ] ] | **ipv6** [ *ipv6-address* [ **vpn-instance** *vpn-instance-name* ] ] | **domain** [ *domainName* [ **vpn-instance** *vpnName* ] ] ] |