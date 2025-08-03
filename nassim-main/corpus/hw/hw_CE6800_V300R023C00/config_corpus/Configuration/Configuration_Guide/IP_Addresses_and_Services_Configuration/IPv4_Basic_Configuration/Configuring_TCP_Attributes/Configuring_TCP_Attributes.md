Configuring TCP Attributes
==========================

Configuring TCP Attributes

#### Context

If TCP is used for device connections, you can configure TCP attributes to improve TCP transmission reliability.

* SYN-Wait timer: starts when SYN packets are sent. If response packets are not received before the SYN-Wait timer expires, the TCP connection is terminated.
* FIN-Wait timer: starts when the TCP connection status changes from FIN\_WAIT\_1 to FIN\_WAIT\_2. If FIN packets are not received before the FIN-Wait timer expires, the TCP connection is terminated.
* Receive or send buffer size of a connection-oriented socket: The size of the TCP sliding window can be adjusted to improve network performance.
* Minimum MSS value: The minimum MSS value of a TCP connection defines the smallest TCP packet size, preventing denial of service (DoS) attacks caused by packets with small MSS values.
* Maximum MSS value: The maximum MSS value of a TCP connection defines the largest TCP packet size, allowing TCP packets to be successfully forwarded by intermediate devices when no MTU is available.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure TCP attributes (see [Table 1](#EN-US_TASK_0000001176663325__table1471653322916)).
   
   
   
   **Table 1** Configuring TCP attributes
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure a SYN-Wait timer for TCP connections. | [**tcp timer syn-timeout**](cmdqueryname=tcp+timer+syn-timeout) *interval* | Optional.  The default SYN-Wait timer of TCP connections is 75 seconds. |
   | Configure a FIN-Wait timer for TCP connections. | [**tcp timer fin-timeout**](cmdqueryname=tcp+timer+fin-timeout) *interval* | Optional.  The default FIN-Wait timer of TCP connections is 675 seconds. |
   | Configure a receive or send buffer size for a TCP socket. | [**tcp window**](cmdqueryname=tcp+window) *window-size* | Optional.  A sliding window size indicates the receive or send buffer size of a TCP socket. Setting a TCP sliding window size can improve network performance. |
   | Configure a maximum MSS value for a TCP connection. | [**tcp max-mss**](cmdqueryname=tcp+max-mss) *maxmss-val* | The maximum MSS value of a TCP connection defines the largest TCP packet size, allowing TCP packets to be successfully forwarded by intermediate devices when no MTU is available. |
   | Configure a minimum MSS value for a TCP connection. | [**tcp min-mss**](cmdqueryname=tcp+min-mss) *minmss-val* | To prevent the device from receiving packets with a small MSS value, configure a minimum MSS value for a TCP connection. |
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```