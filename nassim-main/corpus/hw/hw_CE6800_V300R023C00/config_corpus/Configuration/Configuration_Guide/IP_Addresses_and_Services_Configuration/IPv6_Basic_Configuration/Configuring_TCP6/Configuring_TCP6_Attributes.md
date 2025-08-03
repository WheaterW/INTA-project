Configuring TCP6 Attributes
===========================

Configuring TCP6 Attributes

#### Context

If TCP6 is used for device connection, you can configure TCP6 attributes to improve network performance.

The following TCP6 attributes can be configured on the device:

* SYN-Wait timer: starts when SYN packets are sent. If response packets are not received before the SYN-Wait timer expires, the TCP6 connection is terminated.
* FIN-Wait timer: starts when the TCP6 connection status changes from FIN\_WAIT\_1 to FIN\_WAIT\_2. If FIN packets are not received before the FIN-Wait timer expires, the TCP6 connection is terminated.
* TCP6 sliding window: indicates the receive or send buffer size of a TCP6 socket.
* Maximum maximum segment size (MSS) value: indicates the largest TCP6 packet size.
* Minimum MSS value: indicates the smallest TCP6 packet size.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure TCP6 attributes.
   
   
   
   **Table 1** Configuring TCP6 attributes
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure a SYN-Wait timer for TCP6 connections. | [**tcp ipv6 timer syn-timeout**](cmdqueryname=tcp+ipv6+timer+syn-timeout) *interval* | Set two TCP6 timers to control the TCP6 connection time. |
   | Configure a FIN-WAIT\_2 timer for TCP6 connections. | [**tcp ipv6 timer fin-timeout**](cmdqueryname=tcp+ipv6+timer+fin-timeout) *interval* |
   | Configure a receive or send buffer size for a TCP6 socket. | [**tcp ipv6 window**](cmdqueryname=tcp+ipv6+window) *window-size* | Setting a TCP6 sliding window size can improve network performance. The sliding window size indicates the receive or send buffer size of a TCP6 socket. |
   | Configure a maximum MSS value for a TCP6 connection. | [**tcp ipv6 max-mss**](cmdqueryname=tcp+ipv6+max-mss) *max-mss-val* | The maximum MSS value of a TCP6 connection defines the largest TCP6 packet size, allowing TCP6 packets to be successfully forwarded by intermediate devices when no MTU is available. |
   | Configure a minimum MSS value for a TCP6 connection. | [**tcp ipv6 min-mss**](cmdqueryname=tcp+ipv6+min-mss) *min-mss-val* | To prevent the device from receiving packets with a small MSS value, configure a minimum MSS value for a TCP6 connection. |
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display tcp ipv6 status**](cmdqueryname=display+tcp+ipv6+status+local-ip+local-port+remote-ip) [ **local-ip** *local-ip* ] [ **local-port** *local-port* ] [ **remote-ip** *remote-ip* ] [ **remote-port** *remote-port* ] [ **cid** *cid* ] [ **socket-id** *socket-id* ] command to check the TCP6 connection status.
* Run the [**display tcp ipv6 statistics**](cmdqueryname=display+tcp+ipv6+statistics) command to check TCP6 traffic statistics.