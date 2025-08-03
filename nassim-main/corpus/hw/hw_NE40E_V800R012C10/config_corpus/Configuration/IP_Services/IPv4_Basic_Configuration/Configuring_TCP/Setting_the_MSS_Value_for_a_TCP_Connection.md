Setting the MSS Value for a TCP Connection
==========================================

The minimum MSS value and maximum MSS value can be configured for TCP connections.

#### Context

Setting a minimum MSS value for a TCP connection defines the smallest TCP packet size, preventing DoS attacks caused by packets with small MSS values.

Setting a maximum MSS value for a TCP connection defines the largest TCP packet size, allowing TCP packets to be successfully forwarded by intermediate devices when no MTU is available.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**tcp min-mss**](cmdqueryname=tcp+min-mss) *minmss-val*
   
   
   
   A minimum MSS value is configured for a TCP connection.
3. Run [**tcp max-mss**](cmdqueryname=tcp+max-mss) *maxmss-val*
   
   
   
   A maximum MSS value is configured for a TCP connection.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The maximum MSS value configured using the **tcp max-mss** command must be greater than or equal to the minimum MSS value configured using the **tcp min-mss** command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.