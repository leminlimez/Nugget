#include <iostream>
#include <fstream>
#include <cstring>
#include <string>

// this is because Windows is stupid and MSVC needs arguments that none of the python libraries allow

struct StatusBarRawData
{
    bool itemIsEnabled[45];
    char padding;
    char timeString[64];
    char shortTimeString[64];
    char dateString[256];
    int GSMSignalStrengthRaw;
    int secondaryGSMSignalStrengthRaw;
    int GSMSignalStrengthBars;
    int secondaryGSMSignalStrengthBars;
    char serviceString[100];
    char secondaryServiceString[100];
    char serviceCrossfadeString[100];
    char secondaryServiceCrossfadeString[100];
    char serviceImages[2][100];
    char operatorDirectory[1024];
    unsigned int serviceContentType;
    unsigned int secondaryServiceContentType;
    unsigned int cellLowDataModeActive : 1;
    unsigned int secondaryCellLowDataModeActive : 1;
    int WiFiSignalStrengthRaw;
    int WiFiSignalStrengthBars;
    unsigned int WiFiLowDataModeActive : 1;
    unsigned int dataNetworkType;
    unsigned int secondaryDataNetworkType;
    int batteryCapacity;
    unsigned int batteryState;
    char batteryDetailString[150];
    int bluetoothBatteryCapacity;
    int thermalColor;
    unsigned int thermalSunlightMode : 1;
    unsigned int slowActivity : 1;
    unsigned int syncActivity : 1;
    char activityDisplayId[256];
    unsigned int bluetoothConnected : 1;
    unsigned int displayRawGSMSignal : 1;
    unsigned int displayRawWiFiSignal : 1;
    unsigned int locationIconType : 1;
    unsigned int voiceControlIconType : 2;
    unsigned int quietModeInactive : 1;
    unsigned int tetheringConnectionCount;
    unsigned int batterySaverModeActive : 1;
    unsigned int deviceIsRTL : 1;
    unsigned int lock : 1;
    char breadcrumbTitle[256];
    char breadcrumbSecondaryTitle[256];
    char personName[100];
    unsigned int electronicTollCollectionAvailable : 1;
    unsigned int radarAvailable : 1;
    unsigned int WiFiLinkWarning : 1;
    unsigned int WiFiSearching : 1;
    double backgroundActivityDisplayStartDate;
    unsigned int shouldShowEmergencyOnlyStatus : 1;
    unsigned int secondaryCellularConfigured : 1;
    char primaryServiceBadgeString[100];
    char secondaryServiceBadgeString[100];
    char quietModeImage[256];
    unsigned int extra1 : 1;
};

struct StatusBarOverrideData
{
    bool overrideItemIsEnabled[45];
    char padding;
    unsigned int overrideTimeString : 1;
    unsigned int overrideDateString : 1;
    unsigned int overrideGSMSignalStrengthRaw : 1;
    unsigned int overrideSecondaryGSMSignalStrengthRaw : 1;
    unsigned int overrideGSMSignalStrengthBars : 1;
    unsigned int overrideSecondaryGSMSignalStrengthBars : 1;
    unsigned int overrideServiceString : 1;
    unsigned int overrideSecondaryServiceString : 1;
    unsigned int overrideServiceImages : 2;
    unsigned int overrideOperatorDirectory : 1;
    unsigned int overrideServiceContentType : 1;
    unsigned int overrideSecondaryServiceContentType : 1;
    unsigned int overrideWiFiSignalStrengthRaw : 1;
    unsigned int overrideWiFiSignalStrengthBars : 1;
    unsigned int overrideDataNetworkType : 1;
    unsigned int overrideSecondaryDataNetworkType : 1;
    unsigned int disallowsCellularDataNetworkTypes : 1;
    unsigned int overrideBatteryCapacity : 1;
    unsigned int overrideBatteryState : 1;
    unsigned int overrideBatteryDetailString : 1;
    unsigned int overrideBluetoothBatteryCapacity : 1;
    unsigned int overrideThermalColor : 1;
    unsigned int overrideSlowActivity : 1;
    unsigned int overrideActivityDisplayId : 1;
    unsigned int overrideBluetoothConnected : 1;
    unsigned int overrideBreadcrumb : 1;
    unsigned int overrideLock;
    unsigned int overrideDisplayRawGSMSignal : 1;
    unsigned int overrideDisplayRawWiFiSignal : 1;
    unsigned int overridePersonName : 1;
    unsigned int overrideWiFiLinkWarning : 1;
    unsigned int overrideSecondaryCellularConfigured : 1;
    unsigned int overridePrimaryServiceBadgeString : 1;
    unsigned int overrideSecondaryServiceBadgeString : 1;
    unsigned int overrideQuietModeImage : 1;
    unsigned int overrideExtra1 : 1;
    StatusBarRawData values;
};

