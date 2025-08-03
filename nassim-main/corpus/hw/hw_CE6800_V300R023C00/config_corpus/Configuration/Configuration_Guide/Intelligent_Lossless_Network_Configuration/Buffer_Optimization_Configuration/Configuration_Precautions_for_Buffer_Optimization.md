Configuration Precautions for Buffer Optimization
=================================================

Configuration Precautions for Buffer Optimization

#### Licensing Requirements

Buffer optimization is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature | Feature Requirements | Series | Models |
| --- | --- | --- | --- |
| Distance-based Headroom Buffer Check | 1. The distance-based headroom buffer check function can measure the required headroom buffer space only when interfaces at both ends of a link are set to the long-distance mode and the link status of the interfaces is normal.  2. When the long-distance mode is enabled on too many interfaces, the headroom buffer space required by the interfaces is too large. However, the buffer space of the chip is limited, which may cause packet loss.  3. Automatic detection cannot be completed after the distance-based headroom buffer check function is enabled on an interface that is not in up state. Therefore, you are advised to manually trigger an interface to send detection packets after operations that may cause link status changes, such as interface initialization, interface rate switching, and interface split/aggregation.  4. If you run the display interface command to query statistics information on an interface after a device receives detection packets, the Ignoreds statistical item for the inbound direction in the command output contains the number of detection packets received by the device. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| Long-Distance Buffer Optimization | 1. The plane buffer optimization function and the burst traffic buffering mode are mutually exclusive.  2. After the plane buffer optimization mode is modified and takes effect, the configurations related to the buffer threshold, such as WRED, ECN, and ETS, may be affected. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Long-Distance Buffer Optimization | 1. The plane buffer optimization in enhanced long-distance and the burst traffic buffering mode are mutually exclusive.  2. After the plane buffer optimization in enhanced long-distance mode is modified and takes effect, configurations related to the buffer threshold, such as WRED, ECN, and ETS configurations, may be affected. | CE6800 series  CE8800 series | CE6860-SAN  CE8850-SAN |