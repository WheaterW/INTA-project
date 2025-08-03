Keepalive Detection
===================

Keepalive Detection

#### Background

The GRE protocol cannot detect the link status. As a result, if a remote interface becomes unreachable, the tunnel connection between the local and remote ends cannot be efficiently terminated. The local end continues to send data, which is then discarded by the remote end due to the unreachable tunnel. This leads to a data black hole.

To solve this problem, devices support the link status detection function, also known as the keepalive function, on GRE tunnels. The keepalive function detects whether a tunnel is in keepalive state, that is whether the remote end is reachable. Once the remote end is unreachable, the local device terminates the tunnel connection, preventing data black holes.


#### Implementation

After the keepalive function is enabled on the source end of a GRE tunnel, the source end periodically sends keepalive messages to the destination end. If the destination end is reachable, the source end receives a response message from the destination end. Otherwise, no response message is received. The keepalive detection process is as follows:

1. After the keepalive function is enabled on the source end of a GRE tunnel, the source end creates a timer, periodically sends keepalive messages, and counts the number of failures to receive keepalive response messages. The unreachable counter increases by one each time a message is sent.
2. The destination end sends a response message to the source end each time it receives a keepalive message from the source end.
3. If the source end receives a response message before the number of sent keepalive messages reaches the *retry-times* value, the source end considers the destination end reachable and resets the number of sent keepalive messages. If the source does not receive any response message before the counter reaches the preset value, specifically, the retry times, the source considers the peer unreachable and resets the counter. Then, the source closes the tunnel connection.

![](public_sys-resources/note_3.0-en-us.png) 

The keepalive function takes effect on one end of a tunnel as long as it is configured on this end, regardless of whether it is configured on the other end. Once the destination end receives a keepalive message, it sends a response message to the source end, regardless of whether the keepalive function is configured on the destination end.



#### Benefits

The keepalive function can detect the tunnel status and prevent data loss if the remote end becomes unreachable, ensuring reliable data transmission.