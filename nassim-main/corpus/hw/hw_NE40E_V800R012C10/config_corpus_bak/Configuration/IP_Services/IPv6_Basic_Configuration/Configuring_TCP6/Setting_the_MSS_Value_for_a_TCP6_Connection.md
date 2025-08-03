Setting the MSS Value for a TCP6 Connection
===========================================

The minimum MSS value and maximum MSS value can be configured for TCP6 connections.

#### Context

Setting a minimum MSS value for a TCP6 connection defines the smallest TCP6 packet size, preventing DoS attacks caused by packets with small MSS values.

Setting a maximum MSS value for a TCP6 connection defines the largest TCP6 packet size, allowing TCP6 packets to be successfully forwarded by intermediate devices when no MTU is available.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**tcp ipv6 min-mss**](cmdqueryname=tcp+ipv6+min-mss) *min-mss-val*
   
   
   
   A minimum MSS value is configured for a TCP6 connection.
3. Run [**tcp ipv6 max-mss**](cmdqueryname=tcp+ipv6+max-mss) *max-mss-val*
   
   
   
   A maximum MSS value is configured for a TCP6 connection.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The maximum MSS value configured using the **tcp ipv6 max-mss** command must be greater than or equal to the minimum MSS value configured using the **tcp ipv6 min-mss** command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.