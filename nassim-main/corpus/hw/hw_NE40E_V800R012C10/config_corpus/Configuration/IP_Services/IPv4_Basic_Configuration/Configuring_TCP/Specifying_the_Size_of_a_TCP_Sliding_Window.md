Specifying the Size of a TCP Sliding Window
===========================================

By setting the sliding window size for TCP, you can set the sizes of the receiving buffer and transmitting buffer in the socket. This improves network performance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**tcp window**](cmdqueryname=tcp+window) *window-size*
   
   
   
   The sending/receiving buffer size of the TCP socket is configured.
   
   The sliding window size ranges from 1 KB to 32 KB, and the default value is 8 KB.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.