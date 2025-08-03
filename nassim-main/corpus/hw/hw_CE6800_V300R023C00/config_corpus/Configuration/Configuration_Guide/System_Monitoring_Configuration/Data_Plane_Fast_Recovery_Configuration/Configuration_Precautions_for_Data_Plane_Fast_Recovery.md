Configuration Precautions for Data Plane Fast Recovery
======================================================

Configuration Precautions for Data Plane Fast Recovery

#### Licensing Requirements

Data Plane Fast Recovery is under license control (CE-LIC-DPFR).


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F |
| CE8800 series | CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| All E2E devices on the entire network must support DPFR. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| VPN information cannot be distinguished. Therefore, the network segments of different VPNs cannot overlap. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| After DPFR is enabled globally and then on an interface, only the fault detection capability is enabled and the capability of sending advertisement packets to upstream devices is not limited. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| 1. DPFR does not take effect on trunk interfaces.  2. If the ECMP group contains trunk member interfaces or non-physical member interfaces in the outbound direction, DPFR does not take effect. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| DPFR fast switching cannot be configured with M-LAG access. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| DPFR cannot be configured on ECMP at the ingress or egress of any tunnel, including VXLAN tunnels. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| DPFR supports link switchover only once. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| After DPFR is enabled, the backup path of each NHP in UCMP is not selected based on the weight. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| DPFR and NSLB are mutually exclusive. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| DPFR takes effect only when the destination address is an IPv4 address. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| If the traffic triggers DPFR, the function of not decreasing the TTL by 1 does not take effect. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |