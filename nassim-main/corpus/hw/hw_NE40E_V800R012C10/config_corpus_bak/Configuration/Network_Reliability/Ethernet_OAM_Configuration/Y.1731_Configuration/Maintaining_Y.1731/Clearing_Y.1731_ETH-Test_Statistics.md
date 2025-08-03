Clearing Y.1731 ETH-Test Statistics
===================================

Before collecting statistics about Y.1731 ETH-test packets within a specified period of time, you must clear existing statistics.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Y.1731 ETH-test statistics cannot be restored after being cleared. Exercise caution when clearing Y.1731 ETH-test statistics.



#### Procedure

1. Clear Y.1731 ETH-test statistics on the MEP that initiates an ETH-test instance.
   
   
   * Run the [**reset y1731 eth-test**](cmdqueryname=reset+y1731+eth-test) **md** *md-name* **ma** *ma-name* **mep** *mep-id* command in the user view.
2. Clear Y.1731 ETH-test statistics on the MEP that receives ETH-test packets.
   
   
   * Run the [**reset y1731 statistic-type eth-test**](cmdqueryname=reset+y1731+statistic-type+eth-test) **md** *md-name* **ma** *ma-name* **mep** *mep-id* command in the user view.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.