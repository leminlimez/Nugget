#include <iostream>
#include <fstream>
#include <cstring>
#include <string>

// this is because Windows is stupid and MSVC needs arguments that none of the python libraries allow
// compile command:
// g++ status_setter.cpp -o ../status_setter_windows.exe -mno-ms-bitfields -malign-double

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
     * ./status_setter <in_file> <out_file>
     */

    /*
     * File Structure:
     1. [overrideItemIsEnabled]
     2. [itemIsEnabled]
     3. [timeString]
     4. [shortTimeString]
    */

    StatusBarOverrideData overrides = {};
    std::ifstream infile(argv[1]);
    int n = 0;
    // read through the file line by line
    for (std::string line; getline(infile, line); ) {
        if (n == 0) {
            strToBoolArray(line, 45, overrides.overrideItemIsEnabled);
        }
        // Values
        else if (n == 1) {
            strToBoolArray(line, 45, overrides.values.itemIsEnabled);
        }
        else if (n == 2) {
            strncpy(overrides.values.timeString, line.c_str(), 64);
        }
        else if (n == 3) {
            strncpy(overrides.values.shortTimeString, line.c_str(), 64);
        }
        else if (n == 4) {
            strncpy(overrides.values.dateString, line.c_str(), 256);
        }
        else if (n == 5) {
            strncpy(overrides.values.serviceString, line.c_str(), 100);
        }
        else if (n == 6) {
            strncpy(overrides.values.secondaryServiceString, line.c_str(), 100);
        }
        else if (n == 7) {
            strncpy(overrides.values.serviceCrossfadeString, line.c_str(), 100);
        }
        else if (n == 8) {
            strncpy(overrides.values.secondaryServiceCrossfadeString, line.c_str(), 100);
        }
        else if (n == 9) {
            strncpy(overrides.values.batteryDetailString, line.c_str(), 150);
        }
        else if (n == 10) {
            strncpy(overrides.values.primaryServiceBadgeString, line.c_str(), 100);
        }
        else if (n == 11) {
            strncpy(overrides.values.secondaryServiceBadgeString, line.c_str(), 100);
        }
        else if (n == 12) {
            strncpy(overrides.values.breadcrumbTitle, line.c_str(), 256);
        }
        // Override Data
        else if (n == 13) {
            overrides.overrideTimeString = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 14) {
            overrides.overrideDateString = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 15) {
            overrides.overrideServiceString = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 16) {
            overrides.overrideSecondaryServiceString = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 17) {
            overrides.overrideBatteryDetailString = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 18) {
            overrides.overridePrimaryServiceBadgeString = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 19) {
            overrides.overrideSecondaryServiceBadgeString = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 20) {
            overrides.overrideBreadcrumb = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 21) {
            overrides.overrideDisplayRawWiFiSignal = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 22) {
            overrides.overrideDisplayRawGSMSignal = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 23) {
            overrides.values.displayRawWiFiSignal = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 24) {
            overrides.values.displayRawGSMSignal = line.c_str()[0] == '1' ? 1 : 0;
        }
        // Data Network Types
        else if (n == 25) {
            overrides.overrideDataNetworkType = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 26) {
            overrides.values.dataNetworkType = std::stoi(line);
        }
        else if (n == 27) {
            overrides.overrideSecondaryDataNetworkType = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 28) {
            overrides.values.secondaryDataNetworkType = std::stoi(line);
        }
        // Slider bars
        else if (n == 29) {
            overrides.overrideGSMSignalStrengthBars = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 30) {
            overrides.values.GSMSignalStrengthBars = std::stoi(line);
        }
        else if (n == 31) {
            overrides.overrideSecondaryGSMSignalStrengthBars = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 32) {
            overrides.values.secondaryGSMSignalStrengthBars = std::stoi(line);
        }
        else if (n == 33) {
            overrides.overrideBatteryCapacity = line.c_str()[0] == '1' ? 1 : 0;
        }
        else if (n == 34) {
            overrides.values.batteryCapacity = std::stoi(line);
        }
        else if (n == 35) {
            overrides.overrideWiFiSignalStrengthBars = std::stoi(line);
        }
        else if (n == 36) {
            overrides.values.WiFiSignalStrengthBars = std::stoi(line);
        }
        n++;
    }
    infile.close();

    // Write to the file
    std::string location(argv[2]);
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