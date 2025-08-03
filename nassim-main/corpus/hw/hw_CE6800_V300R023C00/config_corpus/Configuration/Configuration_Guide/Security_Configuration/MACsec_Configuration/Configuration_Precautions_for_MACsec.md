Configuration Precautions for MACsec
====================================

Configuration Precautions for MACsec

#### Licensing Requirements

MACsec is controlled by the license (CE-LIC-MACSEC).


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Special packets are not encrypted. LLDP, MKA, 1588, and Pause packets are involved. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| For the CE6800 Series:  MACsec Interfaces  For the CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P:  25GE interfaces 1 to 16, 50GE interfaces 1 to 16, 100GE interfaces 1 to 8, 200GE interfaces 2/4/6/8, and 100GE interfaces 2/4/6/8 support MACsec after being split.  For the CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F:  8\*100G uplink ports support MACsec.  For the CE8800 Series:  MACsec Interfaces  For the CE8855-32CQ4BQ/CE8851-32CQ4BQ:  Ports 1 to 16  For the CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P:  100GE/200GE interfaces 1 to 4 and their converted interfaces + 400GE interfaces 1 to 4 and their converted interfaces. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| When an interface works in half-duplex mode, configuring MACsec may cause the MACsec links to be disconnected due to conflict.  Do not use MACsec in half-duplex mode. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| To connect to S series campus switches running V200, you need to run the undo macsec cipher-suite { gcm-aes-xpn-128 | gcm-aes-xpn-256} command. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| MACsec and PFC cannot be applied to the same interface. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| MACsec is configured on an interface and its peer, and the interface can receive mirrored packets from the observing port. If the mirrored packets contain MKA protocol packets, the interface can receive both MKA protocol packets and mirrored MKA protocol packets from the peer, as a result, the port identifies two peers (MI is different). The device does not support multi-point connections. As a result, the protocol cannot be established, and data traffic cannot be transmitted on the observing port. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| Packet loss may occur when the MACsec data-plane encryption algorithm is switched. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| By default, the basic software package does not support this feature. To use this feature, log in to Huawei technical support website, search for the corresponding product and version in the software download area, and download the MACsec feature package. For details about how to install the feature package, see "Upgrade Maintenance Configuration" in CLI Configuration Guide > System Management Configuration. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |