Maintaining NAC
===============

Maintaining NAC

#### Monitoring the NAC Running Status

In routine maintenance, you can run the following commands in any view to check the NAC running status.

**Table 1** Monitoring the NAC running status
| Operation | Command |
| --- | --- |
| Display access user information. | [**display access-user**](cmdqueryname=display+access-user) |
| Display user statistics on the device. | **[**display access-user statistics**](cmdqueryname=display+access-user+statistics)** |
| Display statistics about users whose network access is controlled based on the user name. | **[**display access-user user-name-table statistics**](cmdqueryname=display+access-user+user-name-table+statistics)** { **all** | **username** *username* } |
| Display statistics about 802.1X users. | **display dot1x** |
| Display 802.1X authentication information. | **display dot1x statistics** |
| Display information about 802.1X users in quiet state. | [**display dot1x quiet-user**](cmdqueryname=display+dot1x+quiet-user) |
| Display statistics about 802.1X Identity packets. | [**display access-user dot1x-identity statistics**](cmdqueryname=display+access-user+dot1x-identity+statistics) |
| Display statistics about NAC authentication requests. | **[**display aaa statistics access-type-authenreq**](cmdqueryname=display+aaa+statistics+access-type-authenreq)** |



#### Clearing NAC Statistics

![](public_sys-resources/note_3.0-en-us.png) 

The cleared statistics cannot be restored. Exercise caution when clearing statistics.


**Table 2** Clearing NAC statistics
| Operation | Command |
| --- | --- |
| Clear 802.1X authentication statistics. | **reset dot1x statistics** |
| Clear statistics about 802.1X Identity packets. | **[**reset access-user dot1x-identity statistics**](cmdqueryname=reset+access-user+dot1x-identity+statistics)** |
| Clear statistics about NAC authentication requests. | [**reset aaa statistics access-type-authenreq**](cmdqueryname=reset+aaa+statistics+access-type-authenreq) |