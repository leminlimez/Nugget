from enum import Enum

class Daemon(Enum):
    thermalmonitord = ["com.apple.thermalmonitord"]
    OTA = [
        "com.apple.mobile.softwareupdated",
        "com.apple.OTATaskingAgent",
        "com.apple.softwareupdateservicesd"
    ]
    UsageTrackingAgent = ["com.apple.UsageTrackingAgent"]
    GameCenter = ["com.apple.gamed"]
    ScreenTime = [
        "com.apple.ScreenTimeAgent",
        "com.apple.homed",
        "com.apple.familycircled"
    ]
    CrashReports = [
        "com.apple.ReportCrash",
        "com.apple.ReportCrash.Jetsam",
        "com.apple.ReportMemoryException",
        "com.apple.OTACrashCopier",
        "com.apple.analyticsd",
        "com.apple.wifianalyticsd",
        "com.apple.aslmanager",
        "com.apple.coresymbolicationd",
        "com.apple.crash_mover",
        "com.apple.crashreportcopymobile",
        "com.apple.DumpBasebandCrash",
        "com.apple.DumpPanic",
        "com.apple.logd",
        "com.apple.logd.admin",
        "com.apple.logd.events",
        "com.apple.logd.watchdog",
        "com.apple.logd_helper",
        "com.apple.logd_reporter",
        "com.apple.logd_reporter.report_statistics",
        "com.apple.system.logger",
        "com.apple.hangreporter",
        "com.apple.hangtracerd",
        "com.apple.spindump",
        "com.apple.rtcreportingd",
        "com.apple.syslogd"
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
    Spotlight = [
        "com.apple.searchd",
        "com.apple.corespotlightservice",
        "com.apple.spotlightknowledged",
        "com.apple.spotlightknowledged.updater",
        "com.apple.spotlight.IndexAgent"
    ]
    VoiceControl = [
        "com.apple.assistant_service",
        "com.apple.assistantd",
        "com.apple.voiced"
    ]
    NanoTimeKit = ["com.apple.nanotimekitcompaniond"]