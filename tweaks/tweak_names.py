from enum import Enum, auto

class TweakID(Enum):
    # misc pages
    PosterBoard = auto()
    Templates = auto()
    StatusBar = auto()

    # mga
    DynamicIsland = auto()
    ModelName = auto()
    BootChime = auto()
    ChargeLimit = auto()
    CollisionSOS = auto()
    TapToWake = auto()
    CameraButton = auto()
    Parallax = auto()
    StageManager = auto()
    iPadOS = auto()
    iPadOSCacheData = auto()
    iPadApps = auto()
    Shutter = auto()
    FindMyFriends = auto()
    Pencil = auto()
    ActionButton = auto()
    InternalStorage = auto()
    InternalInstall = auto()
    AOD = auto()
    AODVibrancy = auto()
    RdarFix = auto()

    # eligibility
    EUEnabler = auto()
    AIEligibility = auto()
    AIGestalt = auto()
    SpoofModel = auto()
    SpoofHardware = auto()
    SpoofCPU = auto()

    # feature flags
    ClockAnim = auto()
    Lockscreen = auto()
    PhotoUI = auto()
    AI = auto()

    # springboard
    LockScreenFootnote = auto()
    AirDropDisableTimeLimit = auto()
    SBDontLockAfterCrash = auto()
    SBDontDimOrLockOnAC = auto()
    SBHideLowPowerAlerts = auto()
    SBHideACPower = auto()
    SBNeverBreadcrumb = auto()
    SBShowSupervisionTextOnLockScreen = auto()
    AirplaySupport = auto()
    SBMinimumLockscreenIdleTime = auto()
    SBAlwaysShowSystemApertureInSnapshots = auto()
    SBShowAuthenticationEngineeringUI = auto()
    UseFloatingTabBar = auto()

    # internal
    ForceSolariumFallback = auto()
    IgnoreSolariumLinkedOnCheck = auto()
    NoLiquidClock = auto()
    NoLiquidDock = auto()
    SBBuildNumber = auto()
    RTL = auto()
    LTR = auto()
    SBIconVisibility = auto()
    MetalForceHudEnabled = auto()
    iMessageDiagnosticsEnabled = auto()
    IDSDiagnosticsEnabled = auto()
    VCDiagnosticsEnabled = auto()
    AccessoryDeveloperEnabled = auto()
    KeyFlick = auto()
    AppStoreDebug = auto()
    NotesDebugMode = auto()
    BKDigitizerVisualizeTouches = auto()
    BKHideAppleLogoOnLaunch = auto()
    EnableWakeGestureHaptic = auto()
    PlaySoundOnPaste = auto()
    AnnounceAllPastes = auto()

    # risky
    DisableOTAFile = auto()
    CustomResolution = auto()
    # daemons
    Daemons = auto()
    ClearScreenTimeAgentPlist = auto()