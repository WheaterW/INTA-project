Specifying the Size of a TCP6 Sliding Window
============================================

The TCP6 sliding window size determines the size of the receiving buffer and transmitting buffer in the socket. This function improves network performance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**tcp ipv6 window**](cmdqueryname=tcp+ipv6+window) *window-size*
   
   
   
   The sending/receiving buffer size of the TCP6 socket is configured.
   
   The sliding window size ranges from 1 KB to 32 KB, and the default value is 8 KB.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.