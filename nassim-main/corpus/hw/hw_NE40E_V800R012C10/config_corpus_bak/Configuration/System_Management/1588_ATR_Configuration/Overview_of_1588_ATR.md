Overview of 1588 ATR
====================

Overview_of_1588_ATR

#### Definition

1588 Adaptive Time Recovery (1588 ATR) is an adaptive time recovery algorithm based on PTP. It establishes clock links between Routers by sending Layer 3 unicast packets. Then, PTP packets are exchanged to achieve time synchronization over a third-party network between devices.

In 1588v2 time synchronization mode, devices on the entire network must support 1588v2 hop by hop. 1588 ATR can be used to implement time synchronization across devices that do not support 1588v2.

1588 ATR involves the server and client. The server provides 1588 ATR time synchronization for the client, and the client synchronizes with the server.

When the time server (such as the SSU2000) supports only the 1588v2 unicast negotiation mode, the client sends a negotiation request to the server, and the server sends time synchronization packets to the client after the negotiation is established. The client is configured with the 1588 ATR hop-by-hop mode and interconnected with the time server to achieve time synchronization in 1588v2 unicast negotiation mode. After that, the client can function as a BC to provide time synchronization for downstream gNodeBs.