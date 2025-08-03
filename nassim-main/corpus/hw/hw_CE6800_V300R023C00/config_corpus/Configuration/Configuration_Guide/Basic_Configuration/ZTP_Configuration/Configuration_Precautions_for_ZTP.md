Configuration Precautions for ZTP
=================================

Configuration Precautions for ZTP

#### Licensing Requirements

ZTP is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T |
| CE8800 series | CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The option fields in the downloaded intermediate file and script, and the user name, password, and version file name configured in the intermediate file cannot contain the following special characters: & > < " ' | · $ ; ( ) [ ] { } ~ \* ? ! \n # % , | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |
| Python 3 script. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |
| The Syslog server address is obtained through the Options field configured on the DHCP server, but not through the intermediate file. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |
| Syslog server with an IPv4 address | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |
| The device to be deployed must meet the following conditions:  1. The device runs with factory configurations.  2. You can view ZTP process logs after logging in to device through the console port.  3. You are not advised to modify device configurations during ZTP deployment. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |
| The Python script file must use a format supported by the Windows or Unix format. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |
| ZTP needs to be deployed on a private network because doing otherwise may cause security risks. In scenarios where security risks are uncontrollable, use the SZTP mode for deployment. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |
| 1. Device configuration will be modified during the deployment. Therefore, you need to check whether the configuration modified during the deployment is saved by mistake when you log in to the device and try to save the configuration.  2. In non-deployment scenarios, you are advised to save the configuration first to prevent the ZTP script from modifying the configuration. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |
| ZTP can be deployed through the management interface or service interface. However, deploying through the management interface is recommended. If the service interface is used for deployment, the device may be inaccessible due to triple-plane isolation (isolation between the service plane, management plane, and control plane). Therefore, you are advised to deploy ZTP in a secure networking environment. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |
| 1. For SZTP deployment, a device identity certificate must be preconfigured before delivery. The certificate is used for authentication between the device and bootstrap server and for TLS connection establishment.  2. The bootstrapping data sent from the bootstrap server may be encrypted using the public key of the device identity certificate. The device needs to decrypt the bootstrapping data using the private key of the device identity certificate. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |
| Service interfaces are used for ZTP, but this deployment mode may cause isolation of the service plane, management plane, and control plane. Security hardening has been performed on the system by default during deployment. Users need to perform deployment in a secure networking environment. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6885-48YS8CQ-T  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM |