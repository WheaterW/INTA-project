Configuration Precautions for Synchronization Ethernet
======================================================

Configuration Precautions for Synchronization Ethernet

#### Licensing Requirements

Synchronous Ethernet is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6855-48XS8CQ/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-P/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6885-48YS8CQ-T/CE6885-SAN-56F |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Ethernet clock synchronization can be configured on split interfaces. | CE6800 series | CE6855-48XS8CQ/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-P/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode) |
| The existing application of Ethernet clock synchronization is per hop. That is, all devices on the link must support Ethernet clock synchronization. Currently, a maximum of 20 hops are supported. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| When deploying a clock synchronization network, ensure that clock signals are not looped on the network. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| Only optical ports support Ethernet clock synchronization. After an optical interface with a copper module installed is changed to an electrical interface, the optical interface does not support Ethernet clock synchronization. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| Ethernet clock synchronization deployed on 40GE ports of the CE6866 does not take effect. Do not deploy Ethernet clock synchronization on 40GE ports (including auto-sensing 40GE ports) when deploying a clock synchronization network. | CE6800 series | CE6866-48S8CQ-P/CE6866-48S8CQ-K |