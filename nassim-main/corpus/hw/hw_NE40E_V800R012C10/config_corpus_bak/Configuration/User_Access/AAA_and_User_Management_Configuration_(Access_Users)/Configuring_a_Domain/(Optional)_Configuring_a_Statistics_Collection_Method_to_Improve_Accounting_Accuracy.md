(Optional) Configuring a Statistics Collection Method to Improve Accounting Accuracy
====================================================================================

(Optional)_Configuring_a_Statistics_Collection_Method_to_Improve_Accounting_Accuracy

#### Context

One or two layers of VLAN tags are added to each user
packet transmitted over a MAN. The NE40E counts VLAN header length into packet length when collecting
statistics about user packet bytes. As a result, the number of bytes
sent by a user terminal greatly deviates from the number of bytes
in the statistics collected by the NE40E. To improve accounting accuracy, you can configure the NE40E to exclude VLAN header length from packet length when
collecting statistics about packet bytes of Layer 2 IPoE and PPPoE
users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**accounting exclude-type vlan**](cmdqueryname=accounting+exclude-type+vlan) **access-user layer2** { **ipoe** | **pppoe** } \*
   
   
   
   The NE40E is configured to exclude VLAN header length from packet
   length when collecting statistics about user packet bytes.
   
   
   
   This configuration applies to both IPv4 and IPv6 packet
   statistics.
   
   After this command is run, the number of bytes sent
   by the user terminal deviates little from the number of bytes in the
   statistics collected by the NE40E. If no packets are lost, the two numbers are the same.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.