void strToBoolArray(std::string s, size_t len, bool *arr) {
    for (int i = 0; i < len; i++) {
        char c = s.c_str()[i];
        if (c == '0') {
            arr[i] = false;
        } else {
            arr[i] = true;
        }
    }
}

int main(int argc, char *argv[]) {
    /*
     * Usage
     * ./status_setter <out_file> [--arg value]
     */

    StatusBarOverrideData overrides = {};
    for (int i = 2; i < argc; i+=2) {
        // set arg in struct
        std::string k(argv[i]);
        std::string v(argv[i+1]);
        if (k == "--overrideItemIsEnabled") {
            strToBoolArray(v, 45, overrides.overrideItemIsEnabled);
        }
        // Values
        else if (k == "--itemIsEnabled") {
            strToBoolArray(v, 45, overrides.values.itemIsEnabled);
        }
        else if (k == "--timeString") {
            strncpy(overrides.values.timeString, argv[i+1], 64);
        }
        else if (k == "--shortTimeString") {
            strncpy(overrides.values.shortTimeString, argv[i+1], 64);
        }
        else if (k == "--dateString") {
            strncpy(overrides.values.dateString, argv[i+1], 256);
        }
        else if (k == "--serviceString") {
            strncpy(overrides.values.serviceString, argv[i+1], 100);
        }
        else if (k == "--secondaryServiceString") {
            strncpy(overrides.values.secondaryServiceString, argv[i+1], 100);
        }
        else if (k == "--serviceCrossfadeString") {
            strncpy(overrides.values.serviceCrossfadeString, argv[i+1], 100);
        }
        else if (k == "--secondaryServiceCrossfadeString") {
            strncpy(overrides.values.secondaryServiceCrossfadeString, argv[i+1], 100);
        }
        else if (k == "--batteryDetailString") {
            strncpy(overrides.values.batteryDetailString, argv[i+1], 150);
        }
        else if (k == "--primaryServiceBadgeString") {
            strncpy(overrides.values.primaryServiceBadgeString, argv[i+1], 100);
        }
        else if (k == "--secondaryServiceBadgeString") {
            strncpy(overrides.values.secondaryServiceBadgeString, argv[i+1], 100);
        }
        else if (k == "--breadcrumbTitle") {
            strncpy(overrides.values.breadcrumbTitle, argv[i+1], 256);
        }
        // Override Data
        else if (k == "--overrideTimeString") {
            overrides.overrideTimeString = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--overrideDateString") {
            overrides.overrideDateString = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--overrideServiceString") {
            overrides.overrideServiceString = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--overrideSecondaryServiceString") {
            overrides.overrideSecondaryServiceString = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--overrideBatteryDetailString") {
            overrides.overrideBatteryDetailString = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--overridePrimaryServiceBadgeString") {
            overrides.overridePrimaryServiceBadgeString = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--overrideSecondaryServiceBadgeString") {
            overrides.overrideSecondaryServiceBadgeString = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--overrideBreadcrumb") {
            overrides.overrideBreadcrumb = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--overrideDisplayRawWifiSignal") {
            overrides.overrideDisplayRawWiFiSignal = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--overrideDisplayRawGSMSignal") {
            overrides.overrideDisplayRawGSMSignal = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--displayRawWifiSignal") {
            overrides.values.displayRawWiFiSignal = v.c_str()[0] == '1' ? 1 : 0;
        }
        else if (k == "--displayRawGSMSignal") {
            overrides.values.displayRawGSMSignal = v.c_str()[0] == '1' ? 1 : 0;
        }
    }

    // Write to the file
    std::string location(argv[1]);
    std::ofstream outfile(location.c_str(), std::ofstream::binary);
    if (!outfile) {
        perror("openfile");
        return 1;
    }

    char padding[256] = {'\0'};
    outfile.write(reinterpret_cast<char *>(&overrides), sizeof(StatusBarOverrideData));
    outfile.write(padding, sizeof(padding));

    return 0;
}