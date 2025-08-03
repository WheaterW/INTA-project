Configuration Precautions for OAS
=================================

Configuration Precautions for OAS

#### Licensing Requirements

OAS Development Guide is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6863H-48S6CQ/CE6863H-48S6CQ-K |
| CE8800 series | CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The container image software package cannot be upgraded without service interruption. During the upgrade of the container image software package, container services are interrupted. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| A maximum of 1024 handles and 256 processes can be created for services in a container. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| The container Guest Shell allows only one user to log in at a time. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| After a user logs in to the container Guest Shell, the user automatically exits the container Guest Shell if the idle time exceeds 10 minutes. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| A maximum of 20 third-party public keys can be installed. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| The Open GnuPG tool can be used to generate keys. Only the RSA algorithm is supported. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| After the OAS function is enabled, the container daemon process occupies 60 MB memory, and the container instance with no running service occupies 10 MB memory. Therefore, it is recommended that the total reserved physical memory be less than or equal to 30% of the total physical memory. The formula is as follows: Total reserved physical memory = 60 + (Memory required by third-party containers + 10) x Number of containers. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| A maximum of eight applications can be deployed in an open system. The number of applications that can be deployed on a device depends on the board performance and resource consumption of applications. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| 1. A maximum of eight source IP addresses can be configured for the open system.  2. A maximum of one IP address can be configured for the open system management port.  3. A maximum of one destination IP address can be configured for east-west communication of the open system. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| 1. By default, the basic software package does not support this feature. To use this feature, log in to the Huawei technical support website, search for the corresponding product and version in the software download area, and download the OAS feature package. For details about how to install the feature package, see "Upgrade Maintenance Configuration" in Configuration Guide > System Management Configuration.  2. The OAS feature package can be upgraded or downgraded. Before downgrading the feature package, save the CFG configuration. Otherwise, the configuration may be lost after the downgrade. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| Once an instance is started, the network configuration of the instance cannot be modified. You can modify the network parameters in either of the following ways:  1) Delete the application and reconfigure network parameters.  2) Stop the application, cancel the configured run-options, and reconfigure it. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |