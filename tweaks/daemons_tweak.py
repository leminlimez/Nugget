from enum import Enum

class Daemon(Enum):
    thermalmonitord = ["com.apple.thermalmonitord"]
    OTA = ["com.apple.OTATaskingAgent"]
    UsageTrackingAgent = ["com.apple.UsageTrackingAgent"]
    GameCenter = ["com.apple.gamed"]
    ScreenTime = [
        "com.apple.ScreenTimeAgent",
        "com.apple.homed",
        "com.apple.familycircled"
    ]
    CrashReports = [
        "com.apple.DumpBasebandCrash",
        "com.apple.ReportCrash",
        "com.apple.rtcreportingd",
        "com.apple.spindump",
        "com.apple.system.logger",
        "com.apple.syslogd", 
        "com.apple.wifianalyticsd"
    ]
    ATWAKEUP = ["com.apple.atc.atwakeup"]
    Tips = ["com.apple.tipsd"]
    VPN = ["com.apple.racoon"]
    ChineseLAN = [
        "com.apple.wapic",
        "com.apple.wifi.wapic"
    ]
    HealthKit = ["com.apple.healthd"]
    AirPrint = ["com.apple.printd"]
    AssistiveTouch = ["com.apple.assistivetouchd"]
    iCloud = ["com.apple.itunescloudd"]
    InternetTethering = ["com.apple.MobileInternetSharing"]
    PassBook = ["com.apple.passd"]
    Spotlight = ["com.apple.searchd"]
    VoiceControl = [
        "com.apple.assistant_service",
        "com.apple.assistantd",
        "com.apple.voiced"
    ]
