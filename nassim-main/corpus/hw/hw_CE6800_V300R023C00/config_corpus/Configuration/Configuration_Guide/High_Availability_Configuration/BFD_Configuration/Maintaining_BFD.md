Maintaining BFD
===============

Maintaining BFD

#### Checking the BFD Operating Status

**Table 1** Checking the BFD Operating Status
| Operation | Command |
| --- | --- |
| Check information about BFD sessions. | [**display bfd session**](cmdqueryname=display+bfd+session) { **all** { [ **for-ip** ] | **for-ipv6** } | **discriminator** *discr-value* | **dynamic** | **peer-ip** { *peer-ip* [ **vpn-instance** *vpn-instance-name* ] | **default-ip** } | **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-instance-name* ] | **static** { [ **for-ip** ] | **for-ipv6** } | **static-auto** } [ **verbose** ] |
| Check global BFD statistics. | [**display bfd statistics**](cmdqueryname=display+bfd+statistics) |
| Check statistics on BFD sessions. | [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) { **all** { [ **for-ip** ] | **for-ipv6** } | **discriminator** *discr-value* | **dynamic** | **peer-ip** { *peer-ip* [ **vpn-instance** *vpn-instance-name* ] | **default-ip** } | **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-instance-name* ] | **static** { [ **for-ip** ] | **for-ipv6** } | **static-auto** } |



#### Clearing BFD Statistics

![](public_sys-resources/notice_3.0-en-us.png) 

In BFD maintenance, you can clear unneeded BFD statistics, monitor the BFD operating status, and debug BFD if a fault occurs.

To delete unneeded BFD statistics or improve new statistics lookup efficiency, run the [**reset bfd statistics**](cmdqueryname=reset+bfd+statistics) command to clear existing statistics.

Deleted BFD statistics cannot be restored. Exercise caution when you run the [**reset bfd statistics**](cmdqueryname=reset+bfd+statistics) command.


**Table 2** Clearing BFD Statistics
| Operation | Command |
| --- | --- |
| Clear BFD statistics. | [**reset bfd statistics**](cmdqueryname=reset+bfd+statistics) { **all** | **discriminator** *discr-value* } |

####