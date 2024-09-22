from __future__ import annotations
from enum import Enum
from datetime import datetime


class CurrentInstanceBootMode(Enum):
    LEGACYBIOS = 'legacy-bios'
    UEFI = 'uefi'


class AutoRecovery(Enum):
    DISABLED = 'disabled'
    DEFAULT = 'default'


class HostnameType(Enum):
    IPNAME = 'ip-name'
    RESOURCENAME = 'resource-name'


class BootMode(Enum):
    LEGACYBIOS = 'legacy-bios'
    UEFI = 'uefi'
    UEFIPREFERRED = 'uefi-preferred'


class InstanceMetadataTags(Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'


class HttpProtocolIpv6(Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'


class HttpEndpoint(Enum):
    DISABLED = 'disabled'
    ENABLED = 'enabled'


class HttpTokens(Enum):
    OPTIONAL = 'optional'
    REQUIRED = 'required'


class MetadataOptionsState(Enum):
    PENDING = 'pending'
    APPLIED = 'applied'


class CapacityReservationPreference(Enum):
    OPEN = 'open'
    NONE = 'none'


class AmdSevSnp(Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'


class VirtualizationType(Enum):
    HVM = 'hvm'
    PARAVIRTUAL = 'paravirtual'


class RootDeviceType(Enum):
    EBS = 'ebs'
    INSTANCESTORE = 'instance-store'


class NetworkInterfacesStatus(Enum):
    AVAILABLE = 'available'
    ASSOCIATED = 'associated'
    ATTACHING = 'attaching'
    INUSE = 'in-use'
    DETACHING = 'detaching'


class AttachmentStatus(Enum):
    ATTACHING = 'attaching'
    ATTACHED = 'attached'
    DETACHING = 'detaching'
    DETACHED = 'detached'


class InstanceLifecycle(Enum):
    SPOT = 'spot'
    SCHEDULED = 'scheduled'
    CAPACITYBLOCK = 'capacity-block'


class Hypervisor(Enum):
    OVM = 'ovm'
    XEN = 'xen'


class EbsStatus(Enum):
    ATTACHING = 'attaching'
    ATTACHED = 'attached'
    DETACHING = 'detaching'
    DETACHED = 'detached'


class Architecture(Enum):
    I386 = 'i386'
    X86_64 = 'x86_64'
    ARM64 = 'arm64'
    X86_64_MAC = 'x86_64_mac'
    ARM64_MAC = 'arm64_mac'


class Name(Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    SHUTTINGDOWN = 'shutting-down'
    TERMINATED = 'terminated'
    STOPPING = 'stopping'
    STOPPED = 'stopped'


class ProductCodeType(Enum):
    DEVPAY = 'devpay'
    MARKETPLACE = 'marketplace'


class Tenancy(Enum):
    DEFAULT = 'default'
    DEDICATED = 'dedicated'
    HOST = 'host'


class MonitoringState(Enum):
    DISABLED = 'disabled'
    DISABLING = 'disabling'
    ENABLED = 'enabled'
    PENDING = 'pending'


class InstanceType(Enum):
    A1MEDIUM = 'a1.medium'
    A1LARGE = 'a1.large'
    A1XLARGE = 'a1.xlarge'
    A12XLARGE = 'a1.2xlarge'
    A14XLARGE = 'a1.4xlarge'
    A1METAL = 'a1.metal'
    C1MEDIUM = 'c1.medium'
    C1XLARGE = 'c1.xlarge'
    C3LARGE = 'c3.large'
    C3XLARGE = 'c3.xlarge'
    C32XLARGE = 'c3.2xlarge'
    C34XLARGE = 'c3.4xlarge'
    C38XLARGE = 'c3.8xlarge'
    C4LARGE = 'c4.large'
    C4XLARGE = 'c4.xlarge'
    C42XLARGE = 'c4.2xlarge'
    C44XLARGE = 'c4.4xlarge'
    C48XLARGE = 'c4.8xlarge'
    C5LARGE = 'c5.large'
    C5XLARGE = 'c5.xlarge'
    C52XLARGE = 'c5.2xlarge'
    C54XLARGE = 'c5.4xlarge'
    C59XLARGE = 'c5.9xlarge'
    C512XLARGE = 'c5.12xlarge'
    C518XLARGE = 'c5.18xlarge'
    C524XLARGE = 'c5.24xlarge'
    C5METAL = 'c5.metal'
    C5ALARGE = 'c5a.large'
    C5AXLARGE = 'c5a.xlarge'
    C5A2XLARGE = 'c5a.2xlarge'
    C5A4XLARGE = 'c5a.4xlarge'
    C5A8XLARGE = 'c5a.8xlarge'
    C5A12XLARGE = 'c5a.12xlarge'
    C5A16XLARGE = 'c5a.16xlarge'
    C5A24XLARGE = 'c5a.24xlarge'
    C5ADLARGE = 'c5ad.large'
    C5ADXLARGE = 'c5ad.xlarge'
    C5AD2XLARGE = 'c5ad.2xlarge'
    C5AD4XLARGE = 'c5ad.4xlarge'
    C5AD8XLARGE = 'c5ad.8xlarge'
    C5AD12XLARGE = 'c5ad.12xlarge'
    C5AD16XLARGE = 'c5ad.16xlarge'
    C5AD24XLARGE = 'c5ad.24xlarge'
    C5DLARGE = 'c5d.large'
    C5DXLARGE = 'c5d.xlarge'
    C5D2XLARGE = 'c5d.2xlarge'
    C5D4XLARGE = 'c5d.4xlarge'
    C5D9XLARGE = 'c5d.9xlarge'
    C5D12XLARGE = 'c5d.12xlarge'
    C5D18XLARGE = 'c5d.18xlarge'
    C5D24XLARGE = 'c5d.24xlarge'
    C5DMETAL = 'c5d.metal'
    C5NLARGE = 'c5n.large'
    C5NXLARGE = 'c5n.xlarge'
    C5N2XLARGE = 'c5n.2xlarge'
    C5N4XLARGE = 'c5n.4xlarge'
    C5N9XLARGE = 'c5n.9xlarge'
    C5N18XLARGE = 'c5n.18xlarge'
    C5NMETAL = 'c5n.metal'
    C6GMEDIUM = 'c6g.medium'
    C6GLARGE = 'c6g.large'
    C6GXLARGE = 'c6g.xlarge'
    C6G2XLARGE = 'c6g.2xlarge'
    C6G4XLARGE = 'c6g.4xlarge'
    C6G8XLARGE = 'c6g.8xlarge'
    C6G12XLARGE = 'c6g.12xlarge'
    C6G16XLARGE = 'c6g.16xlarge'
    C6GMETAL = 'c6g.metal'
    C6GDMEDIUM = 'c6gd.medium'
    C6GDLARGE = 'c6gd.large'
    C6GDXLARGE = 'c6gd.xlarge'
    C6GD2XLARGE = 'c6gd.2xlarge'
    C6GD4XLARGE = 'c6gd.4xlarge'
    C6GD8XLARGE = 'c6gd.8xlarge'
    C6GD12XLARGE = 'c6gd.12xlarge'
    C6GD16XLARGE = 'c6gd.16xlarge'
    C6GDMETAL = 'c6gd.metal'
    C6GNMEDIUM = 'c6gn.medium'
    C6GNLARGE = 'c6gn.large'
    C6GNXLARGE = 'c6gn.xlarge'
    C6GN2XLARGE = 'c6gn.2xlarge'
    C6GN4XLARGE = 'c6gn.4xlarge'
    C6GN8XLARGE = 'c6gn.8xlarge'
    C6GN12XLARGE = 'c6gn.12xlarge'
    C6GN16XLARGE = 'c6gn.16xlarge'
    C6ILARGE = 'c6i.large'
    C6IXLARGE = 'c6i.xlarge'
    C6I2XLARGE = 'c6i.2xlarge'
    C6I4XLARGE = 'c6i.4xlarge'
    C6I8XLARGE = 'c6i.8xlarge'
    C6I12XLARGE = 'c6i.12xlarge'
    C6I16XLARGE = 'c6i.16xlarge'
    C6I24XLARGE = 'c6i.24xlarge'
    C6I32XLARGE = 'c6i.32xlarge'
    C6IMETAL = 'c6i.metal'
    CC14XLARGE = 'cc1.4xlarge'
    CC28XLARGE = 'cc2.8xlarge'
    CG14XLARGE = 'cg1.4xlarge'
    CR18XLARGE = 'cr1.8xlarge'
    D2XLARGE = 'd2.xlarge'
    D22XLARGE = 'd2.2xlarge'
    D24XLARGE = 'd2.4xlarge'
    D28XLARGE = 'd2.8xlarge'
    D3XLARGE = 'd3.xlarge'
    D32XLARGE = 'd3.2xlarge'
    D34XLARGE = 'd3.4xlarge'
    D38XLARGE = 'd3.8xlarge'
    D3ENXLARGE = 'd3en.xlarge'
    D3EN2XLARGE = 'd3en.2xlarge'
    D3EN4XLARGE = 'd3en.4xlarge'
    D3EN6XLARGE = 'd3en.6xlarge'
    D3EN8XLARGE = 'd3en.8xlarge'
    D3EN12XLARGE = 'd3en.12xlarge'
    DL124XLARGE = 'dl1.24xlarge'
    F12XLARGE = 'f1.2xlarge'
    F14XLARGE = 'f1.4xlarge'
    F116XLARGE = 'f1.16xlarge'
    G22XLARGE = 'g2.2xlarge'
    G28XLARGE = 'g2.8xlarge'
    G34XLARGE = 'g3.4xlarge'
    G38XLARGE = 'g3.8xlarge'
    G316XLARGE = 'g3.16xlarge'
    G3SXLARGE = 'g3s.xlarge'
    G4ADXLARGE = 'g4ad.xlarge'
    G4AD2XLARGE = 'g4ad.2xlarge'
    G4AD4XLARGE = 'g4ad.4xlarge'
    G4AD8XLARGE = 'g4ad.8xlarge'
    G4AD16XLARGE = 'g4ad.16xlarge'
    G4DNXLARGE = 'g4dn.xlarge'
    G4DN2XLARGE = 'g4dn.2xlarge'
    G4DN4XLARGE = 'g4dn.4xlarge'
    G4DN8XLARGE = 'g4dn.8xlarge'
    G4DN12XLARGE = 'g4dn.12xlarge'
    G4DN16XLARGE = 'g4dn.16xlarge'
    G4DNMETAL = 'g4dn.metal'
    G5XLARGE = 'g5.xlarge'
    G52XLARGE = 'g5.2xlarge'
    G54XLARGE = 'g5.4xlarge'
    G58XLARGE = 'g5.8xlarge'
    G512XLARGE = 'g5.12xlarge'
    G516XLARGE = 'g5.16xlarge'
    G524XLARGE = 'g5.24xlarge'
    G548XLARGE = 'g5.48xlarge'
    G5GXLARGE = 'g5g.xlarge'
    G5G2XLARGE = 'g5g.2xlarge'
    G5G4XLARGE = 'g5g.4xlarge'
    G5G8XLARGE = 'g5g.8xlarge'
    G5G16XLARGE = 'g5g.16xlarge'
    G5GMETAL = 'g5g.metal'
    HI14XLARGE = 'hi1.4xlarge'
    HPC6A48XLARGE = 'hpc6a.48xlarge'
    HS18XLARGE = 'hs1.8xlarge'
    H12XLARGE = 'h1.2xlarge'
    H14XLARGE = 'h1.4xlarge'
    H18XLARGE = 'h1.8xlarge'
    H116XLARGE = 'h1.16xlarge'
    I2XLARGE = 'i2.xlarge'
    I22XLARGE = 'i2.2xlarge'
    I24XLARGE = 'i2.4xlarge'
    I28XLARGE = 'i2.8xlarge'
    I3LARGE = 'i3.large'
    I3XLARGE = 'i3.xlarge'
    I32XLARGE = 'i3.2xlarge'
    I34XLARGE = 'i3.4xlarge'
    I38XLARGE = 'i3.8xlarge'
    I316XLARGE = 'i3.16xlarge'
    I3METAL = 'i3.metal'
    I3ENLARGE = 'i3en.large'
    I3ENXLARGE = 'i3en.xlarge'
    I3EN2XLARGE = 'i3en.2xlarge'
    I3EN3XLARGE = 'i3en.3xlarge'
    I3EN6XLARGE = 'i3en.6xlarge'
    I3EN12XLARGE = 'i3en.12xlarge'
    I3EN24XLARGE = 'i3en.24xlarge'
    I3ENMETAL = 'i3en.metal'
    IM4GNLARGE = 'im4gn.large'
    IM4GNXLARGE = 'im4gn.xlarge'
    IM4GN2XLARGE = 'im4gn.2xlarge'
    IM4GN4XLARGE = 'im4gn.4xlarge'
    IM4GN8XLARGE = 'im4gn.8xlarge'
    IM4GN16XLARGE = 'im4gn.16xlarge'
    INF1XLARGE = 'inf1.xlarge'
    INF12XLARGE = 'inf1.2xlarge'
    INF16XLARGE = 'inf1.6xlarge'
    INF124XLARGE = 'inf1.24xlarge'
    IS4GENMEDIUM = 'is4gen.medium'
    IS4GENLARGE = 'is4gen.large'
    IS4GENXLARGE = 'is4gen.xlarge'
    IS4GEN2XLARGE = 'is4gen.2xlarge'
    IS4GEN4XLARGE = 'is4gen.4xlarge'
    IS4GEN8XLARGE = 'is4gen.8xlarge'
    M1SMALL = 'm1.small'
    M1MEDIUM = 'm1.medium'
    M1LARGE = 'm1.large'
    M1XLARGE = 'm1.xlarge'
    M2XLARGE = 'm2.xlarge'
    M22XLARGE = 'm2.2xlarge'
    M24XLARGE = 'm2.4xlarge'
    M3MEDIUM = 'm3.medium'
    M3LARGE = 'm3.large'
    M3XLARGE = 'm3.xlarge'
    M32XLARGE = 'm3.2xlarge'
    M4LARGE = 'm4.large'
    M4XLARGE = 'm4.xlarge'
    M42XLARGE = 'm4.2xlarge'
    M44XLARGE = 'm4.4xlarge'
    M410XLARGE = 'm4.10xlarge'
    M416XLARGE = 'm4.16xlarge'
    M5LARGE = 'm5.large'
    M5XLARGE = 'm5.xlarge'
    M52XLARGE = 'm5.2xlarge'
    M54XLARGE = 'm5.4xlarge'
    M58XLARGE = 'm5.8xlarge'
    M512XLARGE = 'm5.12xlarge'
    M516XLARGE = 'm5.16xlarge'
    M524XLARGE = 'm5.24xlarge'
    M5METAL = 'm5.metal'
    M5ALARGE = 'm5a.large'
    M5AXLARGE = 'm5a.xlarge'
    M5A2XLARGE = 'm5a.2xlarge'
    M5A4XLARGE = 'm5a.4xlarge'
    M5A8XLARGE = 'm5a.8xlarge'
    M5A12XLARGE = 'm5a.12xlarge'
    M5A16XLARGE = 'm5a.16xlarge'
    M5A24XLARGE = 'm5a.24xlarge'
    M5ADLARGE = 'm5ad.large'
    M5ADXLARGE = 'm5ad.xlarge'
    M5AD2XLARGE = 'm5ad.2xlarge'
    M5AD4XLARGE = 'm5ad.4xlarge'
    M5AD8XLARGE = 'm5ad.8xlarge'
    M5AD12XLARGE = 'm5ad.12xlarge'
    M5AD16XLARGE = 'm5ad.16xlarge'
    M5AD24XLARGE = 'm5ad.24xlarge'
    M5DLARGE = 'm5d.large'
    M5DXLARGE = 'm5d.xlarge'
    M5D2XLARGE = 'm5d.2xlarge'
    M5D4XLARGE = 'm5d.4xlarge'
    M5D8XLARGE = 'm5d.8xlarge'
    M5D12XLARGE = 'm5d.12xlarge'
    M5D16XLARGE = 'm5d.16xlarge'
    M5D24XLARGE = 'm5d.24xlarge'
    M5DMETAL = 'm5d.metal'
    M5DNLARGE = 'm5dn.large'
    M5DNXLARGE = 'm5dn.xlarge'
    M5DN2XLARGE = 'm5dn.2xlarge'
    M5DN4XLARGE = 'm5dn.4xlarge'
    M5DN8XLARGE = 'm5dn.8xlarge'
    M5DN12XLARGE = 'm5dn.12xlarge'
    M5DN16XLARGE = 'm5dn.16xlarge'
    M5DN24XLARGE = 'm5dn.24xlarge'
    M5DNMETAL = 'm5dn.metal'
    M5NLARGE = 'm5n.large'
    M5NXLARGE = 'm5n.xlarge'
    M5N2XLARGE = 'm5n.2xlarge'
    M5N4XLARGE = 'm5n.4xlarge'
    M5N8XLARGE = 'm5n.8xlarge'
    M5N12XLARGE = 'm5n.12xlarge'
    M5N16XLARGE = 'm5n.16xlarge'
    M5N24XLARGE = 'm5n.24xlarge'
    M5NMETAL = 'm5n.metal'
    M5ZNLARGE = 'm5zn.large'
    M5ZNXLARGE = 'm5zn.xlarge'
    M5ZN2XLARGE = 'm5zn.2xlarge'
    M5ZN3XLARGE = 'm5zn.3xlarge'
    M5ZN6XLARGE = 'm5zn.6xlarge'
    M5ZN12XLARGE = 'm5zn.12xlarge'
    M5ZNMETAL = 'm5zn.metal'
    M6ALARGE = 'm6a.large'
    M6AXLARGE = 'm6a.xlarge'
    M6A2XLARGE = 'm6a.2xlarge'
    M6A4XLARGE = 'm6a.4xlarge'
    M6A8XLARGE = 'm6a.8xlarge'
    M6A12XLARGE = 'm6a.12xlarge'
    M6A16XLARGE = 'm6a.16xlarge'
    M6A24XLARGE = 'm6a.24xlarge'
    M6A32XLARGE = 'm6a.32xlarge'
    M6A48XLARGE = 'm6a.48xlarge'
    M6GMETAL = 'm6g.metal'
    M6GMEDIUM = 'm6g.medium'
    M6GLARGE = 'm6g.large'
    M6GXLARGE = 'm6g.xlarge'
    M6G2XLARGE = 'm6g.2xlarge'
    M6G4XLARGE = 'm6g.4xlarge'
    M6G8XLARGE = 'm6g.8xlarge'
    M6G12XLARGE = 'm6g.12xlarge'
    M6G16XLARGE = 'm6g.16xlarge'
    M6GDMETAL = 'm6gd.metal'
    M6GDMEDIUM = 'm6gd.medium'
    M6GDLARGE = 'm6gd.large'
    M6GDXLARGE = 'm6gd.xlarge'
    M6GD2XLARGE = 'm6gd.2xlarge'
    M6GD4XLARGE = 'm6gd.4xlarge'
    M6GD8XLARGE = 'm6gd.8xlarge'
    M6GD12XLARGE = 'm6gd.12xlarge'
    M6GD16XLARGE = 'm6gd.16xlarge'
    M6ILARGE = 'm6i.large'
    M6IXLARGE = 'm6i.xlarge'
    M6I2XLARGE = 'm6i.2xlarge'
    M6I4XLARGE = 'm6i.4xlarge'
    M6I8XLARGE = 'm6i.8xlarge'
    M6I12XLARGE = 'm6i.12xlarge'
    M6I16XLARGE = 'm6i.16xlarge'
    M6I24XLARGE = 'm6i.24xlarge'
    M6I32XLARGE = 'm6i.32xlarge'
    M6IMETAL = 'm6i.metal'
    MAC1METAL = 'mac1.metal'
    P2XLARGE = 'p2.xlarge'
    P28XLARGE = 'p2.8xlarge'
    P216XLARGE = 'p2.16xlarge'
    P32XLARGE = 'p3.2xlarge'
    P38XLARGE = 'p3.8xlarge'
    P316XLARGE = 'p3.16xlarge'
    P3DN24XLARGE = 'p3dn.24xlarge'
    P4D24XLARGE = 'p4d.24xlarge'
    R3LARGE = 'r3.large'
    R3XLARGE = 'r3.xlarge'
    R32XLARGE = 'r3.2xlarge'
    R34XLARGE = 'r3.4xlarge'
    R38XLARGE = 'r3.8xlarge'
    R4LARGE = 'r4.large'
    R4XLARGE = 'r4.xlarge'
    R42XLARGE = 'r4.2xlarge'
    R44XLARGE = 'r4.4xlarge'
    R48XLARGE = 'r4.8xlarge'
    R416XLARGE = 'r4.16xlarge'
    R5LARGE = 'r5.large'
    R5XLARGE = 'r5.xlarge'
    R52XLARGE = 'r5.2xlarge'
    R54XLARGE = 'r5.4xlarge'
    R58XLARGE = 'r5.8xlarge'
    R512XLARGE = 'r5.12xlarge'
    R516XLARGE = 'r5.16xlarge'
    R524XLARGE = 'r5.24xlarge'
    R5METAL = 'r5.metal'
    R5ALARGE = 'r5a.large'
    R5AXLARGE = 'r5a.xlarge'
    R5A2XLARGE = 'r5a.2xlarge'
    R5A4XLARGE = 'r5a.4xlarge'
    R5A8XLARGE = 'r5a.8xlarge'
    R5A12XLARGE = 'r5a.12xlarge'
    R5A16XLARGE = 'r5a.16xlarge'
    R5A24XLARGE = 'r5a.24xlarge'
    R5ADLARGE = 'r5ad.large'
    R5ADXLARGE = 'r5ad.xlarge'
    R5AD2XLARGE = 'r5ad.2xlarge'
    R5AD4XLARGE = 'r5ad.4xlarge'
    R5AD8XLARGE = 'r5ad.8xlarge'
    R5AD12XLARGE = 'r5ad.12xlarge'
    R5AD16XLARGE = 'r5ad.16xlarge'
    R5AD24XLARGE = 'r5ad.24xlarge'
    R5BLARGE = 'r5b.large'
    R5BXLARGE = 'r5b.xlarge'
    R5B2XLARGE = 'r5b.2xlarge'
    R5B4XLARGE = 'r5b.4xlarge'
    R5B8XLARGE = 'r5b.8xlarge'
    R5B12XLARGE = 'r5b.12xlarge'
    R5B16XLARGE = 'r5b.16xlarge'
    R5B24XLARGE = 'r5b.24xlarge'
    R5BMETAL = 'r5b.metal'
    R5DLARGE = 'r5d.large'
    R5DXLARGE = 'r5d.xlarge'
    R5D2XLARGE = 'r5d.2xlarge'
    R5D4XLARGE = 'r5d.4xlarge'
    R5D8XLARGE = 'r5d.8xlarge'
    R5D12XLARGE = 'r5d.12xlarge'
    R5D16XLARGE = 'r5d.16xlarge'
    R5D24XLARGE = 'r5d.24xlarge'
    R5DMETAL = 'r5d.metal'
    R5DNLARGE = 'r5dn.large'
    R5DNXLARGE = 'r5dn.xlarge'
    R5DN2XLARGE = 'r5dn.2xlarge'
    R5DN4XLARGE = 'r5dn.4xlarge'
    R5DN8XLARGE = 'r5dn.8xlarge'
    R5DN12XLARGE = 'r5dn.12xlarge'
    R5DN16XLARGE = 'r5dn.16xlarge'
    R5DN24XLARGE = 'r5dn.24xlarge'
    R5DNMETAL = 'r5dn.metal'
    R5NLARGE = 'r5n.large'
    R5NXLARGE = 'r5n.xlarge'
    R5N2XLARGE = 'r5n.2xlarge'
    R5N4XLARGE = 'r5n.4xlarge'
    R5N8XLARGE = 'r5n.8xlarge'
    R5N12XLARGE = 'r5n.12xlarge'
    R5N16XLARGE = 'r5n.16xlarge'
    R5N24XLARGE = 'r5n.24xlarge'
    R5NMETAL = 'r5n.metal'
    R6GMEDIUM = 'r6g.medium'
    R6GLARGE = 'r6g.large'
    R6GXLARGE = 'r6g.xlarge'
    R6G2XLARGE = 'r6g.2xlarge'
    R6G4XLARGE = 'r6g.4xlarge'
    R6G8XLARGE = 'r6g.8xlarge'
    R6G12XLARGE = 'r6g.12xlarge'
    R6G16XLARGE = 'r6g.16xlarge'
    R6GMETAL = 'r6g.metal'
    R6GDMEDIUM = 'r6gd.medium'
    R6GDLARGE = 'r6gd.large'
    R6GDXLARGE = 'r6gd.xlarge'
    R6GD2XLARGE = 'r6gd.2xlarge'
    R6GD4XLARGE = 'r6gd.4xlarge'
    R6GD8XLARGE = 'r6gd.8xlarge'
    R6GD12XLARGE = 'r6gd.12xlarge'
    R6GD16XLARGE = 'r6gd.16xlarge'
    R6GDMETAL = 'r6gd.metal'
    R6ILARGE = 'r6i.large'
    R6IXLARGE = 'r6i.xlarge'
    R6I2XLARGE = 'r6i.2xlarge'
    R6I4XLARGE = 'r6i.4xlarge'
    R6I8XLARGE = 'r6i.8xlarge'
    R6I12XLARGE = 'r6i.12xlarge'
    R6I16XLARGE = 'r6i.16xlarge'
    R6I24XLARGE = 'r6i.24xlarge'
    R6I32XLARGE = 'r6i.32xlarge'
    R6IMETAL = 'r6i.metal'
    T1MICRO = 't1.micro'
    T2NANO = 't2.nano'
    T2MICRO = 't2.micro'
    T2SMALL = 't2.small'
    T2MEDIUM = 't2.medium'
    T2LARGE = 't2.large'
    T2XLARGE = 't2.xlarge'
    T22XLARGE = 't2.2xlarge'
    T3NANO = 't3.nano'
    T3MICRO = 't3.micro'
    T3SMALL = 't3.small'
    T3MEDIUM = 't3.medium'
    T3LARGE = 't3.large'
    T3XLARGE = 't3.xlarge'
    T32XLARGE = 't3.2xlarge'
    T3ANANO = 't3a.nano'
    T3AMICRO = 't3a.micro'
    T3ASMALL = 't3a.small'
    T3AMEDIUM = 't3a.medium'
    T3ALARGE = 't3a.large'
    T3AXLARGE = 't3a.xlarge'
    T3A2XLARGE = 't3a.2xlarge'
    T4GNANO = 't4g.nano'
    T4GMICRO = 't4g.micro'
    T4GSMALL = 't4g.small'
    T4GMEDIUM = 't4g.medium'
    T4GLARGE = 't4g.large'
    T4GXLARGE = 't4g.xlarge'
    T4G2XLARGE = 't4g.2xlarge'
    U6TB156XLARGE = 'u-6tb1.56xlarge'
    U6TB1112XLARGE = 'u-6tb1.112xlarge'
    U9TB1112XLARGE = 'u-9tb1.112xlarge'
    U12TB1112XLARGE = 'u-12tb1.112xlarge'
    U6TB1METAL = 'u-6tb1.metal'
    U9TB1METAL = 'u-9tb1.metal'
    U12TB1METAL = 'u-12tb1.metal'
    U18TB1METAL = 'u-18tb1.metal'
    U24TB1METAL = 'u-24tb1.metal'
    VT13XLARGE = 'vt1.3xlarge'
    VT16XLARGE = 'vt1.6xlarge'
    VT124XLARGE = 'vt1.24xlarge'
    X116XLARGE = 'x1.16xlarge'
    X132XLARGE = 'x1.32xlarge'
    X1EXLARGE = 'x1e.xlarge'
    X1E2XLARGE = 'x1e.2xlarge'
    X1E4XLARGE = 'x1e.4xlarge'
    X1E8XLARGE = 'x1e.8xlarge'
    X1E16XLARGE = 'x1e.16xlarge'
    X1E32XLARGE = 'x1e.32xlarge'
    X2IEZN2XLARGE = 'x2iezn.2xlarge'
    X2IEZN4XLARGE = 'x2iezn.4xlarge'
    X2IEZN6XLARGE = 'x2iezn.6xlarge'
    X2IEZN8XLARGE = 'x2iezn.8xlarge'
    X2IEZN12XLARGE = 'x2iezn.12xlarge'
    X2IEZNMETAL = 'x2iezn.metal'
    X2GDMEDIUM = 'x2gd.medium'
    X2GDLARGE = 'x2gd.large'
    X2GDXLARGE = 'x2gd.xlarge'
    X2GD2XLARGE = 'x2gd.2xlarge'
    X2GD4XLARGE = 'x2gd.4xlarge'
    X2GD8XLARGE = 'x2gd.8xlarge'
    X2GD12XLARGE = 'x2gd.12xlarge'
    X2GD16XLARGE = 'x2gd.16xlarge'
    X2GDMETAL = 'x2gd.metal'
    Z1DLARGE = 'z1d.large'
    Z1DXLARGE = 'z1d.xlarge'
    Z1D2XLARGE = 'z1d.2xlarge'
    Z1D3XLARGE = 'z1d.3xlarge'
    Z1D6XLARGE = 'z1d.6xlarge'
    Z1D12XLARGE = 'z1d.12xlarge'
    Z1DMETAL = 'z1d.metal'
    X2IDN16XLARGE = 'x2idn.16xlarge'
    X2IDN24XLARGE = 'x2idn.24xlarge'
    X2IDN32XLARGE = 'x2idn.32xlarge'
    X2IEDNXLARGE = 'x2iedn.xlarge'
    X2IEDN2XLARGE = 'x2iedn.2xlarge'
    X2IEDN4XLARGE = 'x2iedn.4xlarge'
    X2IEDN8XLARGE = 'x2iedn.8xlarge'
    X2IEDN16XLARGE = 'x2iedn.16xlarge'
    X2IEDN24XLARGE = 'x2iedn.24xlarge'
    X2IEDN32XLARGE = 'x2iedn.32xlarge'
    C6ALARGE = 'c6a.large'
    C6AXLARGE = 'c6a.xlarge'
    C6A2XLARGE = 'c6a.2xlarge'
    C6A4XLARGE = 'c6a.4xlarge'
    C6A8XLARGE = 'c6a.8xlarge'
    C6A12XLARGE = 'c6a.12xlarge'
    C6A16XLARGE = 'c6a.16xlarge'
    C6A24XLARGE = 'c6a.24xlarge'
    C6A32XLARGE = 'c6a.32xlarge'
    C6A48XLARGE = 'c6a.48xlarge'
    C6AMETAL = 'c6a.metal'
    M6AMETAL = 'm6a.metal'
    I4ILARGE = 'i4i.large'
    I4IXLARGE = 'i4i.xlarge'
    I4I2XLARGE = 'i4i.2xlarge'
    I4I4XLARGE = 'i4i.4xlarge'
    I4I8XLARGE = 'i4i.8xlarge'
    I4I16XLARGE = 'i4i.16xlarge'
    I4I32XLARGE = 'i4i.32xlarge'
    I4IMETAL = 'i4i.metal'
    X2IDNMETAL = 'x2idn.metal'
    X2IEDNMETAL = 'x2iedn.metal'
    C7GMEDIUM = 'c7g.medium'
    C7GLARGE = 'c7g.large'
    C7GXLARGE = 'c7g.xlarge'
    C7G2XLARGE = 'c7g.2xlarge'
    C7G4XLARGE = 'c7g.4xlarge'
    C7G8XLARGE = 'c7g.8xlarge'
    C7G12XLARGE = 'c7g.12xlarge'
    C7G16XLARGE = 'c7g.16xlarge'
    MAC2METAL = 'mac2.metal'
    C6IDLARGE = 'c6id.large'
    C6IDXLARGE = 'c6id.xlarge'
    C6ID2XLARGE = 'c6id.2xlarge'
    C6ID4XLARGE = 'c6id.4xlarge'
    C6ID8XLARGE = 'c6id.8xlarge'
    C6ID12XLARGE = 'c6id.12xlarge'
    C6ID16XLARGE = 'c6id.16xlarge'
    C6ID24XLARGE = 'c6id.24xlarge'
    C6ID32XLARGE = 'c6id.32xlarge'
    C6IDMETAL = 'c6id.metal'
    M6IDLARGE = 'm6id.large'
    M6IDXLARGE = 'm6id.xlarge'
    M6ID2XLARGE = 'm6id.2xlarge'
    M6ID4XLARGE = 'm6id.4xlarge'
    M6ID8XLARGE = 'm6id.8xlarge'
    M6ID12XLARGE = 'm6id.12xlarge'
    M6ID16XLARGE = 'm6id.16xlarge'
    M6ID24XLARGE = 'm6id.24xlarge'
    M6ID32XLARGE = 'm6id.32xlarge'
    M6IDMETAL = 'm6id.metal'
    R6IDLARGE = 'r6id.large'
    R6IDXLARGE = 'r6id.xlarge'
    R6ID2XLARGE = 'r6id.2xlarge'
    R6ID4XLARGE = 'r6id.4xlarge'
    R6ID8XLARGE = 'r6id.8xlarge'
    R6ID12XLARGE = 'r6id.12xlarge'
    R6ID16XLARGE = 'r6id.16xlarge'
    R6ID24XLARGE = 'r6id.24xlarge'
    R6ID32XLARGE = 'r6id.32xlarge'
    R6IDMETAL = 'r6id.metal'
    R6ALARGE = 'r6a.large'
    R6AXLARGE = 'r6a.xlarge'
    R6A2XLARGE = 'r6a.2xlarge'
    R6A4XLARGE = 'r6a.4xlarge'
    R6A8XLARGE = 'r6a.8xlarge'
    R6A12XLARGE = 'r6a.12xlarge'
    R6A16XLARGE = 'r6a.16xlarge'
    R6A24XLARGE = 'r6a.24xlarge'
    R6A32XLARGE = 'r6a.32xlarge'
    R6A48XLARGE = 'r6a.48xlarge'
    R6AMETAL = 'r6a.metal'
    P4DE24XLARGE = 'p4de.24xlarge'
    U3TB156XLARGE = 'u-3tb1.56xlarge'
    U18TB1112XLARGE = 'u-18tb1.112xlarge'
    U24TB1112XLARGE = 'u-24tb1.112xlarge'
    TRN12XLARGE = 'trn1.2xlarge'
    TRN132XLARGE = 'trn1.32xlarge'
    HPC6ID32XLARGE = 'hpc6id.32xlarge'
    C6INLARGE = 'c6in.large'
    C6INXLARGE = 'c6in.xlarge'
    C6IN2XLARGE = 'c6in.2xlarge'
    C6IN4XLARGE = 'c6in.4xlarge'
    C6IN8XLARGE = 'c6in.8xlarge'
    C6IN12XLARGE = 'c6in.12xlarge'
    C6IN16XLARGE = 'c6in.16xlarge'
    C6IN24XLARGE = 'c6in.24xlarge'
    C6IN32XLARGE = 'c6in.32xlarge'
    M6INLARGE = 'm6in.large'
    M6INXLARGE = 'm6in.xlarge'
    M6IN2XLARGE = 'm6in.2xlarge'
    M6IN4XLARGE = 'm6in.4xlarge'
    M6IN8XLARGE = 'm6in.8xlarge'
    M6IN12XLARGE = 'm6in.12xlarge'
    M6IN16XLARGE = 'm6in.16xlarge'
    M6IN24XLARGE = 'm6in.24xlarge'
    M6IN32XLARGE = 'm6in.32xlarge'
    M6IDNLARGE = 'm6idn.large'
    M6IDNXLARGE = 'm6idn.xlarge'
    M6IDN2XLARGE = 'm6idn.2xlarge'
    M6IDN4XLARGE = 'm6idn.4xlarge'
    M6IDN8XLARGE = 'm6idn.8xlarge'
    M6IDN12XLARGE = 'm6idn.12xlarge'
    M6IDN16XLARGE = 'm6idn.16xlarge'
    M6IDN24XLARGE = 'm6idn.24xlarge'
    M6IDN32XLARGE = 'm6idn.32xlarge'
    R6INLARGE = 'r6in.large'
    R6INXLARGE = 'r6in.xlarge'
    R6IN2XLARGE = 'r6in.2xlarge'
    R6IN4XLARGE = 'r6in.4xlarge'
    R6IN8XLARGE = 'r6in.8xlarge'
    R6IN12XLARGE = 'r6in.12xlarge'
    R6IN16XLARGE = 'r6in.16xlarge'
    R6IN24XLARGE = 'r6in.24xlarge'
    R6IN32XLARGE = 'r6in.32xlarge'
    R6IDNLARGE = 'r6idn.large'
    R6IDNXLARGE = 'r6idn.xlarge'
    R6IDN2XLARGE = 'r6idn.2xlarge'
    R6IDN4XLARGE = 'r6idn.4xlarge'
    R6IDN8XLARGE = 'r6idn.8xlarge'
    R6IDN12XLARGE = 'r6idn.12xlarge'
    R6IDN16XLARGE = 'r6idn.16xlarge'
    R6IDN24XLARGE = 'r6idn.24xlarge'
    R6IDN32XLARGE = 'r6idn.32xlarge'
    C7GMETAL = 'c7g.metal'
    M7GMEDIUM = 'm7g.medium'
    M7GLARGE = 'm7g.large'
    M7GXLARGE = 'm7g.xlarge'
    M7G2XLARGE = 'm7g.2xlarge'
    M7G4XLARGE = 'm7g.4xlarge'
    M7G8XLARGE = 'm7g.8xlarge'
    M7G12XLARGE = 'm7g.12xlarge'
    M7G16XLARGE = 'm7g.16xlarge'
    M7GMETAL = 'm7g.metal'
    R7GMEDIUM = 'r7g.medium'
    R7GLARGE = 'r7g.large'
    R7GXLARGE = 'r7g.xlarge'
    R7G2XLARGE = 'r7g.2xlarge'
    R7G4XLARGE = 'r7g.4xlarge'
    R7G8XLARGE = 'r7g.8xlarge'
    R7G12XLARGE = 'r7g.12xlarge'
    R7G16XLARGE = 'r7g.16xlarge'
    R7GMETAL = 'r7g.metal'
    C6INMETAL = 'c6in.metal'
    M6INMETAL = 'm6in.metal'
    M6IDNMETAL = 'm6idn.metal'
    R6INMETAL = 'r6in.metal'
    R6IDNMETAL = 'r6idn.metal'
    INF2XLARGE = 'inf2.xlarge'
    INF28XLARGE = 'inf2.8xlarge'
    INF224XLARGE = 'inf2.24xlarge'
    INF248XLARGE = 'inf2.48xlarge'
    TRN1N32XLARGE = 'trn1n.32xlarge'
    I4GLARGE = 'i4g.large'
    I4GXLARGE = 'i4g.xlarge'
    I4G2XLARGE = 'i4g.2xlarge'
    I4G4XLARGE = 'i4g.4xlarge'
    I4G8XLARGE = 'i4g.8xlarge'
    I4G16XLARGE = 'i4g.16xlarge'
    HPC7G4XLARGE = 'hpc7g.4xlarge'
    HPC7G8XLARGE = 'hpc7g.8xlarge'
    HPC7G16XLARGE = 'hpc7g.16xlarge'
    C7GNMEDIUM = 'c7gn.medium'
    C7GNLARGE = 'c7gn.large'
    C7GNXLARGE = 'c7gn.xlarge'
    C7GN2XLARGE = 'c7gn.2xlarge'
    C7GN4XLARGE = 'c7gn.4xlarge'
    C7GN8XLARGE = 'c7gn.8xlarge'
    C7GN12XLARGE = 'c7gn.12xlarge'
    C7GN16XLARGE = 'c7gn.16xlarge'
    P548XLARGE = 'p5.48xlarge'
    M7ILARGE = 'm7i.large'
    M7IXLARGE = 'm7i.xlarge'
    M7I2XLARGE = 'm7i.2xlarge'
    M7I4XLARGE = 'm7i.4xlarge'
    M7I8XLARGE = 'm7i.8xlarge'
    M7I12XLARGE = 'm7i.12xlarge'
    M7I16XLARGE = 'm7i.16xlarge'
    M7I24XLARGE = 'm7i.24xlarge'
    M7I48XLARGE = 'm7i.48xlarge'
    M7IFLEXLARGE = 'm7i-flex.large'
    M7IFLEXXLARGE = 'm7i-flex.xlarge'
    M7IFLEX2XLARGE = 'm7i-flex.2xlarge'
    M7IFLEX4XLARGE = 'm7i-flex.4xlarge'
    M7IFLEX8XLARGE = 'm7i-flex.8xlarge'
    M7AMEDIUM = 'm7a.medium'
    M7ALARGE = 'm7a.large'
    M7AXLARGE = 'm7a.xlarge'
    M7A2XLARGE = 'm7a.2xlarge'
    M7A4XLARGE = 'm7a.4xlarge'
    M7A8XLARGE = 'm7a.8xlarge'
    M7A12XLARGE = 'm7a.12xlarge'
    M7A16XLARGE = 'm7a.16xlarge'
    M7A24XLARGE = 'm7a.24xlarge'
    M7A32XLARGE = 'm7a.32xlarge'
    M7A48XLARGE = 'm7a.48xlarge'
    M7AMETAL48XL = 'm7a.metal-48xl'
    HPC7A12XLARGE = 'hpc7a.12xlarge'
    HPC7A24XLARGE = 'hpc7a.24xlarge'
    HPC7A48XLARGE = 'hpc7a.48xlarge'
    HPC7A96XLARGE = 'hpc7a.96xlarge'
    C7GDMEDIUM = 'c7gd.medium'
    C7GDLARGE = 'c7gd.large'
    C7GDXLARGE = 'c7gd.xlarge'
    C7GD2XLARGE = 'c7gd.2xlarge'
    C7GD4XLARGE = 'c7gd.4xlarge'
    C7GD8XLARGE = 'c7gd.8xlarge'
    C7GD12XLARGE = 'c7gd.12xlarge'
    C7GD16XLARGE = 'c7gd.16xlarge'
    M7GDMEDIUM = 'm7gd.medium'
    M7GDLARGE = 'm7gd.large'
    M7GDXLARGE = 'm7gd.xlarge'
    M7GD2XLARGE = 'm7gd.2xlarge'
    M7GD4XLARGE = 'm7gd.4xlarge'
    M7GD8XLARGE = 'm7gd.8xlarge'
    M7GD12XLARGE = 'm7gd.12xlarge'
    M7GD16XLARGE = 'm7gd.16xlarge'
    R7GDMEDIUM = 'r7gd.medium'
    R7GDLARGE = 'r7gd.large'
    R7GDXLARGE = 'r7gd.xlarge'
    R7GD2XLARGE = 'r7gd.2xlarge'
    R7GD4XLARGE = 'r7gd.4xlarge'
    R7GD8XLARGE = 'r7gd.8xlarge'
    R7GD12XLARGE = 'r7gd.12xlarge'
    R7GD16XLARGE = 'r7gd.16xlarge'
    R7AMEDIUM = 'r7a.medium'
    R7ALARGE = 'r7a.large'
    R7AXLARGE = 'r7a.xlarge'
    R7A2XLARGE = 'r7a.2xlarge'
    R7A4XLARGE = 'r7a.4xlarge'
    R7A8XLARGE = 'r7a.8xlarge'
    R7A12XLARGE = 'r7a.12xlarge'
    R7A16XLARGE = 'r7a.16xlarge'
    R7A24XLARGE = 'r7a.24xlarge'
    R7A32XLARGE = 'r7a.32xlarge'
    R7A48XLARGE = 'r7a.48xlarge'
    C7ILARGE = 'c7i.large'
    C7IXLARGE = 'c7i.xlarge'
    C7I2XLARGE = 'c7i.2xlarge'
    C7I4XLARGE = 'c7i.4xlarge'
    C7I8XLARGE = 'c7i.8xlarge'
    C7I12XLARGE = 'c7i.12xlarge'
    C7I16XLARGE = 'c7i.16xlarge'
    C7I24XLARGE = 'c7i.24xlarge'
    C7I48XLARGE = 'c7i.48xlarge'
    MAC2M2PROMETAL = 'mac2-m2pro.metal'
    R7IZLARGE = 'r7iz.large'
    R7IZXLARGE = 'r7iz.xlarge'
    R7IZ2XLARGE = 'r7iz.2xlarge'
    R7IZ4XLARGE = 'r7iz.4xlarge'
    R7IZ8XLARGE = 'r7iz.8xlarge'
    R7IZ12XLARGE = 'r7iz.12xlarge'
    R7IZ16XLARGE = 'r7iz.16xlarge'
    R7IZ32XLARGE = 'r7iz.32xlarge'
    C7AMEDIUM = 'c7a.medium'
    C7ALARGE = 'c7a.large'
    C7AXLARGE = 'c7a.xlarge'
    C7A2XLARGE = 'c7a.2xlarge'
    C7A4XLARGE = 'c7a.4xlarge'
    C7A8XLARGE = 'c7a.8xlarge'
    C7A12XLARGE = 'c7a.12xlarge'
    C7A16XLARGE = 'c7a.16xlarge'
    C7A24XLARGE = 'c7a.24xlarge'
    C7A32XLARGE = 'c7a.32xlarge'
    C7A48XLARGE = 'c7a.48xlarge'
    C7AMETAL48XL = 'c7a.metal-48xl'
    R7AMETAL48XL = 'r7a.metal-48xl'
    R7ILARGE = 'r7i.large'
    R7IXLARGE = 'r7i.xlarge'
    R7I2XLARGE = 'r7i.2xlarge'
    R7I4XLARGE = 'r7i.4xlarge'
    R7I8XLARGE = 'r7i.8xlarge'
    R7I12XLARGE = 'r7i.12xlarge'
    R7I16XLARGE = 'r7i.16xlarge'
    R7I24XLARGE = 'r7i.24xlarge'
    R7I48XLARGE = 'r7i.48xlarge'
    DL2Q24XLARGE = 'dl2q.24xlarge'
    MAC2M2METAL = 'mac2-m2.metal'
    I4I12XLARGE = 'i4i.12xlarge'
    I4I24XLARGE = 'i4i.24xlarge'
    C7IMETAL24XL = 'c7i.metal-24xl'
    C7IMETAL48XL = 'c7i.metal-48xl'
    M7IMETAL24XL = 'm7i.metal-24xl'
    M7IMETAL48XL = 'm7i.metal-48xl'
    R7IMETAL24XL = 'r7i.metal-24xl'
    R7IMETAL48XL = 'r7i.metal-48xl'
    R7IZMETAL16XL = 'r7iz.metal-16xl'
    R7IZMETAL32XL = 'r7iz.metal-32xl'
    C7GDMETAL = 'c7gd.metal'
    M7GDMETAL = 'm7gd.metal'
    R7GDMETAL = 'r7gd.metal'
    G6XLARGE = 'g6.xlarge'
    G62XLARGE = 'g6.2xlarge'
    G64XLARGE = 'g6.4xlarge'
    G68XLARGE = 'g6.8xlarge'
    G612XLARGE = 'g6.12xlarge'
    G616XLARGE = 'g6.16xlarge'
    G624XLARGE = 'g6.24xlarge'
    G648XLARGE = 'g6.48xlarge'
    GR64XLARGE = 'gr6.4xlarge'
    GR68XLARGE = 'gr6.8xlarge'
    C7IFLEXLARGE = 'c7i-flex.large'
    C7IFLEXXLARGE = 'c7i-flex.xlarge'
    C7IFLEX2XLARGE = 'c7i-flex.2xlarge'
    C7IFLEX4XLARGE = 'c7i-flex.4xlarge'
    C7IFLEX8XLARGE = 'c7i-flex.8xlarge'
    U7I12TB224XLARGE = 'u7i-12tb.224xlarge'
    U7IN16TB224XLARGE = 'u7in-16tb.224xlarge'
    U7IN24TB224XLARGE = 'u7in-24tb.224xlarge'
    U7IN32TB224XLARGE = 'u7in-32tb.224xlarge'
    U7IB12TB224XLARGE = 'u7ib-12tb.224xlarge'
    C7GNMETAL = 'c7gn.metal'
    R8GMEDIUM = 'r8g.medium'
    R8GLARGE = 'r8g.large'
    R8GXLARGE = 'r8g.xlarge'
    R8G2XLARGE = 'r8g.2xlarge'
    R8G4XLARGE = 'r8g.4xlarge'
    R8G8XLARGE = 'r8g.8xlarge'
    R8G12XLARGE = 'r8g.12xlarge'
    R8G16XLARGE = 'r8g.16xlarge'
    R8G24XLARGE = 'r8g.24xlarge'
    R8G48XLARGE = 'r8g.48xlarge'
    R8GMETAL24XL = 'r8g.metal-24xl'
    R8GMETAL48XL = 'r8g.metal-48xl'
    MAC2M1ULTRAMETAL = 'mac2-m1ultra.metal'


from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class Group(BaseResponse):
    GroupName: Optional[str]
    GroupId: Optional[str]


class Monitoring(BaseResponse):
    State: Optional[MonitoringState]


class Placement(BaseResponse):
    AvailabilityZone: Optional[str]
    Affinity: Optional[str]
    GroupName: Optional[str]
    PartitionNumber: Optional[int]
    HostId: Optional[str]
    Tenancy: Optional[Tenancy]
    SpreadDomain: Optional[str]
    HostResourceGroupArn: Optional[str]
    GroupId: Optional[str]


class ProductCode(BaseResponse):
    ProductCodeId: Optional[str]
    ProductCodeType: Optional[ProductCodeType]


class State(BaseResponse):
    Code: Optional[int]
    Name: Optional[Name]


class Ebs(BaseResponse):
    AttachTime: Optional[datetime]
    DeleteOnTermination: Optional[bool]
    Status: Optional[EbsStatus]
    VolumeId: Optional[str]
    AssociatedResource: Optional[str]
    VolumeOwnerId: Optional[str]


class BlockDeviceMapping(BaseResponse):
    DeviceName: Optional[str]
    Ebs: Optional[Ebs]


class IamInstanceProfile(BaseResponse):
    Arn: Optional[str]
    Id: Optional[str]


class ElasticGpuAssociation(BaseResponse):
    ElasticGpuId: Optional[str]
    ElasticGpuAssociationId: Optional[str]
    ElasticGpuAssociationState: Optional[str]
    ElasticGpuAssociationTime: Optional[str]


class ElasticInferenceAcceleratorAssociation(BaseResponse):
    ElasticInferenceAcceleratorArn: Optional[str]
    ElasticInferenceAcceleratorAssociationId: Optional[str]
    ElasticInferenceAcceleratorAssociationState: Optional[str]
    ElasticInferenceAcceleratorAssociationTime: Optional[datetime]


class Association(BaseResponse):
    CarrierIp: Optional[str]
    CustomerOwnedIp: Optional[str]
    IpOwnerId: Optional[str]
    PublicDnsName: Optional[str]
    PublicIp: Optional[str]


class EnaSrdUdpSpecification(BaseResponse):
    EnaSrdUdpEnabled: Optional[bool]


class EnaSrdSpecification(BaseResponse):
    EnaSrdEnabled: Optional[bool]
    EnaSrdUdpSpecification: Optional[EnaSrdUdpSpecification]


class Attachment(BaseResponse):
    AttachTime: Optional[datetime]
    AttachmentId: Optional[str]
    DeleteOnTermination: Optional[bool]
    DeviceIndex: Optional[int]
    Status: Optional[AttachmentStatus]
    NetworkCardIndex: Optional[int]
    EnaSrdSpecification: Optional[EnaSrdSpecification]


class Ipv6Address(BaseResponse):
    Ipv6Address: Optional[str]
    IsPrimaryIpv6: Optional[bool]


class PrivateIpAddress(BaseResponse):
    Association: Optional[Association]
    Primary: Optional[bool]
    PrivateDnsName: Optional[str]
    PrivateIpAddress: Optional[str]


class Ipv4Prefix(BaseResponse):
    Ipv4Prefix: Optional[str]


class Ipv6Prefix(BaseResponse):
    Ipv6Prefix: Optional[str]


class ConnectionTrackingConfiguration(BaseResponse):
    TcpEstablishedTimeout: Optional[int]
    UdpStreamTimeout: Optional[int]
    UdpTimeout: Optional[int]


class NetworkInterface(BaseResponse):
    Association: Optional[Association]
    Attachment: Optional[Attachment]
    Description: Optional[str]
    Groups: Optional[List[Group]]
    Ipv6Addresses: Optional[List[Ipv6Address]]
    MacAddress: Optional[str]
    NetworkInterfaceId: Optional[str]
    OwnerId: Optional[str]
    PrivateDnsName: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddresses: Optional[List[PrivateIpAddress]]
    SourceDestCheck: Optional[bool]
    Status: Optional[NetworkInterfacesStatus]
    SubnetId: Optional[str]
    VpcId: Optional[str]
    InterfaceType: Optional[str]
    Ipv4Prefixes: Optional[List[Ipv4Prefix]]
    Ipv6Prefixes: Optional[List[Ipv6Prefix]]
    ConnectionTrackingConfiguration: Optional[ConnectionTrackingConfiguration]


class SecurityGroup(BaseResponse):
    GroupName: Optional[str]
    GroupId: Optional[str]


class StateReason(BaseResponse):
    Code: Optional[str]
    Message: Optional[str]


class Tag(BaseResponse):
    Key: Optional[str]
    Value: Optional[str]


class CpuOptions(BaseResponse):
    CoreCount: Optional[int]
    ThreadsPerCore: Optional[int]
    AmdSevSnp: Optional[AmdSevSnp]


class CapacityReservationTarget(BaseResponse):
    CapacityReservationId: Optional[str]
    CapacityReservationResourceGroupArn: Optional[str]


class CapacityReservationSpecification(BaseResponse):
    CapacityReservationPreference: Optional[CapacityReservationPreference]
    CapacityReservationTarget: Optional[CapacityReservationTarget]


class HibernationOptions(BaseResponse):
    Configured: Optional[bool]


class License(BaseResponse):
    LicenseConfigurationArn: Optional[str]


class MetadataOptions(BaseResponse):
    State: Optional[MetadataOptionsState]
    HttpTokens: Optional[HttpTokens]
    HttpPutResponseHopLimit: Optional[int]
    HttpEndpoint: Optional[HttpEndpoint]
    HttpProtocolIpv6: Optional[HttpProtocolIpv6]
    InstanceMetadataTags: Optional[InstanceMetadataTags]


class EnclaveOptions(BaseResponse):
    Enabled: Optional[bool]


class PrivateDnsNameOptions(BaseResponse):
    HostnameType: Optional[HostnameType]
    EnableResourceNameDnsARecord: Optional[bool]
    EnableResourceNameDnsAAAARecord: Optional[bool]


class MaintenanceOptions(BaseResponse):
    AutoRecovery: Optional[AutoRecovery]


class Instance(BaseResponse):
    AmiLaunchIndex: Optional[int]
    ImageId: Optional[str]
    InstanceId: Optional[str]
    InstanceType: Optional[InstanceType]
    KernelId: Optional[str]
    KeyName: Optional[str]
    LaunchTime: Optional[datetime]
    Monitoring: Optional[Monitoring]
    Placement: Optional[Placement]
    Platform: Optional[str]
    PrivateDnsName: Optional[str]
    PrivateIpAddress: Optional[str]
    ProductCodes: Optional[List[ProductCode]]
    PublicDnsName: Optional[str]
    PublicIpAddress: Optional[str]
    RamdiskId: Optional[str]
    State: Optional[State]
    StateTransitionReason: Optional[str]
    SubnetId: Optional[str]
    VpcId: Optional[str]
    Architecture: Optional[Architecture]
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]]
    ClientToken: Optional[str]
    EbsOptimized: Optional[bool]
    EnaSupport: Optional[bool]
    Hypervisor: Optional[Hypervisor]
    IamInstanceProfile: Optional[IamInstanceProfile]
    InstanceLifecycle: Optional[InstanceLifecycle]
    ElasticGpuAssociations: Optional[List[ElasticGpuAssociation]]
    ElasticInferenceAcceleratorAssociations: Optional[List[
        ElasticInferenceAcceleratorAssociation]]
    NetworkInterfaces: Optional[List[NetworkInterface]]
    OutpostArn: Optional[str]
    RootDeviceName: Optional[str]
    RootDeviceType: Optional[RootDeviceType]
    SecurityGroups: Optional[List[SecurityGroup]]
    SourceDestCheck: Optional[bool]
    SpotInstanceRequestId: Optional[str]
    SriovNetSupport: Optional[str]
    StateReason: Optional[StateReason]
    Tags: Optional[List[Tag]]
    VirtualizationType: Optional[VirtualizationType]
    CpuOptions: Optional[CpuOptions]
    CapacityReservationId: Optional[str]
    CapacityReservationSpecification: Optional[CapacityReservationSpecification
        ]
    HibernationOptions: Optional[HibernationOptions]
    Licenses: Optional[List[License]]
    MetadataOptions: Optional[MetadataOptions]
    EnclaveOptions: Optional[EnclaveOptions]
    BootMode: Optional[BootMode]
    PlatformDetails: Optional[str]
    UsageOperation: Optional[str]
    UsageOperationUpdateTime: Optional[datetime]
    PrivateDnsNameOptions: Optional[PrivateDnsNameOptions]
    Ipv6Address: Optional[str]
    TpmSupport: Optional[str]
    MaintenanceOptions: Optional[MaintenanceOptions]
    CurrentInstanceBootMode: Optional[CurrentInstanceBootMode]


class Reservation(BaseResponse):
    Groups: Optional[List[Group]]
    Instances: Optional[List[Instance]]
    OwnerId: Optional[str]
    RequesterId: Optional[str]
    ReservationId: Optional[str]


class DescribeInstancesResponse(BaseResponse):
    Reservations: Optional[List[Reservation]]
    NextToken: Optional[str]
